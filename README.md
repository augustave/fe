# Fé

**A bound-folio design system for legibility under contested conditions.**

Each folio pairs an argument with a worked artifact: doctrine on the recto, codex on the verso, bound by a single mark color used exclusively at the one operational moment where the argument and the artifact agree. The form is the enforcement surface — a reader holding any single folio can verify, in one glance, that the codex obeys the doctrine.

Volume 01 is eight folios: a self-documenting foundation, a Norse philosophical trio, and a contemporary defense quartet. Together they argue a single thesis — that legibility, the ability to hold an accurate read of a situation while the situation actively works to destroy that read, is the load-bearing concept under defense systems, brand systems, and any complex-systems discipline operating under pressure.

---

## The thesis

The doctrine pages name a legibility problem in some domain; the codex pages render the answer. This is the through-line across all eight folios.

Legibility is not transparency and not documentation. It is the property of an artifact that lets you read what it is doing while it is doing it, under conditions designed to prevent exactly that. A logging system documents after the fact. A legible system shows in the moment, in the artifact itself, inspectable in flight. The distinction matters most where it is hardest to maintain — degraded communications, contested authority, adversarial conditions, machine-tempo action faster than human review.

The system takes the position that this is an old problem wearing new clothes. Sovereignty has always operated through named, attested, legible artifacts — the writ, the deed, the commission, the seal. What modernity stripped from contemporary systems is not the underlying logic but the operational legibility. The folios argue that the older shape is the structural answer.

---

## The form

Every folio obeys a fixed architecture. The discipline is not decorative — it makes the argument-to-artifact bind auditable.

- **Doctrine recto, codex verso.** The argument lives on the left page; the worked artifact lives on the right. The masthead spans both; the slug spans both; a structural spine separates them.
- **One mark per folio.** A single color from the Mark Color Index, used exclusively at the operational moment the doctrine and codex share. Decorative use is forbidden.
- **Three palette strata.** Each folio's palette is organized into three named strata (3–4 colors each, 9–11 total including the mark), named for the folio's content register.
- **Locked foundation.** System core colors, paper spectrum, and typography are immutable across the series. Variation happens in the per-folio strata and the mark, where variation carries meaning.
- **Auditable accessibility.** Every body-text color meets WCAG 2.1 AA against its paper. The audit runs before render.

---

## The catalogue

Volume 01 · eight editions.

### Foundation

**№00 · CANON × FORM** — The system documents itself. The codex is the form: type specimen, palette strata, the seven-slot Mark Color Index, the iron rules, the folio index. The doctrine argues that the form is the enforcement surface. The only folio with no single mark — it catalogues all of them.

### Norse philosophical trio

The runes of the Old Norwegian rune poem, read as structural predictions rather than mysticism.

**№01 · FALLOW × FÉ** — Fé (wealth) read as the engine of kin-strife: wealth produces the conditions for conflict. The codex draws latent threat below a visible surface, with a single contact point in Slow Red where the latency becomes visible.

**№02 · ASSAY × ÚR** — Úr (slag) read as the discipline upstream of engagement: substance must be verified before it is used. The codex is an assayer's bench of samples, the failures struck through in Slag Mark.

**№03 · MARGIN × ÞURS** — Þurs (the unmeasurable giant) read as strategic estimation under capability overhang. The codex draws a landscape with a named horizon in Margin Gold — the limit of assertion, beyond which we are guessing.

### Contemporary defense quartet

A sovereignty-and-accountability map for autonomous systems. The four folios bracket a single bound action in action, authority, origin, and identity.

**№04 · MANIFEST × INTENT** — The operator–fleet seam under degraded communications. Argues an autonomous-fleet orchestrator's competitive surface is the seam, not the parser. The codex is a six-track timeline with commit marks in Bind Blue.

**№05 · WRIT × OATH** — Sovereignty as operational legibility. Argues authority must be legible in the artifact that acts, not asserted by separate paperwork. The codex is a formal writ with a named attestation chain in Crown Indigo — the first codex that is a document rather than a visualization.

