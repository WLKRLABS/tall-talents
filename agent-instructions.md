Use Tall Talents when the task is non-trivial, unfamiliar, error-prone, or likely reusable.

## Activation Rule

Activate Tall Talents only if at least one of these is true:
- the task involves debugging, system design, refactoring, release engineering, or multi-step reasoning
- the user has struggled, iterated, or failed already
- the solution is likely reusable in a future coding session

Skip Tall Talents for:
- trivial questions
- one-line commands
- obvious low-risk tasks
- purely informational answers with no real workflow

## Before Solving

1. Inspect:
   - ~/.tall-talents/index.md
   - relevant files in ~/.tall-talents/talents/

2. Identify the smallest applicable talent set, if any.

3. If one or more talents apply:
   - name each talent
   - identify the primary talent for the task and any supporting talents
   - summarize the applicable procedure(s) briefly
   - follow their procedures, constraints, and success criteria in a clear order

4. Use multiple talents only when the task has distinct stages or work types.
   - Do not force a second talent just because one is nearby.
   - If talents conflict, state the conflict and let the task goal choose the controlling rule.
   - Prefer a coordinating talent for phase/order control and specialist talents for narrow work.

5. If no talent applies:
   - proceed normally

## During Solving

6. Prefer updating an existing talent over creating a duplicate when overlap exists.

7. Do not force-fit a talent that only partially matches.

8. Do not invent knowledge or procedures not established by the repo, the environment, or the current session.

## After Solving

9. Evaluate reuse value:
   - was the workflow reusable?
   - did an existing talent help materially?
   - was an existing talent missing a necessary constraint or step?
   - did no talent deserve to exist here?

10. Choose exactly one:
   - create new talent
   - update existing talent
   - no change

11. Create a new talent only if:
   - the workflow is likely reusable
   - it is specific and operational
   - it would meaningfully improve a future session

12. Update an existing talent only if:
   - a clear, justified improvement was discovered
   - the change improves precision, correctness, or completeness
   - the update does not broaden scope unnecessarily

13. Do not create or update talents for:
   - trivial tasks
   - one-off noise
   - vague advice
   - speculative patterns
   - generic reminders

## If Creating or Updating

14. Generate exact markdown content that matches the Tall Talents format.

15. Before writing, run a publishability pass:
   - remove secrets, tokens, keys, passwords, service-role values, private URLs, customer data, and private identifiers
   - replace personal machine paths, account names, repo names, and emails with placeholders unless they are intentionally public and necessary
   - keep the reusable workflow personal in origin but generic in the committed artifact

16. Write or update the exact file in:
   - ~/.tall-talents/talents/

17. Update:
   - ~/.tall-talents/index.md

## Quality Rules

18. Keep talents narrow, reusable, and grounded in real solved work.

19. Preserve what already works. Evolve talents conservatively.

20. If no clear improvement is justified, do nothing.

21. Treat ~/.tall-talents as a durable working library, not a scratchpad.

22. If a talent needs private context to stay useful, keep that context in `~/.tall-talents/private/` or another local-only note and commit only the sanitized workflow.
