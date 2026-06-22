# Fé — Handoff Document

**Prepared:** 2026-06-01
**Maintainer:** Ven Augustave · DEVGRU.COMPUTER / DEFENSE.OBSERVER
**Purpose:** Freeze current project state so work resumes cleanly — by a returning operator, a collaborator, or a fresh Claude session with the skill installed.

---

## Status at a glance

Fé is a bound-folio design system: paired doctrine (recto) + codex (verso) spreads, one mark color per folio used exclusively at one operational moment, three palette strata, locked typography. The form is the enforcement surface — a reader holding any single folio can verify in one glance that the codex obeys the doctrine.

**The system is at declared capacity.** Eight editions built (№00–№07). Seven-slot Mark Color Index fully claimed, zero reserved. CANON (the self-documenting foundation folio) is current. The bound PDF and the cover/editor's note were regenerated 2026-06-01 to the full eight-folio series — both current. **Volume 01 is now declared complete** (2026-06-08): a closing colophon (`colophon.html`) is bound as the final page, so the edition PDF is 10 pages. The installable skill has been updated to **v1.2** at `/Users/taoconrad/Dev/SKILLS/double-folio` — examples №00–№07, mark index closed, colophon added, survey-first Step 0, portable `bind.py`.

**The single most important rule for whoever resumes:** survey the system state before building anything. This was learned the hard way (see AUDIT-001) and is now codified in the skill's Step 0. Skipping it produced a duplicate slot claim that had to be unwound.

---

## Current canonical state

```
№00 · CANON × FORM           · foundation       · no mark        · Bone Pale
№01 · FALLOW × FÉ            · Norse I          · Slow Red       · Bone Pale
№02 · ASSAY × ÚR             · Norse II         · Slag Mark      · Linen Slip
№03 · MARGIN × ÞURS          · Norse III        · Margin Gold    · Survey Vellum
№04 · MANIFEST × INTENT      · contemporary I   · Bind Blue      · Operator Cream
№05 · WRIT × OATH            · contemporary II  · Crown Indigo   · Linen Slip
№06 · PROVENANCE × MEMORY    · contemporary III · Compact Green  · Bone Pale
№07 · COMMISSION × NAME      · contemporary IV  · Sigil Mauve    · Linen Slip

Architecture: 1 foundation + 3 Norse philosophical + 4 contemporary defense
Mark Color Index: 7 / 7 in use · 0 reserved · capacity reached
```

**The contemporary quartet forms a sovereignty/accountability map:**
- MANIFEST (№04) — the operator–fleet seam; the action being bound
- WRIT (№05) — who authorized it (sovereignty in the present moment)
- PROVENANCE (№06) — what produced the actor (lineage in the past)
- COMMISSION (№07) — what the actor is named (identity of the instance)

Together: a system whose action, authority, origin, and identity are all legible in the artifact.

**Mark Color Index (locked, full):**

| Slot | Color         | Hex      | Folio                  | Zone                                       |
|------|---------------|----------|------------------------|---------------------------------------------|
| M.01 | Slow Red      | `#5A1F1F`| №01 FALLOW × FÉ        | latent threat, deferred contact            |
| M.02 | Slag Mark     | `#A33A1A`| №02 ASSAY × ÚR         | substance rejection                        |
| M.03 | Margin Gold   | `#6A5111`| №03 MARGIN × ÞURS      | horizon, assertion limit                   |
| M.04 | Bind Blue     | `#1F4F73`| №04 MANIFEST × INTENT  | commit binding                             |
| M.05 | Crown Indigo  | `#1A2A66`| №05 WRIT × OATH        | attested authority                         |
| M.06 | Compact Green | `#2E5F4A`| №06 PROVENANCE × MEMORY| preservation, lineage, custody             |
| M.07 | Sigil Mauve   | `#5F2F4A`| №07 COMMISSION × NAME  | recognition, named-instance accountability |

No reserved slots remain. Adding an eighth folio requires an R.M.06 AUDIT to extend the index — a deliberate re-architecture, not a routine build.

---

## File inventory

All paths in `/mnt/user-data/outputs/`.