**№06 · PROVENANCE × MEMORY** — Lineage as auditable inheritance. Argues the system must carry the record of what produced it — training corpus, weight lineage, custody transitions. The codex is a six-generation inheritance chain, each custodian named and hashed, in Compact Green.

**№07 · COMMISSION × NAME** — Named-instance accountability. Argues autonomous instances must be named, not numbered — a serial is a count, a name is an actor. The codex is a commission document with a central heraldic blazon in Sigil Mauve, binding the named instance to its writ (№05) and its provenance (№06).

The quartet completes a chain: MANIFEST binds the action, WRIT names who authorized it, PROVENANCE names what produced the actor, COMMISSION names the actor itself. A system whose action, authority, origin, and identity are all legible in the artifact.

---

## How to read it

- **Single folio:** open any `*_spread.html` in a browser. Each renders as one wide spread, designed at 1440px width. Read the doctrine (left), then the codex (right); verify the codex obeys the doctrine.
- **The whole catalogue:** the bound PDF (`double_folio_volume_01.pdf`) sequences the folios with a cover and editor's note — 10 pages, cover + №00 through №07 + a closing colophon.
- **The system itself:** `double_folio_stage_a_spec.md` documents the locked foundation. Folio №00 (CANON) documents the system in its own form.

---

## Project structure

```
Folios (open in browser)
  canon_form_spread.html          №00 · foundation, self-documenting
  fallow_fe_spread.html           №01 · Norse I
  assay_ur_spread.html            №02 · Norse II
  margin_thurs_spread.html        №03 · Norse III
  manifest_intent_spread.html     №04 · contemporary I
  writ_oath_spread.html           №05 · contemporary II
  provenance_memory_spread.html   №06 · contemporary III
  commission_name_spread.html     №07 · contemporary IV

Bound volume
  cover.html                      Cover / editor's note
  colophon.html                   Closing colophon · Vol 01 complete
  double_folio_volume_01.pdf      Bound catalogue · 10 pages (cover + №00–№07 + colophon)
  bind.py                         Binding pipeline · Playwright → pypdf · --order cuts

System reference
  double_folio_stage_a_spec.md    Locked foundation: core, papers, WCAG, remediation
  DOUBLE_FOLIO_handoff.md         Current state, pending work, resume protocol

System governance
  AUDIT_001_slot_06_resolution.md           First AUDIT — slot-conflict resolution
  audit_001_archived_register_hold.html     Archived folio proposal (not in catalogue)

Installable skill
  double-folio-skill-v1.1.zip     SKILL.md + references + templates + examples + tools
```

---

## The installable skill

The system is packaged as a Claude skill. Once installed, `"build a Fé on [topic]"` becomes a one-prompt invocation. The package contains the canonical SKILL.md, reference files (foundation values, the Mark Color Index discipline, the iron rules, template anatomy, worked examples), blank HTML scaffolds, the six original folios as worked examples, and the binding pipeline.

The skill carries its own scar tissue: v1.1 added a mandatory survey-first workflow step after a cold-start build duplicated an occupied mark slot. The changelog documents why the rule exists. See `AUDIT_001` for the worked instance.

---

## Project status

The Mark Color Index is at declared capacity — seven slots, all claimed, zero reserved. The system has a closed shape: one foundation, three Norse, four contemporary — and is now formally declared **complete**, a closing colophon (`colophon.html`) making the seven-mark index intentionally finished rather than merely full. CANON is current. The bound PDF and the cover's editor's note have been regenerated to the full eight-folio series (PDF: 10 pages, cover + №00–№07 + colophon). The installable skill package still predates №06 and №07.

For the full state, pending work, and resume protocol, see `DOUBLE_FOLIO_handoff.md`.

---

## Imprint

DEVGRU.COMPUTER / DEFENSE.OBSERVER · Ven Augustave · New York · 2026.

Typography: EB Garamond, JetBrains Mono, and Fraunces (all SIL OFL). The folios are zero-dependency HTML — no build step, no framework, no external assets beyond the Google Fonts CDN. Open any folio in a browser to read it.
