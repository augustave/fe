#!/usr/bin/env python3
"""
Fé — binding pipeline.

Renders each spread HTML at its NATIVE dimensions (1440px / 15in wide,
variable height, portrait-aspect) under print-media emulation, then
concatenates the pages into the bound Volume 01 PDF.

Do NOT force 17in x 11in landscape. The folios ship an @page rule that
declares landscape with a 0.4in margin; downscaling a 1440px spread into
that box destroys legibility. This script overrides the page size
(prefer_css_page_size=False) and renders ONE tall page per spread at the
spread's own measured height, so nothing is scaled or paginated.

Requires: playwright (chromium) + pypdf.
Run:      ./.venv/bin/python bind.py
"""

import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

HERE = Path(__file__).resolve().parent

# Source spreads. CANON (No.00) is the system's key and leads every cut.
COVER      = "cover.html"                     # cover / editor's note
CANON      = "canon_form_spread.html"         # No.00 CANON x FORM        (no mark)
FALLOW     = "fallow_fe_spread.html"          # No.01 FALLOW x FE         Slow Red
ASSAY      = "assay_ur_spread.html"           # No.02 ASSAY x UR          Slag Mark
MARGIN     = "margin_thurs_spread.html"       # No.03 MARGIN x THURS      Margin Gold
MANIFEST   = "manifest_intent_spread.html"    # No.04 MANIFEST x INTENT   Bind Blue
WRIT       = "writ_oath_spread.html"          # No.05 WRIT x OATH         Crown Indigo
PROVENANCE = "provenance_memory_spread.html"  # No.06 PROVENANCE x MEMORY Compact Green
COMMISSION = "commission_name_spread.html"    # No.07 COMMISSION x NAME   Sigil Mauve
COLOPHON   = "colophon.html"                   # closing colophon — Vol 01 complete

# Binding cuts. Sequence is NOT locked discipline, so re-ordering is a
# legal variation (see VARIATIONS_register.md — VR.06 spectrum, VR.07 cuts).
ORDERS = {
    # canonical: cover + No.00 -> No.07 + closing colophon
    "edition":      [COVER, CANON, FALLOW, ASSAY, MARGIN, MANIFEST, WRIT, PROVENANCE, COMMISSION, COLOPHON],
    # VR.06 — by mark hue: red -> orange -> gold -> green -> blue -> indigo -> mauve
    "spectrum":     [COVER, CANON, FALLOW, ASSAY, MARGIN, PROVENANCE, MANIFEST, WRIT, COMMISSION, COLOPHON],
    # VR.07 — domain cuts, each keeping CANON as the key
    "norse":        [COVER, CANON, FALLOW, ASSAY, MARGIN],
    "contemporary": [COVER, CANON, MANIFEST, WRIT, PROVENANCE, COMMISSION],
}

DEFAULT_OUT = {
    "edition":      "double_folio_volume_01.pdf",
    "spectrum":     "double_folio_volume_01_spectrum.pdf",
    "norse":        "double_folio_norse.pdf",
    "contemporary": "double_folio_contemporary.pdf",
}

WIDTH_PX = 1440  # 15in at 96dpi — the locked native spread width
PAD = 6          # px added to page height to absorb sub-pixel print reflow


def render_one(page, src_path: Path, out_pdf: Path) -> int:
    """Render one spread to a single native-size PDF page. Returns height in px."""
    page.set_viewport_size({"width": WIDTH_PX, "height": 1024})
    page.emulate_media(media="print")
    page.goto(src_path.as_uri(), wait_until="networkidle")
    # Fonts load from the Google Fonts CDN; wait so text metrics are final.
    page.evaluate("document.fonts.ready")
    # Two print-time traps to defuse BEFORE measuring:
    #  1. UA body margin — offsets the spread and can overflow the page.
    #  2. `min-height:100vh` on body — harmless on screen, but at PDF time
    #     1vh = the (tall) page height, so the body re-inflates to a full
    #     page and spills onto a phantom second one. Zero it out so the
    #     measured height is the spread's true natural height.
    page.add_style_tag(content=(
        "html,body{margin:0!important;padding:0!important;min-height:0!important}"
        ".spread,.cover{min-height:0!important}"
    ))
    # Measure true content height under print media at native width.
    # Folios wrap in .spread, the cover in .cover; fall back to body.
    height = page.evaluate(
        "(() => {"
        "  const el = document.querySelector('.spread, .cover') || document.body;"
        "  return Math.ceil(Math.max("
        "    document.body.scrollHeight,"
        "    document.documentElement.scrollHeight,"
        "    el.getBoundingClientRect().height));"
        "})()"
    )
    # Drive the page box via CSS @page (prefer_css_page_size=True). The
    # width/height params of page.pdf() are unreliable when content sits
    # near the page boundary — Chrome paginates the spread across two
    # pages even when it fits — whereas an injected @page rule sets the
    # box the layout engine actually uses and yields one clean page. This
    # also overrides the folios' own `@page 17in 11in landscape`. PAD adds
    # a hair of slack (~0.06in white at the foot) so nothing tips over.
    page.add_style_tag(
        content=f"@page{{size:{WIDTH_PX}px {height + PAD}px;margin:0}}"
    )
    page.pdf(
        path=str(out_pdf),
        print_background=True,
        prefer_css_page_size=True,
    )
    return height


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser(description="Bind Fé spreads into one PDF.")
    ap.add_argument("--order", choices=sorted(ORDERS), default="edition",
                    help="binding cut / sequence (default: edition)")
    ap.add_argument("--out", default=None, help="output PDF path (default per order)")
    args = ap.parse_args()

    order = args.order
    out_name = args.out or DEFAULT_OUT[order]
    sources = [HERE / s for s in ORDERS[order]]
    missing = [s for s in sources if not s.exists()]
    if missing:
        print("MISSING sources:", *[f"  {m.name}" for m in missing], sep="\n")
        sys.exit(1)

    print(f"order: {order}  ({len(sources)} spreads) -> {out_name}")
    writer = PdfWriter()
    ok = True
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        with tempfile.TemporaryDirectory() as td:
            for i, src in enumerate(sources):
                tmp = Path(td) / f"{i:02d}.pdf"
                h = render_one(page, src, tmp)
                reader = PdfReader(str(tmp))
                n = len(reader.pages)
                flag = ""
                if n != 1:
                    flag = f"  <-- WARNING: {n} pages (expected 1)"
                    ok = False
                print(f"  {src.name:32s} {WIDTH_PX}x{h}px  {n}p{flag}")
                for pg in reader.pages:
                    writer.add_page(pg)
        browser.close()

    writer.add_metadata({
        "/Title": "Fé — Volume 01",
        "/Author": "Ven Augustave",
        "/Subject": "A bound volume of eight folios: doctrine recto, codex verso, one mark per folio.",
        "/Creator": "DEVGRU.COMPUTER / DEFENSE.OBSERVER",
        "/Producer": "Fé binding pipeline",
    })

    out = HERE / out_name
    with open(out, "wb") as fh:
        writer.write(fh)
    print(f"\nWrote {out.name}  ({len(writer.pages)} pages)")
    if not ok:
        print("One or more spreads paginated — inspect before shipping.")
        sys.exit(2)


if __name__ == "__main__":
    main()