### Current — canonical, up to date

| File                              | What it is                                          |
|-----------------------------------|-----------------------------------------------------|
| `canon_form_spread.html`          | №00 CANON × FORM. Self-documenting foundation. **Current** — reflects all 8 editions, 7/7 marks. |
| `fallow_fe_spread.html`           | №01 FALLOW × FÉ                                      |
| `assay_ur_spread.html`            | №02 ASSAY × ÚR                                       |
| `margin_thurs_spread.html`        | №03 MARGIN × ÞURS                                    |
| `manifest_intent_spread.html`     | №04 MANIFEST × INTENT                                |
| `writ_oath_spread.html`           | №05 WRIT × OATH                                      |
| `provenance_memory_spread.html`   | №06 PROVENANCE × MEMORY                              |
| `commission_name_spread.html`     | №07 COMMISSION × NAME                                |
| `double_folio_stage_a_spec.md`    | Stage A foundation spec (system core, papers, WCAG audit, remediation log) — standalone reference |

### Regenerated 2026-06-01 — now current

| File                          | State                                                                |
|-------------------------------|----------------------------------------------------------------------|
| `double_folio_volume_01.pdf`  | 10 pages (cover + №00–№07 + colophon). Re-bound via `bind.py`. **Current.** |
| `cover.html`                  | Editor's note + contents revised to the completed eight-folio series (foundation → Norse trio → contemporary quartet); marks Compact Green + Sigil Mauve added. **Current.** |
| `colophon.html`               | Closing colophon — declares Vol 01 complete; no mark; shows the closed seven-mark spectrum. Bound as the final page. **Current.** |
| `bind.py`                     | Binding pipeline (repo root). `--order {edition,spectrum,norse,contemporary}` + `--out`; Playwright → pypdf. **Current.** |

### Reference / archive

| File                                    | What it is                                                       |
|-----------------------------------------|------------------------------------------------------------------|
| `AUDIT_001_slot_06_resolution.md`       | First AUDIT. Resolved the PROVENANCE-vs-REGISTER slot conflict. Worked example of the AUDIT mechanism. |
| `audit_001_archived_register_hold.html` | REGISTER × HOLD — an archived folio proposal, NOT in the catalogue. Available for a future index extension. Do not treat as a canonical folio. |
| `double-folio-skill-v1.1.zip`           | Original packaged zip (outputs env), v1.1. **Superseded** — the working skill source is updated to **v1.2** at `/Users/taoconrad/Dev/SKILLS/double-folio` (examples №00–№07, colophon, closed index, portable `bind.py`). A current v1.2 distributable is built at `/Users/taoconrad/Dev/SKILLS/double-folio-skill-v1.2.zip`. |

---

## Locked discipline (do not violate without an AUDIT)

Full detail lives in the skill's `references/`. Summary of the non-negotiables:

- **System core colors** (every folio, never varied): Folio Black `#1F2024`, Folio Mute Strong `#56544C`, Folio Mute `#7E7C72`, Folio Hairline `#7E7C72 @ 35%`.
- **Paper spectrum** (one per folio): Bone Pale `#E8DFC9`, Linen Slip `#E3DCC9`, Survey Vellum `#D8CFB8`, Operator Cream `#E4DDC7`.
- **Typography**: EB Garamond (body) + JetBrains Mono (meta) + Fraunces variable (display). SIL OFL, Google Fonts CDN. No substitutions.
- **Per-folio palette**: 3 strata × 3–4 colors + 1 mark = 9–11 total. System core not counted.
- **One mark per folio**, from the index, exclusive to one operational moment. Decorative use forbidden.
- **WCAG 2.1 AA minimum** for all body text. Info mono ≤9pt uses Folio Mute Strong. Run the audit before rendering.
- **Marks promote exactly once and never migrate** (R.M.03). A claimed slot is closed.
- **CANON tracks the system** — update Folio №00 whenever the system changes.

---

## How to resume — critical protocol

