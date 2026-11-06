# AI Prompt Patterns for Documentation — Guide

A starter catalogue of reusable AI prompt patterns for IT documentation.
This is a learning template — adapt the patterns to your own tools and
organisation. All systems, people, and examples below are fictional.

## How a pattern works

Every pattern has the same shape:

1. **Role** — who the AI should act as (for example: "technical writer").
2. **Task** — what to produce (for example: "an SOP for a password reset").
3. **Context** — the facts the AI needs: system name, audience, steps, limits.
4. **Format** — how the output should look: headings, numbered steps, table.
5. **Check** — what a human must verify before the draft goes live.

Never paste real credentials, real user data, or internal URLs into an AI
prompt. Fill the `[placeholders]` with your own details and strip anything
sensitive first.

## The patterns

### 1. SOP from a task list (category: sop)

**Prompt**

> Act as a technical writer. Write a step-by-step SOP for `[task]` on
> `[system]`, for `[audience]`. Use the steps below, in order, one numbered
> step per action. Add a "Before you start" section listing `[prerequisites]`
> and a "If it fails" section with `[fallback]`.
>
> Steps: `[step 1; step 2; step 3]`

**Check before publishing:** every step runs in the order written; no step
assumes access the reader does not have; the fallback step is real.

### 2. Runbook from an outage log (category: runbook)

**Prompt**

> Act as an IT operations writer. Draft a runbook for `[incident type]` on
> `[system]`. Include: symptoms, first checks, escalation trigger, and
> recovery steps. Base it only on this log excerpt: `[log excerpt]`. Do not
> invent causes that are not in the log.

**Check before publishing:** symptoms match the real incident; escalation
names and contact paths are current; nothing is invented from the log.

### 3. Ticket thread to KB article (category: kb-article)

**Prompt**

> Act as a support writer. Turn this resolved ticket thread into a
> knowledge-base article for `[audience]`. Structure: problem, cause in one
> sentence, fix in numbered steps, "still stuck?" line. Keep it under
> `[word count]` words. Ticket thread: `[thread summary]`

**Check before publishing:** the fix was the one that actually resolved the
ticket; no internal ticket IDs or user names remain.

### 4. Change list to release notes (category: release-note)

**Prompt**

> Act as a release-notes writer. Summarise these changes for `[audience]`
> in plain language: `[change 1; change 2; change 3]`. Group them under
> "New", "Fixed", and "Changed". Leave out anything internal-only.

**Check before publishing:** every item in the notes shipped in this
release; internal-only items are removed, not reworded.

### 5. Pre-change checklist (category: checklist)

**Prompt**

> Act as a change manager. Build a pre-change checklist for `[change]` on
> `[system]`. Include: backup taken, rollback plan, who to notify, and a
> test step after the change. Output as a tick-box list.

**Check before publishing:** the rollback plan is tested, not just written;
notification list includes the on-call person.

## Adding your own pattern

Add a row to `prompt-patterns-template.csv` with: id, category, title,
prompt, sample_context, and check_notes. Keep the prompt generic — no real
system names, no real data.

## Sample / Demo notice

All prompts and examples here are fictional samples for learning, labelled
"Sample / Demo" in the diagram. This template does not claim any production
use.
