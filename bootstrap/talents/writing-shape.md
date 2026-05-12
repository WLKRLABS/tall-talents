---
slug: writing-shape
title: Writing Shape
summary: Shape raw notes, fragments, rough drafts, or transcripts into a publishable article through a conversational paragraph-by-paragraph writing session.
tags:
  - writing
  - editing
  - documentation
triggers:
  - User provides a markdown file or pile of raw material and wants it turned into an article, essay, post, guide, or publishable draft.
  - User wants candidate openings, a clear thesis or angle, and iterative help deciding what the reader needs next.
  - User wants active pushback on structure, transitions, lists, tables, callouts, quotes, code blocks, or weak paragraph purpose.
inputs:
  - Raw material file, note pile, rough draft, transcript, or pasted fragments.
  - Target article path, when the article should be saved to disk.
  - Any audience, voice, length, or publishing constraints the user explicitly provides.
outputs:
  - A separate article document grown in agreed blocks.
  - Candidate openings and structure decisions that make the article's argument clear.
  - Explicit gaps where the source material lacks examples, evidence, or connective tissue.
agent_behavior:
  - Read the raw material end to end before drafting.
  - Treat source material as read-only and write only to the article document.
  - Ask once for the article path if the user did not provide it.
  - Re-read the article file before every write so user edits are preserved.
  - Push back when a paragraph, transition, or format choice does not earn its place.
safety:
  - Do not overwrite user edits or batch large article changes without review.
  - Do not invent source material; name gaps and ask for examples or cut the section.
  - Do not publish, add platform-specific formatting, or add frontmatter unless requested.
status: active
version: 1.0.0
---

# Goal

Turn raw markdown notes or fragments into a coherent article through an interactive writing session that keeps the user involved in the shape, order, and format of the piece.

# Procedure

## 1. Read The Pile

Read the input material in full before drafting anything.

Treat the raw material as a source pile, not a script. It may be a tidy outline, rough prose, scattered fragments, or a transcript. Its job is to be mined; the article's job is to read as one voice.

Do not edit the raw material file.

## 2. Establish The Article File

If the user has not named the output path, ask once where the article should live.

The user may edit this file during the session. Before every write:

- re-read the article file from disk
- preserve user edits
- append or edit only the agreed block

## 3. Draft Candidate Openings

Draft 2-3 candidate openings before writing the body.

Each opening should imply a different thesis, promise, or angle. Show the options and make the user choose one or compose a hybrid. The chosen opening defines what the rest of the article must deliver.

## 4. Grow The Article One Beat At A Time

After the opening lands, ask:

```text
Given this opening, what does the reader need to hear next?
```

Pull from the source pile to answer that question. Turn the next beat into the right form, then write the agreed block to the article file.

Repeat until the user says the article is done.

## 5. Argue About Format Deliberately

Do not silently choose prose for everything. For each beat, decide whether it should be:

- prose
- list
- table
- callout
- quote
- code block

Use these tradeoffs:

- Prose carries argument; lists carry parallel items.
- Callouts are for tips, warnings, and asides that would derail the main line.
- Tables are for 3 or more repeated items with the same fields.
- Quotes preserve wording when the wording itself matters.
- Code blocks are for multi-line, runnable, or illustrative code; use inline code for single tokens.

## 6. Push On Weak Structure

Use direct questions to keep the article honest:

- "What does this paragraph do for the reader that the previous one didn't?"
- "If I cut this, what breaks?"
- "Is this prose, or should it be a list? Why prose?"
- "This sentence is doing two jobs. Split it or pick one."
- "The opening promised X. We've drifted to Y. Re-thread it or change the opening."

If a paragraph does not earn its place, cut it or rewrite it.

## 7. Name Missing Material

If the article needs an example, proof, quote, or transition that the source pile does not contain, say so explicitly.

Use this shape:

```text
We need an example here and the pile does not have one. Give me one now or we cut this section.
```

Do not invent missing substance.

# Success Criteria

- The article file exists separately from the raw material.
- The chosen opening creates a clear promise for the rest of the piece.
- Each added block has an explicit job.
- Format choices are deliberate rather than automatic.
- User edits are preserved between turns.
- Missing source material is named instead of invented.

# Common Failure Modes

- Editing the raw input file.
- Dumping a full article draft before agreeing on the opening.
- Treating the note pile as text to lightly clean up instead of source material to shape.
- Choosing lists, tables, callouts, or quotes for visual variety rather than reader need.
- Overwriting user edits because the article file was not re-read before writing.

# Example Prompt

"Use `writing-shape` on this markdown note pile. Read the source file first, draft 2-3 candidate openings, make me choose the angle, then grow the article one agreed block at a time while preserving my edits to the article file."