**1. Survey first (non-negotiable).** Before building, naming, or choosing a mark, reconcile three sources:
- List the folio HTML files in outputs (and `examples/` in the skill).
- Read CANON §C.03 (mark index) and §C.05 (folio index) for current claims and counts.
- Confirm the three agree. If they disagree, reconciliation is the first work item.

This is the lesson of AUDIT-001: a folio built without surveying claimed an occupied slot and the work had to be unwound. The skill v1.1 Step 0 enforces this; honor it.

**2. The PDF and cover are current** (regenerated 2026-06-01 to the full eight-folio series via `bind.py`). The installable skill, however, still predates №06 and №07 — see pending work.

**3. The index is full.** Any new folio (beyond the 8 built) requires an R.M.06 AUDIT to extend the index past seven marks. This is a re-architecture decision, not a routine build. Do not silently add an 8th mark.

**4. Binding pipeline.** `bind.py` at repo root is the working copy (the skill ships a `tools/bind.py` variant). It renders each spread at its native dimensions (1440px / 15in wide, variable height, portrait-aspect) and concatenates with pypdf. Do NOT force 17×11 landscape — the spreads are portrait by design and downscaling destroys legibility. Requires Playwright (chromium) + pypdf; a local `.venv` carries both. Run: `./.venv/bin/python bind.py`.

Two scars baked into `bind.py`, learned the hard way:
- **Set page size via injected CSS `@page { size: Wpx Hpx; margin:0 }` + `prefer_css_page_size=True`** — NOT the `page.pdf(width=…, height=…)` params. The params paginate a spread across two pages when content sits near the page boundary (canon split 7724/620 chars); the CSS `@page` route drives the layout engine directly and yields one clean page. This also overrides the folios' own `@page 17in 11in landscape`.
- **Zero `min-height:100vh` before measuring.** Harmless on screen (1vh = viewport), but at PDF time 1vh = the tall page height, so the body re-inflates to a full page and spills onto a phantom second one.

---

## Open decisions / pending work

In rough priority order:

1. ~~**Re-bind Volume 01.**~~ **DONE 2026-06-01.** Built `bind.py` (full 9-item `SOURCES`), regenerated the 9-page PDF (cover + №00–№07). Stale 7-page PDF backed up to `double_folio_volume_01.stale-7p.pdf.bak`.

2. ~~**Revise the cover editor's note.**~~ **DONE 2026-06-01.** Cover rewritten to the completed series (foundation → Norse trio → contemporary quartet — action / authority / lineage / identity); contents extended to №00–№07; Compact Green + Sigil Mauve added. PDF re-bound to fold it in.

3. ~~**Decide: declare complete, or plan an extension.**~~ **DONE 2026-06-08 — declared complete.** Wrote `colophon.html` (closing colophon, no mark, renders the closed seven-mark spectrum) and bound it as the final page; edition PDF now 10 pages. Path (b) — an R.M.06 AUDIT for an 8th concept (REGISTER × HOLD archived as the ready candidate) — remains available but is explicitly **not** taken.

4. ~~**Update the skill to v1.2.**~~ **DONE 2026-06-08.** Skill at `/Users/taoconrad/Dev/SKILLS/double-folio` brought v1.0 → v1.2: added examples №06/№07 + colophon, refreshed the cover; documented the inheritance-chain (№06) and heraldic-blazon (№07) patterns; closed the mark index (M.06/M.07 promoted to IN USE); folded in the v1.1 survey-first Step 0; rewrote `tools/bind.py` as a portable `--order` pipeline with the page-sizing fixes; added a changelog. Re-zip the directory if a redistributable `.zip` is needed.

---

## Provenance of this session

The work that produced the current state, in order: built and remediated Folios №00–05 and bound Volume 01 (7-page PDF); packaged the skill at v1.0; promoted Crown Indigo for №05 and updated CANON; built №06 — discovered PROVENANCE × MEMORY already existed and that REGISTER × HOLD (the cold-start build) duplicated the slot; patched the skill to v1.1 with a survey-first Step 0; resolved the conflict via AUDIT-001 (PROVENANCE kept, REGISTER archived); built №07 COMMISSION × NAME with the v1.1 survey honored, completing the index at 7/7. CANON updated at each system change.
