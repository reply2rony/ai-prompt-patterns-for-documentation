# AI Prompt Patterns for Documentation — Starter Template

A starter learning template: a small library of reusable AI prompt patterns
for writing IT documentation — SOPs, runbooks, knowledge-base articles, and
release notes. Each pattern is a fill-in-the-blank prompt with a purpose, a
worked sample, and notes on what to check before the draft goes live. Sample
content only — no real company data, no invented metrics, and no claim that
these prompts replace a human review.

## What it is

- `docs/prompt-patterns-guide.md` — the pattern catalogue and how to use it:
  pick a pattern, fill the placeholders, review the output.
- `prompt-patterns-template.csv` — the pattern library in CSV form, so you
  can copy it, filter it, and add your own patterns.
- `scripts/pattern-search.py` — a starter Python script that searches the
  CSV by category or keyword and prints the matching patterns. Labelled a
  starter learning template; it is not a production tool.

## How to use

1. Pick a documentation job (for example: "write an SOP for a password
   reset") and find the matching pattern in `docs/prompt-patterns-guide.md`
   or in the CSV.
2. Replace the `[placeholders]` with your own details — system names, steps,
   audience — and paste the prompt into your AI tool.
3. Check the output against the "check before publishing" notes in the
   guide: accuracy, missing steps, and anything the AI invented.
4. Search the library from the command line:

```bash
python3 scripts/pattern-search.py prompt-patterns-template.csv sop
python3 scripts/pattern-search.py prompt-patterns-template.csv --category runbook
```

## Pattern categories (starter guide)

| Category | Use it for | Example pattern |
|----------|------------|-----------------|
| sop | Step-by-step procedures | Write an SOP from a task list |
| runbook | Incident / recovery steps | Draft a runbook from an outage log |
| kb-article | End-user help articles | Turn a ticket thread into a KB article |
| release-note | Change summaries | Summarise a change list for users |
| checklist | Verification lists | Build a pre-change checklist |

Categories above are starter suggestions for a learning template, not a
standard for any real organisation.

## Sample / Demo notice

All prompts, systems, and examples in this repo are fictional samples for
learning. The diagram in `docs/diagram.png` is a locally generated
illustration labelled "Sample / Demo" — it is not a screenshot of a real
system, and this template does not claim any production use.

## License

MIT — see `LICENSE`.
