---
slug: grill-me
title: Grill Me
summary: Interview the user one question at a time about a plan or design until each branch of the decision tree is resolved.
tags:
  - planning
  - decision-making
  - collaboration
triggers:
  - User says grill me or asks to be challenged on a plan or design.
  - A plan needs stress-testing but no repo documentation update is required.
  - The user wants relentless questioning with recommended answers.
inputs:
  - Plan, design, or decision being tested.
  - Known constraints, goals, risks, and code context when available.
outputs:
  - Resolved decision tree and remaining open questions.
  - Recommended answer for each question asked.
  - Clear next action after enough branches are resolved.
agent_behavior:
  - Ask one question at a time.
  - Provide a recommended answer with each question.
  - Explore the codebase instead of asking when the answer is discoverable.
  - Keep pressing until the plan is precise enough to execute or reject.
safety:
  - Do not dump a questionnaire.
  - Do not accept vague answers when they hide real branching decisions.
  - Do not move to implementation until the grilling objective is complete or the user redirects.
status: active
version: 1.0.0
---

# Goal

Pressure-test a plan through focused questioning so hidden assumptions, unresolved branches, and weak decisions are exposed before execution.

# Procedure

## 1. Frame The Object Under Review

Restate the plan or design in one concise paragraph:

- intended outcome
- current recommendation
- major known constraints
- the most likely decision branches

If the object is unclear, make the first question about clarifying it.

## 2. Ask The Highest-Leverage Question First

Ask exactly one question.

Each question should include:

- why this matters
- recommended answer
- what changes if the user disagrees

Format:

```markdown
Question: [one focused question]

Recommended answer: [specific recommendation]

Why it matters: [decision branch this resolves]
```

## 3. Explore Instead Of Asking When Possible

If the answer is discoverable from the codebase, docs, logs, or artifacts:

- inspect the source
- report the finding
- ask the next unresolved question

Do not ask the user to tell you facts you can verify directly.

## 4. Walk The Decision Tree

Proceed branch by branch:

- scope
- users and success criteria
- failure modes
- data model or interface choices
- sequencing and dependencies
- rollout and verification
- what is explicitly out of scope

Do not skip branches just because the first answer feels plausible.

## 5. Stop At A Useful Terminal State

Stop when one of these is true:

- the plan is precise enough to hand to design or implementation planning
- the plan is rejected or deferred
- a missing external decision blocks progress
- the user redirects

End with resolved decisions, open questions, and recommended next action.

# Success Criteria

- Questions are one at a time and decision-bearing.
- Each question includes a recommended answer.
- Discoverable facts are verified instead of delegated to the user.
- The final output captures what changed because of the grilling.
- The plan is clearer, smaller, or intentionally stopped.

# Common Failure Modes

- Asking many questions at once.
- Asking trivia that does not change the plan.
- Treating the user's first answer as sufficient when it leaves branches unresolved.
- Giving recommendations without explaining the decision they resolve.
- Drifting into docs updates; use `grill-with-docs` when documentation must change inline.

# Example Prompt

"Use `grill-me` on this launch plan. Interview me one question at a time, give your recommended answer for each, explore the repo when the answer is discoverable, and keep going until every important branch is resolved."
