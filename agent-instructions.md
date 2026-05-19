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

## External Skill Precedence

When the user explicitly invokes a non-Tall-Talents Codex skill, plugin, or slash-style workflow, treat that invoked skill as the controlling workflow.

Do not auto-activate Tall Talents just because a nearby talent matches the same domain.

Tall Talents may join only when at least one of these is true:
- the user explicitly asks for Tall Talents too
- the invoked skill explicitly asks for a Tall Talents procedure
- the task has a separate stage the invoked skill does not cover
- the task is about creating, updating, validating, or routing Tall Talents itself

If Tall Talents is skipped for this reason, say:
`Controlling skill: <skill>. Tall Talents skipped; no separate talent needed.`

If Tall Talents joins under an external controlling workflow, name the external workflow as controlling and each Tall Talent as supporting.

## Before Solving

1. Inspect:
   - ~/.tall-talents/index.md
   - relevant ~/.tall-talents/talents/<slug>/TALENT.md files

   Load `CHANGELOG.md`, examples, scripts, templates, or helper files only when the selected `TALENT.md` references them, the current task needs them, or self-iteration is modifying that package.

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
   - did a loaded talent add context or procedural bloat with no concrete benefit?

10. Choose exactly one:
   - create new talent
   - update existing talent
   - archive or split an existing talent when the evidence threshold is met
   - no change

11. Create a new talent only if:
   - the workflow is likely reusable
   - it is specific and operational
   - it would meaningfully improve a future session

12. Update an existing talent only if:
   - a clear, justified improvement was discovered
   - the change improves precision, correctness, or completeness
   - the update does not broaden scope unnecessarily

12a. Archive only when:
   - there is a serious safety or privacy problem, or
   - three evidence-backed negative reports across at least two sessions show repeated wrong activation or net bloat

12b. Split only when:
   - one broad talent repeatedly does unrelated jobs and concrete session evidence shows narrower talents would route better

12c. Do not automatically merge talents yet.

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
   - ~/.tall-talents/talents/<slug>/TALENT.md

17. Update:
   - ~/.tall-talents/index.md
   - ~/.tall-talents/talents/<slug>/CHANGELOG.md

18. For every automatic talent change, append a package changelog entry with:
   - Session
   - Change
   - Evidence
   - Effect
   - Oscillation check

19. After every non-trivial conversation, run a self-iteration pass:
   - write a raw local report under ~/.tall-talents/private/self-iteration/
   - write a sanitized report under ~/.tall-talents/reports/self-iteration/ only when safe
   - edit talents only when concrete evidence exists
   - otherwise record the no-change rationale

## Quality Rules

20. Keep talents narrow, reusable, and grounded in real solved work.

21. Preserve what already works. Evolve talents conservatively.

22. If no clear improvement is justified, do nothing.

23. Treat ~/.tall-talents as a durable working library, not a scratchpad.

24. If a talent needs private context to stay useful, keep that context in `~/.tall-talents/private/` or another local-only note and commit only the sanitized workflow.
