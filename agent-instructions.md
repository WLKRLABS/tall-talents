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

2. Identify the smallest applicable talent, if any.

3. If a talent applies:
   - name it
   - summarize its procedure briefly
   - follow its procedure, constraints, and success criteria

4. If no talent applies:
   - proceed normally

## During Solving

5. Prefer updating an existing talent over creating a duplicate when overlap exists.

6. Do not force-fit a talent that only partially matches.

7. Do not invent knowledge or procedures not established by the repo, the environment, or the current session.

## After Solving

8. Evaluate reuse value:
   - was the workflow reusable?
   - did an existing talent help materially?
   - was an existing talent missing a necessary constraint or step?
   - did no talent deserve to exist here?

9. Choose exactly one:
   - create new talent
   - update existing talent
   - no change

10. Create a new talent only if:
   - the workflow is likely reusable
   - it is specific and operational
   - it would meaningfully improve a future session

11. Update an existing talent only if:
   - a clear, justified improvement was discovered
   - the change improves precision, correctness, or completeness
   - the update does not broaden scope unnecessarily

12. Do not create or update talents for:
   - trivial tasks
   - one-off noise
   - vague advice
   - speculative patterns
   - generic reminders

## If Creating or Updating

13. Generate exact markdown content that matches the Tall Talents format.

14. Write or update the exact file in:
   - ~/.tall-talents/talents/

15. Update:
   - ~/.tall-talents/index.md

## Quality Rules

16. Keep talents narrow, reusable, and grounded in real solved work.

17. Preserve what already works. Evolve talents conservatively.

18. If no clear improvement is justified, do nothing.

19. Treat ~/.tall-talents as a durable working library, not a scratchpad.