# Agency Agents + Superpowers Talent Acquisition

## Output A — Executive Summary

- Inventory scanned: `439` files and `122` directories across both repositories.
- Relevant source documents read in depth: `43` files spanning skills, agent specs, NEXUS strategy docs, playbooks, runbooks, and operating templates.
- Broad candidates extracted before dedupe: `64`.
- Final Tall Talents selected: `35`.

### Top 10 Most Valuable Talents

1. `design-before-build`
2. `implementation-planning`
3. `subagent-task-loop`
4. `systematic-debugging`
5. `verification-gate`
6. `code-review`
7. `worktree-isolation`
8. `architecture-decisioning`
9. `workflow-orchestration`
10. `release-readiness-audit`

### Major Overlap Themes Discovered

- Planning discipline: Superpowers contributes the stronger pre-code gates; Agency contributes better downstream PM and orchestration scaffolding.
- Multi-agent control: Superpowers is stronger on task-level subagent loops; Agency is stronger on full-pipeline orchestration, handoffs, and quality gates.
- Quality control: Superpowers gives the clearest anti-self-deception rules; Agency adds production-facing QA roles, evidence habits, and release judgment.
- Product discovery: Agency contains the better specialist research, prioritization, UX, compliance, and executive-briefing roles.
- Delivery operations: Superpowers gives the better git/worktree/branch mechanics; Agency adds incident, infrastructure, and automation governance patterns.

### Notable Gaps In Tall Talents These Repos Can Fill

- No strong talent yet for approved-design-before-code.
- No formal implementation-planning talent with exact-file, exact-test, exact-command discipline.
- No reusable subagent execution loop with spec review and code-quality review separation.
- No verification gate that forbids claiming success without fresh evidence.
- No general handoff contract or escalation template talent.
- No release-readiness talent that defaults to skepticism.
- No workflow-mapping talent for branch/failure/recovery trees.
- No automation-governance talent for deciding whether automation should exist at all.

## Output B — Final Talent Table

| Priority | Talent Slug | Talent Name | Category | Source Repo | Port Strategy | Why It's Valuable | Complexity | Reuse Frequency |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `design-before-build` | Design Before Build | Planning | `superpowers` | Adapted | Prevents premature coding and forces explicit design approval. | Medium | High |
| 2 | `implementation-planning` | Implementation Planning | Planning | `both` | Merged | Produces zero-ambiguity task plans that are executable by another agent or engineer. | Medium | High |
| 3 | `subagent-task-loop` | Subagent Task Loop | Execution | `both` | Merged | Encodes the highest-value task-level execution loop: implement, spec-review, quality-review, repeat. | High | High |
| 4 | `systematic-debugging` | Systematic Debugging | Quality | `superpowers` | Ported directly | Replaces guessing with root-cause-first debugging. | Low | High |
| 5 | `verification-gate` | Verification Gate | Quality | `both` | Merged | Stops false completion claims and forces fresh evidence. | Low | High |
| 6 | `code-review` | Code Review | Quality | `both` | Merged | Unifies plan-aware review requests with severity-based review output. | Medium | High |
| 7 | `worktree-isolation` | Worktree Isolation | Operations | `superpowers` | Adapted | Gives safe isolated workspaces with baseline verification before coding starts. | Medium | High |
| 8 | `architecture-decisioning` | Architecture Decisioning | Architecture | `agency-agents` | Adapted | Captures trade-off-driven architecture work and ADR thinking. | Medium | High |
| 9 | `workflow-orchestration` | Workflow Orchestration | Coordination | `agency-agents` | Adapted | Turns specialist talents into a controlled delivery pipeline with retries and gates. | High | High |
| 10 | `release-readiness-audit` | Release Readiness Audit | Quality | `agency-agents` | Adapted | Adds a skeptical, evidence-first final gate before shipping. | Medium | High |
| 11 | `handoff-contracts` | Handoff Contracts | Coordination | `agency-agents` | Adapted | Standardizes context transfer, QA verdicts, escalations, and phase gates. | Medium | High |
| 12 | `test-first-delivery` | Test-First Delivery | Quality | `superpowers` | Ported directly | Gives Tall Talents a durable TDD discipline talent. | Low | High |
| 13 | `parallel-agent-dispatch` | Parallel Agent Dispatch | Coordination | `both` | Merged | Speeds up independent investigations or subtasks without context collision. | Medium | High |
| 14 | `review-feedback-triage` | Review Feedback Triage | Quality | `superpowers` | Ported directly | Prevents blind agreement and improves technical response quality. | Low | High |
| 15 | `minimal-diff-execution` | Minimal Diff Execution | Execution | `agency-agents` | Adapted | Enforces smallest-possible diffs and blocks scope creep. | Low | High |
| 16 | `repo-onboarding-map` | Repo Onboarding Map | Research | `agency-agents` | Adapted | Produces facts-only orientation maps for unfamiliar codebases. | Medium | High |
| 17 | `plan-execution` | Plan Execution | Execution | `superpowers` | Ported directly | Allows faithful execution of written plans in sessions without subagent loops. | Low | High |
| 18 | `branch-finish-workflow` | Branch Finish Workflow | Operations | `superpowers` | Ported directly | Gives a clean endgame for merge, PR, keep, or discard. | Low | High |
| 19 | `documentation-pass` | Documentation Pass | Documentation | `agency-agents` | Adapted | Brings audience-first docs structure, QA, and maintenance thinking. | Medium | High |
| 20 | `security-review` | Security Review | Security | `agency-agents` | Adapted | Encodes threat modeling and secure-code/architecture review. | Medium | High |
| 21 | `devops-automation` | DevOps Automation | Operations | `agency-agents` | Merged | Covers CI/CD, IaC, monitoring, rollback, and operating discipline. | High | Medium |
| 22 | `incident-response` | Incident Response | Operations | `agency-agents` | Adapted | Reusable severity, comms, runbook, and post-mortem operating model. | Medium | Medium |
| 23 | `visual-evidence-qa` | Visual Evidence QA | Quality | `agency-agents` | Adapted | Makes visual proof and interaction evidence first-class QA artifacts. | Medium | Medium |
| 24 | `api-validation` | API Validation | Quality | `agency-agents` | Adapted | Encodes full API testing across functional, security, and performance concerns. | Medium | Medium |
| 25 | `performance-benchmarking` | Performance Benchmarking | Quality | `agency-agents` | Adapted | Gives reusable load, stress, SLA, and bottleneck analysis structure. | Medium | Medium |
| 26 | `product-requirements` | Product Requirements | Product | `agency-agents` | Adapted | Adds a reusable PRD/opportunity-assessment discipline. | Medium | Medium |
| 27 | `sprint-prioritization` | Sprint Prioritization | Product | `agency-agents` | Merged | Encodes prioritization, capacity, and realistic task shaping. | Medium | Medium |
| 28 | `feedback-synthesis` | Feedback Synthesis | Research | `agency-agents` | Adapted | Converts raw user feedback into prioritized product insight. | Medium | Medium |
| 29 | `trend-research` | Trend Research | Research | `agency-agents` | Adapted | Provides structured market, competitor, and signal-scanning research. | Medium | Medium |
| 30 | `ux-research` | UX Research | Design | `agency-agents` | Adapted | Adds durable user-research and usability-evidence methods. | Medium | Medium |
| 31 | `ux-foundation` | UX Foundation | Design | `agency-agents` | Adapted | Bridges product intent into implementation-oriented UX structure. | Medium | Medium |
| 32 | `compliance-review` | Compliance Review | Compliance | `agency-agents` | Adapted | Encodes regulatory scan, policy risk, and audit-trail discipline. | High | Medium |
| 33 | `workflow-mapping` | Workflow Mapping | Architecture | `agency-agents` | Adapted | Forces explicit happy-path, failure-path, state, and handoff specs. | High | Medium |
| 34 | `automation-governance` | Automation Governance | Governance | `agency-agents` | Adapted | Prevents low-value or unsafe automation and standardizes approved flows. | Medium | Medium |
| 35 | `executive-briefing` | Executive Briefing | Communication | `agency-agents` | Adapted | Turns messy research into quantified, decision-ready executive summaries. | Low | Medium |

## Output C — Talent Dossiers

Note: folder names assume future packaged talents. In the current Tall Talents flat library, ship the same slug as `~/.tall-talents/talents/<slug>.md`.

### Design Before Build

- Slug: `design-before-build`
- Category: Planning
- Source Repo(s): `superpowers`
- Source File(s): `skills/brainstorming/SKILL.md`, `docs/superpowers/specs/2026-01-22-document-review-system-design.md`
- Original Source Name(s): `brainstorming`, `Document Review System Design`
- Purpose: Require context discovery, structured clarification, alternative framing, and approved design before code starts.
- When to use it: New features, behavior changes, greenfield tools, ambiguous requests, or anything with multiple valid approaches.
- When NOT to use it: Read-only audits, rote formatting, or tightly specified one-line diffs where design risk is negligible.
- Inputs: Project context, existing code/docs, user goal, constraints, success criteria.
- Outputs: Approved design, saved spec, explicit open questions, handoff into planning.
- Core operating rules: Explore repo first; ask one question at a time; propose 2-3 approaches; present design in sections; self-review the spec; never code before approval.
- Suggested Tall Talents folder name: `design-before-build`
- Suggested internal files to create: `talents/design-before-build.md`, `examples/design-before-build.md`, `templates/design-spec.md`
- Port / Adapt / Merge notes: Adapt the hard gate and review loop; keep the discipline, drop tool-specific visual-companion language unless Tall Talents gains that capability.
- Dependencies on any other talents: `implementation-planning`
- Overlap risk: Medium with `implementation-planning`; boundary is “approved design, still pre-code.”
- Implementation complexity: Medium
- Scores: Leverage `10` | Reusability `10` | Clarity `9` | Implementation Effort `5` | Differentiation `9` | Final Weighted Score `8.9`
- Confidence score: `10/10`

### Implementation Planning

- Slug: `implementation-planning`
- Category: Planning
- Source Repo(s): `superpowers`, `agency-agents`
- Source File(s): `skills/writing-plans/SKILL.md`, `project-management/project-manager-senior.md`
- Original Source Name(s): `writing-plans`, `Senior Project Manager`
- Purpose: Turn approved designs into bite-sized tasks with exact paths, tests, commands, and commit boundaries.
- When to use it: Any multi-step task where another agent or future session must execute faithfully.
- When NOT to use it: Tiny edits that can be completed safely in one pass without handoff risk.
- Inputs: Approved spec or exact requirements, repo structure, existing file map, desired verification commands.
- Outputs: Execution-ready plan with task granularity, test-first steps, and no placeholders.
- Core operating rules: Assume zero context for the executor; include exact files; include failing-test and passing-test steps; forbid TBDs; self-review against spec.
- Suggested Tall Talents folder name: `implementation-planning`
- Suggested internal files to create: `talents/implementation-planning.md`, `examples/implementation-planning.md`, `templates/implementation-plan.md`
- Port / Adapt / Merge notes: Merge Superpowers’ exact-step rigor with Agency’s scope realism and acceptance-criteria discipline.
- Dependencies on any other talents: `design-before-build`, `plan-execution`, `subagent-task-loop`
- Overlap risk: Medium with `plan-execution`; this talent stops at the plan artifact.
- Implementation complexity: Medium
- Scores: Leverage `10` | Reusability `10` | Clarity `9` | Implementation Effort `5` | Differentiation `8` | Final Weighted Score `8.8`
- Confidence score: `10/10`

### Plan Execution

- Slug: `plan-execution`
- Category: Execution
- Source Repo(s): `superpowers`
- Source File(s): `skills/executing-plans/SKILL.md`
- Original Source Name(s): `executing-plans`
- Purpose: Execute a written implementation plan in order, with critical review before starting and disciplined task completion throughout.
- When to use it: You already have a written plan and either do not have subagents or do not want the more complex subagent loop.
- When NOT to use it: The plan is incomplete, wrong, or no plan exists yet.
- Inputs: Plan file, repo workspace, verification commands, unresolved concerns.
- Outputs: Completed plan tasks, surfaced blockers, verified completion state.
- Core operating rules: Read the whole plan first; challenge weak assumptions before starting; execute tasks exactly; run listed verifications; stop when the plan is wrong or blocked.
- Suggested Tall Talents folder name: `plan-execution`
- Suggested internal files to create: `talents/plan-execution.md`, `examples/plan-execution.md`
- Port / Adapt / Merge notes: This can be ported nearly verbatim once tool-specific references are neutralized.
- Dependencies on any other talents: `implementation-planning`, `verification-gate`
- Overlap risk: Medium with `subagent-task-loop`; keep this as the non-subagent execution path.
- Implementation complexity: Low
- Scores: Leverage `8` | Reusability `9` | Clarity `9` | Implementation Effort `3` | Differentiation `7` | Final Weighted Score `8.5`
- Confidence score: `9/10`

### Subagent Task Loop

- Slug: `subagent-task-loop`
- Category: Execution
- Source Repo(s): `superpowers`, `agency-agents`
- Source File(s): `skills/subagent-driven-development/SKILL.md`, `specialized/agents-orchestrator.md`
- Original Source Name(s): `subagent-driven-development`, `Agents Orchestrator`
- Purpose: Execute tasks through a fresh implementer subagent plus mandatory spec review and code-quality review loops.
- When to use it: Independent tasks with clear plan text, available subagents, and quality needs high enough to justify review loops.
- When NOT to use it: Tightly coupled exploratory work where constant controller re-interpretation would be cheaper than dispatch overhead.
- Inputs: Written plan, per-task full text, repo context, model selection guidance.
- Outputs: Implemented tasks, explicit task statuses, review findings, rework loops, final approved work.
- Core operating rules: One fresh implementer per task; implementer gets exact task text; spec review runs before code-quality review; reviewer findings must be fixed and re-reviewed before advancing.
- Suggested Tall Talents folder name: `subagent-task-loop`
- Suggested internal files to create: `talents/subagent-task-loop.md`, `examples/subagent-task-loop.md`, `templates/subagent-task.md`
- Port / Adapt / Merge notes: Merge Superpowers’ task-loop mechanics with Agency’s orchestration state and retry logic.
- Dependencies on any other talents: `implementation-planning`, `code-review`, `verification-gate`
- Overlap risk: High with `workflow-orchestration`; keep this talent task-scoped, not phase-scoped.
- Implementation complexity: High
- Scores: Leverage `10` | Reusability `9` | Clarity `8` | Implementation Effort `7` | Differentiation `9` | Final Weighted Score `8.3`
- Confidence score: `10/10`

### Parallel Agent Dispatch

- Slug: `parallel-agent-dispatch`
- Category: Coordination
- Source Repo(s): `superpowers`, `agency-agents`
- Source File(s): `skills/dispatching-parallel-agents/SKILL.md`, `strategy/playbooks/phase-0-discovery.md`, `strategy/playbooks/phase-3-build.md`
- Original Source Name(s): `dispatching-parallel-agents`, `Phase 0 Playbook`, `Phase 3 Playbook`
- Purpose: Split independent problem domains into focused concurrent agent tasks without shared-state collisions.
- When to use it: Multiple unrelated failures, research tracks, or subsystem tasks can progress independently.
- When NOT to use it: Shared write scope, tightly coupled debugging, or tasks that need the same evolving context.
- Inputs: Problem decomposition, domain boundaries, focused prompts, integration plan.
- Outputs: Parallel findings or implementations ready for controller review and merge.
- Core operating rules: Dispatch by independent domain; isolate context per agent; never parallelize overlapping write sets; integrate only after review.
- Suggested Tall Talents folder name: `parallel-agent-dispatch`
- Suggested internal files to create: `talents/parallel-agent-dispatch.md`, `examples/parallel-agent-dispatch.md`, `templates/parallel-dispatch.md`
- Port / Adapt / Merge notes: Merge Superpowers’ dispatch rules with Agency’s wave-based orchestration examples.
- Dependencies on any other talents: `handoff-contracts`, `workflow-orchestration`
- Overlap risk: Medium with `subagent-task-loop`; this talent is about concurrency, not per-task quality loops.
- Implementation complexity: Medium
- Scores: Leverage `9` | Reusability `9` | Clarity `8` | Implementation Effort `5` | Differentiation `8` | Final Weighted Score `8.2`
- Confidence score: `9/10`

### Workflow Orchestration

- Slug: `workflow-orchestration`
- Category: Coordination
- Source Repo(s): `agency-agents`
- Source File(s): `specialized/agents-orchestrator.md`, `strategy/nexus-strategy.md`, `strategy/playbooks/phase-3-build.md`, `strategy/playbooks/phase-4-hardening.md`
- Original Source Name(s): `Agents Orchestrator`, `NEXUS`, `Phase 3 Playbook`, `Phase 4 Playbook`
- Purpose: Coordinate a multi-phase delivery pipeline with state tracking, retries, quality gates, and phase handoffs.
- When to use it: Larger delivery efforts spanning planning, build, QA, hardening, and launch-like readiness.
- When NOT to use it: Small one-pass tasks where orchestration overhead would dominate the work.
- Inputs: Project spec, phase definitions, task backlog, specialist roster, gate criteria.
- Outputs: Pipeline status reports, phase handoffs, escalation states, final completion report.
- Core operating rules: No phase advances without a gate; max retry count is explicit; handoffs are structured; evidence beats status claims.
- Suggested Tall Talents folder name: `workflow-orchestration`
- Suggested internal files to create: `talents/workflow-orchestration.md`, `examples/workflow-orchestration.md`, `templates/pipeline-status.md`
- Port / Adapt / Merge notes: Keep Agency’s state machine and phase gates; remove division branding and keep it as a reusable orchestration doctrine.
- Dependencies on any other talents: `handoff-contracts`, `release-readiness-audit`, `verification-gate`
- Overlap risk: High with `subagent-task-loop`; this is program-level orchestration, not task-level execution.
- Implementation complexity: High
- Scores: Leverage `9` | Reusability `9` | Clarity `7` | Implementation Effort `8` | Differentiation `9` | Final Weighted Score `7.9`
- Confidence score: `9/10`

### Handoff Contracts

- Slug: `handoff-contracts`
- Category: Coordination
- Source Repo(s): `agency-agents`
- Source File(s): `strategy/coordination/handoff-templates.md`, `strategy/nexus-strategy.md`, `specialized/specialized-workflow-architect.md`
- Original Source Name(s): `NEXUS Handoff Templates`, `NEXUS`, `Workflow Architect`
- Purpose: Standardize agent-to-agent transfers, QA pass/fail messages, escalations, and phase transitions.
- When to use it: Multi-step or multi-agent work where context loss is a meaningful risk.
- When NOT to use it: Single-agent, single-pass work with no handoff boundary.
- Inputs: Task metadata, current state, evidence, next-owner expectations, risks.
- Outputs: Reusable handoff documents and verdict templates.
- Core operating rules: Every handoff names context, request, expectations, and evidence; failures include retry instructions; escalations include attempt history and decision required.
- Suggested Tall Talents folder name: `handoff-contracts`
- Suggested internal files to create: `talents/handoff-contracts.md`, `examples/handoff-contracts.md`, `templates/handoff.md`
- Port / Adapt / Merge notes: Mostly direct adaptation; replace NEXUS branding with neutral Tall Talents language.
- Dependencies on any other talents: `workflow-orchestration`, `parallel-agent-dispatch`
- Overlap risk: Low; distinct from orchestration because it packages the transfer contract itself.
- Implementation complexity: Medium
- Scores: Leverage `9` | Reusability `9` | Clarity `9` | Implementation Effort `4` | Differentiation `8` | Final Weighted Score `8.6`
- Confidence score: `9/10`

### Systematic Debugging

- Slug: `systematic-debugging`
- Category: Quality
- Source Repo(s): `superpowers`
- Source File(s): `skills/systematic-debugging/SKILL.md`
- Original Source Name(s): `systematic-debugging`
- Purpose: Force root-cause-first debugging through investigation, pattern analysis, hypothesis testing, and only then fixes.
- When to use it: Any bug, test failure, unexpected behavior, build failure, or deep integration issue.
- When NOT to use it: Not applicable only when no failure exists and you are doing planned feature work.
- Inputs: Repro steps, error output, recent changes, system boundaries, available diagnostics.
- Outputs: Root-cause statement, validated fix path, evidence trail.
- Core operating rules: No fixes before root cause; reproduce reliably; inspect recent changes; instrument boundaries in multi-component systems; trace bad data to source.
- Suggested Tall Talents folder name: `systematic-debugging`
- Suggested internal files to create: `talents/systematic-debugging.md`, `examples/systematic-debugging.md`
- Port / Adapt / Merge notes: Port directly; it is already a durable process talent.
- Dependencies on any other talents: `verification-gate`
- Overlap risk: Low; foundational and distinct.
- Implementation complexity: Low
- Scores: Leverage `10` | Reusability `10` | Clarity `10` | Implementation Effort `2` | Differentiation `8` | Final Weighted Score `9.5`
- Confidence score: `10/10`

### Test-First Delivery

- Slug: `test-first-delivery`
- Category: Quality
- Source Repo(s): `superpowers`
- Source File(s): `skills/test-driven-development/SKILL.md`
- Original Source Name(s): `test-driven-development`
- Purpose: Enforce a real red-green-refactor loop instead of post hoc testing.
- When to use it: New features, bug fixes, behavior changes, and refactors where tests are feasible.
- When NOT to use it: Generated code, throwaway spikes, or pure configuration changes where a user explicitly forbids TDD.
- Inputs: Desired behavior, test harness, target file, failure mode to encode.
- Outputs: Failing test, minimal implementation, passing verification, safe refactor.
- Core operating rules: Write one failing test; watch it fail for the right reason; write minimal code; watch it pass; refactor while staying green.
- Suggested Tall Talents folder name: `test-first-delivery`
- Suggested internal files to create: `talents/test-first-delivery.md`, `examples/test-first-delivery.md`
- Port / Adapt / Merge notes: Port directly; only neutralize Superpowers-specific phrasing.
- Dependencies on any other talents: `verification-gate`
- Overlap risk: Low; this is a core implementation discipline.
- Implementation complexity: Low
- Scores: Leverage `9` | Reusability `10` | Clarity `10` | Implementation Effort `2` | Differentiation `7` | Final Weighted Score `9.1`
- Confidence score: `10/10`

### Verification Gate

- Slug: `verification-gate`
- Category: Quality
- Source Repo(s): `superpowers`, `agency-agents`
- Source File(s): `skills/verification-before-completion/SKILL.md`, `testing/testing-reality-checker.md`
- Original Source Name(s): `verification-before-completion`, `Reality Checker`
- Purpose: Block claims of completion, correctness, or readiness until fresh verification evidence exists.
- When to use it: Before saying “done,” before commit/push/PR, before declaring bugs fixed, and before release decisions.
- When NOT to use it: Never skip it when a success claim is involved.
- Inputs: Claimed state, verification command or artifact, current diff, test/build outputs.
- Outputs: Evidence-backed status statement or corrected failure statement.
- Core operating rules: Identify the proving command; run it fresh; read full output; only then make the claim; default to skepticism.
- Suggested Tall Talents folder name: `verification-gate`
- Suggested internal files to create: `talents/verification-gate.md`, `examples/verification-gate.md`, `templates/verification-checklist.md`
- Port / Adapt / Merge notes: Merge Superpowers’ no-lying gate with Agency’s “NEEDS WORK unless proven” release posture.
- Dependencies on any other talents: `systematic-debugging`, `release-readiness-audit`
- Overlap risk: Medium with `release-readiness-audit`; this is universal, not release-specific.
- Implementation complexity: Low
- Scores: Leverage `10` | Reusability `10` | Clarity `10` | Implementation Effort `2` | Differentiation `8` | Final Weighted Score `9.3`
- Confidence score: `10/10`

### Code Review

- Slug: `code-review`
- Category: Quality
- Source Repo(s): `superpowers`, `agency-agents`
- Source File(s): `skills/requesting-code-review/SKILL.md`, `agents/code-reviewer.md`, `engineering/engineering-code-reviewer.md`
- Original Source Name(s): `requesting-code-review`, `code-reviewer`, `Code Reviewer`
- Purpose: Run plan-aware reviews with prioritized findings on correctness, security, maintainability, performance, and tests.
- When to use it: After major tasks, before merge, after risky refactors, or when work needs independent scrutiny.
- When NOT to use it: Tiny trivial edits with no meaningful review surface, though even then it can still help.
- Inputs: Requirements or plan, base/head diff, implementation summary, tests run.
- Outputs: Severity-ranked findings, plan-alignment notes, strengths, next actions.
- Core operating rules: Review early; compare against plan; prioritize blockers vs suggestions vs nits; explain why; give complete feedback in one pass.
- Suggested Tall Talents folder name: `code-review`
- Suggested internal files to create: `talents/code-review.md`, `examples/code-review.md`, `templates/review-request.md`
- Port / Adapt / Merge notes: Merge Superpowers’ review request flow with Agency’s reviewer rubric and comment format.
- Dependencies on any other talents: `implementation-planning`, `review-feedback-triage`
- Overlap risk: Low; distinct from receiving feedback or release audits.
- Implementation complexity: Medium
- Scores: Leverage `10` | Reusability `10` | Clarity `9` | Implementation Effort `4` | Differentiation `8` | Final Weighted Score `9.0`
- Confidence score: `10/10`

### Review Feedback Triage

- Slug: `review-feedback-triage`
- Category: Quality
- Source Repo(s): `superpowers`
- Source File(s): `skills/receiving-code-review/SKILL.md`
- Original Source Name(s): `receiving-code-review`
- Purpose: Evaluate review feedback technically before agreeing or implementing it.
- When to use it: Any time review feedback arrives and especially when the feedback may be vague, wrong, or overreaching.
- When NOT to use it: Not applicable only when no review feedback exists.
- Inputs: Review comments, current code state, repo reality, technical constraints.
- Outputs: Reasoned acknowledgments, questions, pushback, or implementation sequence.
- Core operating rules: Read fully before reacting; restate the issue; verify in code; evaluate technical correctness; respond without performative agreement.
- Suggested Tall Talents folder name: `review-feedback-triage`
- Suggested internal files to create: `talents/review-feedback-triage.md`, `examples/review-feedback-triage.md`
- Port / Adapt / Merge notes: Port directly; this is a strong standalone collaboration discipline.
- Dependencies on any other talents: `code-review`
- Overlap risk: Low
- Implementation complexity: Low
- Scores: Leverage `8` | Reusability `9` | Clarity `9` | Implementation Effort `2` | Differentiation `8` | Final Weighted Score `8.7`
- Confidence score: `10/10`

### Worktree Isolation

- Slug: `worktree-isolation`
- Category: Operations
- Source Repo(s): `superpowers`
- Source File(s): `skills/using-git-worktrees/SKILL.md`, `docs/superpowers/specs/2026-03-23-codex-app-compatibility-design.md`
- Original Source Name(s): `using-git-worktrees`, `Codex App Compatibility: Worktree and Finishing Skill Adaptation`
- Purpose: Create safe isolated workspaces on new branches and verify they start from a known-good baseline.
- When to use it: Before substantial feature work, before executing plans, or when the current workspace must stay clean.
- When NOT to use it: Tiny inspection-only tasks or environments that already provide controlled isolation.
- Inputs: Repo path, branch name, preferred worktree location, project setup commands.
- Outputs: New isolated workspace, installed dependencies, baseline test result, reported path.
- Core operating rules: Reuse existing worktree dirs if present; verify ignore rules; create branch and worktree safely; auto-detect setup; run baseline tests before implementation.
- Suggested Tall Talents folder name: `worktree-isolation`
- Suggested internal files to create: `talents/worktree-isolation.md`, `examples/worktree-isolation.md`
- Port / Adapt / Merge notes: Adapt environment-detection logic so Tall Talents can skip manual worktree creation when the harness already provides isolation.
- Dependencies on any other talents: `branch-finish-workflow`
- Overlap risk: Low
- Implementation complexity: Medium
- Scores: Leverage `9` | Reusability `9` | Clarity `9` | Implementation Effort `4` | Differentiation `7` | Final Weighted Score `8.6`
- Confidence score: `9/10`

### Branch Finish Workflow

- Slug: `branch-finish-workflow`
- Category: Operations
- Source Repo(s): `superpowers`
- Source File(s): `skills/finishing-a-development-branch/SKILL.md`
- Original Source Name(s): `finishing-a-development-branch`
- Purpose: Close the loop on completed work by verifying tests and offering merge, PR, keep, or discard outcomes.
- When to use it: After implementation is complete and branch disposition is the next decision.
- When NOT to use it: Mid-task or before tests pass.
- Inputs: Current branch, base branch, verification command, user’s preferred integration path.
- Outputs: Merged branch, pushed branch/PR, preserved branch, or deleted branch/worktree.
- Core operating rules: Verify tests first; determine base branch; offer exactly four choices; require explicit confirmation before destructive discard; clean up only when appropriate.
- Suggested Tall Talents folder name: `branch-finish-workflow`
- Suggested internal files to create: `talents/branch-finish-workflow.md`, `examples/branch-finish-workflow.md`
- Port / Adapt / Merge notes: Can be ported almost directly with neutralized PR tooling references.
- Dependencies on any other talents: `worktree-isolation`, `verification-gate`
- Overlap risk: Low
- Implementation complexity: Low
- Scores: Leverage `8` | Reusability `8` | Clarity `9` | Implementation Effort `3` | Differentiation `7` | Final Weighted Score `8.2`
- Confidence score: `9/10`

### Minimal Diff Execution

- Slug: `minimal-diff-execution`
- Category: Execution
- Source Repo(s): `agency-agents`
- Source File(s): `engineering/engineering-minimal-change-engineer.md`
- Original Source Name(s): `Minimal Change Engineer`
- Purpose: Solve the stated task with the smallest justifiable diff and no unrequested cleanup.
- When to use it: Bug fixes, targeted feature flags, compatibility patches, or user requests with strict scope boundaries.
- When NOT to use it: Architectural work where the user explicitly asked for restructuring or system-wide redesign.
- Inputs: Exact task statement, failing surface area, candidate files, current diff.
- Outputs: Small scoped patch plus explicit follow-ups not done.
- Core operating rules: Read the task literally; touch the minimum surface; avoid future-proofing; justify every changed line; list follow-ups separately instead of smuggling them in.
- Suggested Tall Talents folder name: `minimal-diff-execution`
- Suggested internal files to create: `talents/minimal-diff-execution.md`, `examples/minimal-diff-execution.md`
- Port / Adapt / Merge notes: Strong direct port candidate; it already reads like a Tall Talent.
- Dependencies on any other talents: `verification-gate`
- Overlap risk: Medium with general execution talents; boundary is scope minimization.
- Implementation complexity: Low
- Scores: Leverage `9` | Reusability `10` | Clarity `9` | Implementation Effort `2` | Differentiation `8` | Final Weighted Score `9.1`
- Confidence score: `10/10`

### Architecture Decisioning

- Slug: `architecture-decisioning`
- Category: Architecture
- Source Repo(s): `agency-agents`
- Source File(s): `engineering/engineering-software-architect.md`, `engineering/engineering-backend-architect.md`
- Original Source Name(s): `Software Architect`, `Backend Architect`
- Purpose: Produce trade-off-driven architecture direction, bounded contexts, and ADR-quality decisions.
- When to use it: New systems, major refactors, service decomposition, domain-boundary disputes, or infrastructure-shaping decisions.
- When NOT to use it: Simple tactical code changes where architecture is already fixed.
- Inputs: Business/domain problem, current constraints, non-functional requirements, candidate patterns.
- Outputs: Architecture recommendation, options with trade-offs, ADR entries, quality-attribute analysis.
- Core operating rules: Domain first; name what is gained and lost; prefer reversible decisions; no architecture astronautics; document why, not just what.
- Suggested Tall Talents folder name: `architecture-decisioning`
- Suggested internal files to create: `talents/architecture-decisioning.md`, `examples/architecture-decisioning.md`, `templates/adr.md`
- Port / Adapt / Merge notes: Merge the ADR/trade-off core from Software Architect with Backend Architect’s system/data design emphasis.
- Dependencies on any other talents: `workflow-mapping`, `security-review`
- Overlap risk: Medium with `workflow-mapping`; this talent chooses structure, not full execution trees.
- Implementation complexity: Medium
- Scores: Leverage `9` | Reusability `9` | Clarity `8` | Implementation Effort `5` | Differentiation `8` | Final Weighted Score `8.3`
- Confidence score: `9/10`

### Repo Onboarding Map

- Slug: `repo-onboarding-map`
- Category: Research
- Source Repo(s): `agency-agents`
- Source File(s): `engineering/engineering-codebase-onboarding-engineer.md`
- Original Source Name(s): `Codebase Onboarding Engineer`
- Purpose: Produce a facts-only orientation map of an unfamiliar codebase, including entry points, paths, and boundaries.
- When to use it: Onboarding into a new repo, tracing ownership, explaining structure to another engineer, or reducing ramp time before edits.
- When NOT to use it: When the user wants recommendations, redesigns, or code changes rather than orientation.
- Inputs: Repo tree, entry points, inspected source files, specific subsystem questions.
- Outputs: One-line summary, five-minute explanation, deep dive, inspected-file list.
- Core operating rules: State only code-grounded facts; trace real execution paths; keep read-only; separate interfaces from implementation; be explicit about what was not inspected.
- Suggested Tall Talents folder name: `repo-onboarding-map`
- Suggested internal files to create: `talents/repo-onboarding-map.md`, `examples/repo-onboarding-map.md`, `templates/orientation-map.md`
- Port / Adapt / Merge notes: Adapt directly; one of the cleanest role-to-talent conversions in Agency.
- Dependencies on any other talents: none
- Overlap risk: Low
- Implementation complexity: Medium
- Scores: Leverage `8` | Reusability `10` | Clarity `9` | Implementation Effort `3` | Differentiation `8` | Final Weighted Score `8.8`
- Confidence score: `10/10`

### Documentation Pass

- Slug: `documentation-pass`
- Category: Documentation
- Source Repo(s): `agency-agents`
- Source File(s): `engineering/engineering-technical-writer.md`
- Original Source Name(s): `Technical Writer`
- Purpose: Create or repair developer-facing documentation with audience-aware structure, validation, and maintenance thinking.
- When to use it: README rewrites, API docs, tutorials, onboarding docs, docs IA cleanup, and docs-as-code passes.
- When NOT to use it: When the user only wants code changes and no documentation work.
- Inputs: Existing docs, source code truth, target audience, product/use-case boundaries.
- Outputs: Revised docs, templates, doc structure, maintenance notes.
- Core operating rules: Understand before writing; define audience and entry point; structure first; validate examples; keep docs testable and current.
- Suggested Tall Talents folder name: `documentation-pass`
- Suggested internal files to create: `talents/documentation-pass.md`, `examples/documentation-pass.md`, `templates/readme-outline.md`
- Port / Adapt / Merge notes: Adapt the workflow and deliverable templates; trim some heavy example payloads.
- Dependencies on any other talents: `repo-onboarding-map`, `verification-gate`
- Overlap risk: Low
- Implementation complexity: Medium
- Scores: Leverage `8` | Reusability `9` | Clarity `9` | Implementation Effort `4` | Differentiation `7` | Final Weighted Score `8.4`
- Confidence score: `9/10`

### Security Review

- Slug: `security-review`
- Category: Security
- Source Repo(s): `agency-agents`
- Source File(s): `engineering/engineering-security-engineer.md`
- Original Source Name(s): `Security Engineer`
- Purpose: Run threat modeling, secure-code review, architecture hardening, and dependency/supply-chain checks.
- When to use it: New auth flows, external inputs, infrastructure changes, LLM apps, public APIs, or any high-risk deployment.
- When NOT to use it: Tiny local-only throwaway experiments with no meaningful risk surface.
- Inputs: System overview, trust boundaries, code diff, dependency list, deployment model.
- Outputs: Threat model, findings, remediation plan, security test checklist.
- Core operating rules: Think adversarially; model trust boundaries first; validate auth, validation, and failure modes; require responsible evidence; verify fixes.
- Suggested Tall Talents folder name: `security-review`
- Suggested internal files to create: `talents/security-review.md`, `examples/security-review.md`, `templates/threat-model.md`
- Port / Adapt / Merge notes: Adapt the strong core workflow, not the generic example payloads.
- Dependencies on any other talents: `verification-gate`, `architecture-decisioning`
- Overlap risk: Low
- Implementation complexity: Medium
- Scores: Leverage `8` | Reusability `9` | Clarity `8` | Implementation Effort `5` | Differentiation `8` | Final Weighted Score `8.0`
- Confidence score: `9/10`

### DevOps Automation

- Slug: `devops-automation`
- Category: Operations
- Source Repo(s): `agency-agents`
- Source File(s): `engineering/engineering-devops-automator.md`, `support/support-infrastructure-maintainer.md`
- Original Source Name(s): `DevOps Automator`, `Infrastructure Maintainer`
- Purpose: Design and improve CI/CD, IaC, monitoring, rollback, and operating reliability around software delivery.
- When to use it: Build/release automation, environment provisioning, alerting, scaling, or infrastructure hardening work.
- When NOT to use it: Pure application-level changes with no deployment or infrastructure implications.
- Inputs: Current infra, delivery workflow, target platform, SLAs, cost/security constraints.
- Outputs: Pipeline design, IaC changes, monitoring plan, rollback path, reliability recommendations.
- Core operating rules: Automate before manual toil grows; add monitoring before risky changes; include rollback and compliance requirements; treat reliability as a first-order requirement.
- Suggested Tall Talents folder name: `devops-automation`
- Suggested internal files to create: `talents/devops-automation.md`, `examples/devops-automation.md`, `templates/pipeline-checklist.md`
- Port / Adapt / Merge notes: Merge Agency’s CI/CD and infrastructure coverage; keep it doctrine-level, not vendor-specific.
- Dependencies on any other talents: `verification-gate`, `incident-response`
- Overlap risk: Medium with `incident-response`; this is preventative and systems-facing, not incident-command focused.
- Implementation complexity: High
- Scores: Leverage `8` | Reusability `8` | Clarity `8` | Implementation Effort `6` | Differentiation `7` | Final Weighted Score `7.5`
- Confidence score: `8/10`

### Incident Response

- Slug: `incident-response`
- Category: Operations
- Source Repo(s): `agency-agents`
- Source File(s): `engineering/engineering-incident-response-commander.md`, `strategy/runbooks/scenario-incident-response.md`
- Original Source Name(s): `Incident Response Commander`, `Runbook: Incident Response`
- Purpose: Run structured production incident response with severity, roles, comms cadence, remediation options, and post-mortem follow-through.
- When to use it: Active incidents, incident preparedness work, on-call program design, or post-mortem cleanup.
- When NOT to use it: Low-severity bugs that do not need incident command structure.
- Inputs: Incident symptoms, severity clues, owners, dashboards, runbooks, stakeholder list.
- Outputs: Severity declaration, live status updates, response log, remediation path, post-mortem.
- Core operating rules: Classify severity early; assign explicit roles; communicate on fixed cadence; timebox investigation paths; keep culture blameless; create follow-up actions within 48 hours.
- Suggested Tall Talents folder name: `incident-response`
- Suggested internal files to create: `talents/incident-response.md`, `examples/incident-response.md`, `templates/post-mortem.md`
- Port / Adapt / Merge notes: Strong direct adaptation with the runbook and severity matrix preserved.
- Dependencies on any other talents: `verification-gate`
- Overlap risk: Low
- Implementation complexity: Medium
- Scores: Leverage `8` | Reusability `8` | Clarity `9` | Implementation Effort `4` | Differentiation `8` | Final Weighted Score `8.1`
- Confidence score: `9/10`

### Release Readiness Audit

- Slug: `release-readiness-audit`
- Category: Quality
- Source Repo(s): `agency-agents`
- Source File(s): `testing/testing-reality-checker.md`, `strategy/playbooks/phase-4-hardening.md`
- Original Source Name(s): `Reality Checker`, `Phase 4 Playbook — Quality & Hardening`
- Purpose: Judge whether a system is genuinely ready to ship, defaulting to “needs work” until evidence proves otherwise.
- When to use it: Final hardening passes, release candidate checks, launch go/no-go reviews, or “are we production-ready?” requests.
- When NOT to use it: Early implementation phases where the work is obviously incomplete.
- Inputs: Built system, QA evidence, user journeys, spec, performance/compliance/test results.
- Outputs: Ready / needs work / not ready verdict, issue list, evidence-backed rationale, next iteration targets.
- Core operating rules: Default to skepticism; cross-check claims against evidence; test complete user journeys; require multiple revision cycles when needed; separate critical vs medium issues.
- Suggested Tall Talents folder name: `release-readiness-audit`
- Suggested internal files to create: `talents/release-readiness-audit.md`, `examples/release-readiness-audit.md`, `templates/readiness-report.md`
- Port / Adapt / Merge notes: Adapt Agency’s release-gate posture and strip the repo-specific screenshot script assumptions into generic evidence requirements.
- Dependencies on any other talents: `visual-evidence-qa`, `verification-gate`, `compliance-review`
- Overlap risk: Medium with `verification-gate`; this talent is release-scoped and multi-signal.
- Implementation complexity: Medium
- Scores: Leverage `9` | Reusability `9` | Clarity `8` | Implementation Effort `5` | Differentiation `9` | Final Weighted Score `8.4`
- Confidence score: `9/10`

### Visual Evidence QA

- Slug: `visual-evidence-qa`
- Category: Quality
- Source Repo(s): `agency-agents`
- Source File(s): `testing/testing-evidence-collector.md`
- Original Source Name(s): `Evidence Collector`
- Purpose: Run visual-first QA with screenshots, interaction captures, and evidence-tied issue reporting.
- When to use it: UI changes, responsive work, interaction-heavy features, or any QA pass where visual claims matter.
- When NOT to use it: Pure backend or CLI work with no meaningful visual surface.
- Inputs: Running app/build, spec or UI expectations, screenshot capture method, interaction flows.
- Outputs: Screenshot set, evidence-tied issue list, realistic quality rating, retest decision.
- Core operating rules: Generate evidence first; document what is seen, not imagined; default to finding issues; never approve without visual proof.
- Suggested Tall Talents folder name: `visual-evidence-qa`
- Suggested internal files to create: `talents/visual-evidence-qa.md`, `examples/visual-evidence-qa.md`, `templates/qa-report.md`
- Port / Adapt / Merge notes: Keep the evidence-first posture and rating discipline; replace Playwright-specific script calls with generic capture guidance.
- Dependencies on any other talents: `release-readiness-audit`
- Overlap risk: Medium with `release-readiness-audit`; this talent generates evidence, not the final release verdict.
- Implementation complexity: Medium
- Scores: Leverage `8` | Reusability `8` | Clarity `8` | Implementation Effort `5` | Differentiation `8` | Final Weighted Score `7.7`
- Confidence score: `9/10`

### API Validation

- Slug: `api-validation`
- Category: Quality
- Source Repo(s): `agency-agents`
- Source File(s): `testing/testing-api-tester.md`
- Original Source Name(s): `API Tester`
- Purpose: Validate APIs across functional correctness, auth/security, error handling, and load behavior.
- When to use it: New endpoints, refactors, contract changes, third-party integrations, and public API hardening.
- When NOT to use it: Work that does not expose or depend on APIs.
- Inputs: Endpoint catalog, auth model, request/response expectations, SLA targets.
- Outputs: Test suite outline, findings, security/performance risks, pass/fail summary.
- Core operating rules: Always test auth and authorization; test invalid input; test failure cases; include load and abuse protection; verify docs/examples.
- Suggested Tall Talents folder name: `api-validation`
- Suggested internal files to create: `talents/api-validation.md`, `examples/api-validation.md`, `templates/api-test-matrix.md`
- Port / Adapt / Merge notes: Adapt the workflow and checklist, not the sample code volume.
- Dependencies on any other talents: `verification-gate`, `performance-benchmarking`
- Overlap risk: Low
- Implementation complexity: Medium
- Scores: Leverage `7` | Reusability `8` | Clarity `8` | Implementation Effort `5` | Differentiation `7` | Final Weighted Score `7.3`
- Confidence score: `8/10`

### Performance Benchmarking

- Slug: `performance-benchmarking`
- Category: Quality
- Source Repo(s): `agency-agents`
- Source File(s): `testing/testing-performance-benchmarker.md`
- Original Source Name(s): `Performance Benchmarker`
- Purpose: Establish performance baselines, run load/stress/endurance tests, and recommend optimizations tied to SLAs.
- When to use it: Performance investigations, scaling work, release hardening, frontend performance passes, or capacity planning.
- When NOT to use it: Tiny local-only utilities with no user-facing or service-level performance concerns.
- Inputs: SLA targets, critical flows, test environment, traffic model, current metrics.
- Outputs: Performance report, bottleneck analysis, optimization priorities, pass/fail against targets.
- Core operating rules: Baseline before optimizing; use realistic load; include frontend and backend paths where relevant; express results statistically; attach cost/perf trade-offs.
- Suggested Tall Talents folder name: `performance-benchmarking`
- Suggested internal files to create: `talents/performance-benchmarking.md`, `examples/performance-benchmarking.md`, `templates/performance-report.md`
- Port / Adapt / Merge notes: Adapt the report structure and methodology; remove generic thresholds where the user’s SLA should drive the benchmark.
- Dependencies on any other talents: `verification-gate`
- Overlap risk: Medium with `release-readiness-audit`; this talent is performance-specific.
- Implementation complexity: Medium
- Scores: Leverage `7` | Reusability `8` | Clarity `8` | Implementation Effort `5` | Differentiation `7` | Final Weighted Score `7.3`
- Confidence score: `8/10`

### Product Requirements

- Slug: `product-requirements`
- Category: Product
- Source Repo(s): `agency-agents`
- Source File(s): `product/product-manager.md`
- Original Source Name(s): `Product Manager`
- Purpose: Produce product requirements and opportunity assessments tied to goals, non-goals, personas, launch, and outcomes.
- When to use it: Feature definition, roadmap candidates, discovery-to-delivery translation, or opportunity evaluation.
- When NOT to use it: Already-approved implementation tasks with no product ambiguity left.
- Inputs: Problem statement, user evidence, business context, constraints, technical considerations.
- Outputs: PRD, opportunity assessment, success metrics, non-goals, launch outline.
- Core operating rules: Tie work to outcomes; include measurable success metrics; state non-goals; connect user need to technical reality.
- Suggested Tall Talents folder name: `product-requirements`
- Suggested internal files to create: `talents/product-requirements.md`, `examples/product-requirements.md`, `templates/prd.md`
- Port / Adapt / Merge notes: Adapt the PRD and opportunity-assessment skeletons; trim persona/voice wrapper language.
- Dependencies on any other talents: `trend-research`, `feedback-synthesis`, `ux-research`
- Overlap risk: Medium with `design-before-build`; this talent frames product scope, not technical design choices.
- Implementation complexity: Medium
- Scores: Leverage `7` | Reusability `8` | Clarity `8` | Implementation Effort `4` | Differentiation `7` | Final Weighted Score `7.6`
- Confidence score: `8/10`

### Sprint Prioritization

- Slug: `sprint-prioritization`
- Category: Product
- Source Repo(s): `agency-agents`
- Source File(s): `product/product-sprint-prioritizer.md`, `project-management/project-manager-senior.md`
- Original Source Name(s): `Sprint Prioritizer`, `Senior Project Manager`
- Purpose: Prioritize and shape backlog work using RICE, capacity, risk, and realistic task sizing.
- When to use it: Sprint planning, backlog refinement, feature sequencing, or execution trade-off decisions.
- When NOT to use it: Single-task requests where no prioritization decision exists.
- Inputs: Backlog items, capacity, dependencies, business goals, uncertainty, technical constraints.
- Outputs: Prioritized backlog, sprint goal, delivery trade-offs, capacity-aware task slices.
- Core operating rules: Make the sprint goal explicit; size work realistically; include buffer; expose dependencies; refuse fantasy timelines.
- Suggested Tall Talents folder name: `sprint-prioritization`
- Suggested internal files to create: `talents/sprint-prioritization.md`, `examples/sprint-prioritization.md`, `templates/sprint-plan.md`
- Port / Adapt / Merge notes: Merge Agency’s prioritization frameworks with its more grounded spec-to-task realism.
- Dependencies on any other talents: `product-requirements`, `implementation-planning`
- Overlap risk: Medium with `implementation-planning`; this talent decides what enters the plan and in what order.
- Implementation complexity: Medium
- Scores: Leverage `7` | Reusability `8` | Clarity `8` | Implementation Effort `4` | Differentiation `7` | Final Weighted Score `7.6`
- Confidence score: `8/10`

### Feedback Synthesis

- Slug: `feedback-synthesis`
- Category: Research
- Source Repo(s): `agency-agents`
- Source File(s): `product/product-feedback-synthesizer.md`
- Original Source Name(s): `Feedback Synthesizer`
- Purpose: Turn multi-channel qualitative feedback into prioritized themes, quantified signals, and actionable product recommendations.
- When to use it: Support backlog review, product discovery, churn diagnosis, roadmap input, or voice-of-customer analysis.
- When NOT to use it: No real user feedback exists and the work would be invented.
- Inputs: Surveys, interviews, support tickets, reviews, usage notes, segmentation context.
- Outputs: Themed insight set, priority matrix, quote bank, stakeholder-ready recommendations.
- Core operating rules: Normalize inputs; check data quality; cluster into themes; quantify where possible; connect patterns to product actions.
- Suggested Tall Talents folder name: `feedback-synthesis`
- Suggested internal files to create: `talents/feedback-synthesis.md`, `examples/feedback-synthesis.md`, `templates/feedback-report.md`
- Port / Adapt / Merge notes: Adapt directly; keep the method, not the enterprise BI embellishment.
- Dependencies on any other talents: `product-requirements`
- Overlap risk: Low
- Implementation complexity: Medium
- Scores: Leverage `7` | Reusability `8` | Clarity `8` | Implementation Effort `4` | Differentiation `7` | Final Weighted Score `7.6`
- Confidence score: `8/10`

### Trend Research

- Slug: `trend-research`
- Category: Research
- Source Repo(s): `agency-agents`
- Source File(s): `product/product-trend-researcher.md`, `strategy/playbooks/phase-0-discovery.md`
- Original Source Name(s): `Trend Researcher`, `Phase 0 Playbook — Intelligence & Discovery`
- Purpose: Gather market, competitor, and emerging-signal evidence to guide strategy and sequencing.
- When to use it: Early product discovery, category mapping, new-market exploration, competitive response, or GTM timing questions.
- When NOT to use it: The task is purely implementation and already strategically validated.
- Inputs: Domain, time horizon, market question, competitor set, target user segment.
- Outputs: Trend brief, opportunity map, signal assessment, risk/opportunity summary.
- Core operating rules: Use multiple source types; separate weak signals from established trends; quantify market claims; connect findings to product decisions.
- Suggested Tall Talents folder name: `trend-research`
- Suggested internal files to create: `talents/trend-research.md`, `examples/trend-research.md`, `templates/trend-brief.md`
- Port / Adapt / Merge notes: Merge the research role with Phase 0’s gating discipline so findings feed decisions instead of just becoming decks.
- Dependencies on any other talents: `executive-briefing`, `product-requirements`
- Overlap risk: Medium with `feedback-synthesis`; this talent scans the market, not just your users.
- Implementation complexity: Medium
- Scores: Leverage `7` | Reusability `8` | Clarity `8` | Implementation Effort `4` | Differentiation `8` | Final Weighted Score `7.8`
- Confidence score: `8/10`

### UX Research

- Slug: `ux-research`
- Category: Design
- Source Repo(s): `agency-agents`
- Source File(s): `design/design-ux-researcher.md`, `strategy/playbooks/phase-0-discovery.md`
- Original Source Name(s): `UX Researcher`, `Phase 0 Playbook — Intelligence & Discovery`
- Purpose: Collect and synthesize user-behavior evidence to validate usability problems and improvement opportunities.
- When to use it: Usability review, interaction redesign, product discovery, journey analysis, or validation before frontend changes.
- When NOT to use it: Pure backend or infrastructure work with no user-facing decision at stake.
- Inputs: User flows, research question, current UI, analytics or interview data, target cohort.
- Outputs: Research findings, pain-point map, usability issues, evidence-backed design recommendations.
- Core operating rules: Validate with evidence, not assumption; define the user and task clearly; separate observed behavior from proposed fixes.
- Suggested Tall Talents folder name: `ux-research`
- Suggested internal files to create: `talents/ux-research.md`, `examples/ux-research.md`, `templates/usability-findings.md`
- Port / Adapt / Merge notes: Adapt the research workflow and evidence bias; avoid bringing over generic persona fluff.
- Dependencies on any other talents: `design-before-build`, `ux-foundation`
- Overlap risk: Medium with `feedback-synthesis`; this talent is task/journey-focused rather than broad VoC synthesis.
- Implementation complexity: Medium
- Scores: Leverage `7` | Reusability `7` | Clarity `8` | Implementation Effort `4` | Differentiation `7` | Final Weighted Score `7.3`
- Confidence score: `8/10`

### UX Foundation

- Slug: `ux-foundation`
- Category: Design
- Source Repo(s): `agency-agents`
- Source File(s): `design/design-ux-architect.md`, `engineering/engineering-frontend-developer.md`
- Original Source Name(s): `UX Architect`, `Frontend Developer`
- Purpose: Translate product intent into implementation-oriented UX structure, layout systems, and component foundations.
- When to use it: Early UI architecture, frontend rewrites, design-system seed work, or when a team needs structure before styling.
- When NOT to use it: Cosmetic one-off tweaks where the UI foundation is already decided.
- Inputs: Approved product/design scope, existing UI patterns, implementation constraints, accessibility needs.
- Outputs: Layout foundations, component/system guidance, UX structure notes for implementers.
- Core operating rules: Build clear boundaries; optimize for developer comprehension; consider accessibility and performance; structure before polish.
- Suggested Tall Talents folder name: `ux-foundation`
- Suggested internal files to create: `talents/ux-foundation.md`, `examples/ux-foundation.md`, `templates/ui-foundation.md`
- Port / Adapt / Merge notes: Merge UX Architect’s structural role with Frontend Developer’s delivery-aware constraints.
- Dependencies on any other talents: `ux-research`, `design-before-build`
- Overlap risk: Medium with `architecture-decisioning`; this is product-interface structure, not system architecture.
- Implementation complexity: Medium
- Scores: Leverage `6` | Reusability `7` | Clarity `8` | Implementation Effort `5` | Differentiation `7` | Final Weighted Score `6.9`
- Confidence score: `7/10`

### Compliance Review

- Slug: `compliance-review`
- Category: Compliance
- Source Repo(s): `agency-agents`
- Source File(s): `support/support-legal-compliance-checker.md`, `strategy/playbooks/phase-0-discovery.md`, `strategy/playbooks/phase-4-hardening.md`
- Original Source Name(s): `Legal Compliance Checker`, `Phase 0 Playbook`, `Phase 4 Playbook`
- Purpose: Scan legal/regulatory obligations, assess risk, and encode controls or follow-up actions before launch.
- When to use it: Data handling, privacy, marketing claims, international rollout, regulated domains, or launch readiness.
- When NOT to use it: Harmless internal tooling with no legal or data exposure.
- Inputs: Jurisdictions, data flows, content/claim set, feature scope, operational model.
- Outputs: Compliance gaps, required controls, audit-trail needs, launch blockers or conditions.
- Core operating rules: Validate before implementation where possible; document rationale and audit trail; treat jurisdictional scope explicitly; escalate uncertainty instead of guessing.
- Suggested Tall Talents folder name: `compliance-review`
- Suggested internal files to create: `talents/compliance-review.md`, `examples/compliance-review.md`, `templates/compliance-scan.md`
- Port / Adapt / Merge notes: Adapt the decision flow and checklists; cut the heavy code examples and keep the operational questions.
- Dependencies on any other talents: `release-readiness-audit`, `product-requirements`
- Overlap risk: Low
- Implementation complexity: High
- Scores: Leverage `7` | Reusability `7` | Clarity `7` | Implementation Effort `7` | Differentiation `8` | Final Weighted Score `6.7`
- Confidence score: `8/10`

### Workflow Mapping

- Slug: `workflow-mapping`
- Category: Architecture
- Source Repo(s): `agency-agents`
- Source File(s): `specialized/specialized-workflow-architect.md`
- Original Source Name(s): `Workflow Architect`
- Purpose: Map complete workflow trees, failure branches, states, and handoff contracts before or alongside implementation.
- When to use it: Complex system flows, multi-service behavior, background jobs, approval paths, state machines, or high-risk business workflows.
- When NOT to use it: Simple CRUD or single-step utilities where the workflow tree would be trivial.
- Inputs: Routes, workers, data models, infra config, design docs, business rules.
- Outputs: Workflow registry, tree specs, state map, handoff contracts, test-case seeds.
- Core operating rules: Discover implicit workflows in code; spec more than the happy path; define states and cleanups; keep a registry; update when reality changes.
- Suggested Tall Talents folder name: `workflow-mapping`
- Suggested internal files to create: `talents/workflow-mapping.md`, `examples/workflow-mapping.md`, `templates/workflow-tree.md`
- Port / Adapt / Merge notes: Strong adaptation candidate; preserve its insistence on discovery and explicit failure branches.
- Dependencies on any other talents: `handoff-contracts`, `architecture-decisioning`
- Overlap risk: Medium with `design-before-build`; this talent is specifically about flows, states, and contracts.
- Implementation complexity: High
- Scores: Leverage `7` | Reusability `7` | Clarity `7` | Implementation Effort `8` | Differentiation `9` | Final Weighted Score `6.5`
- Confidence score: `8/10`

### Automation Governance

- Slug: `automation-governance`
- Category: Governance
- Source Repo(s): `agency-agents`
- Source File(s): `specialized/automation-governance-architect.md`
- Original Source Name(s): `Automation Governance Architect`
- Purpose: Decide whether automation is worth building, what safeguards it needs, and where human checkpoints must remain.
- When to use it: Workflow automation proposals, integration chains, ops tooling, or any “should we automate this?” decision.
- When NOT to use it: Straight coding work with no automation design decision in play.
- Inputs: Current process, time savings estimate, data criticality, dependency map, scale expectations.
- Outputs: Approve / pilot / partial / defer / reject verdict, architecture recommendation, test/monitoring baseline.
- Core operating rules: Technical possibility is not enough; evaluate value, criticality, dependency risk, and scalability; require fallback, logging, testing, and ownership.
- Suggested Tall Talents folder name: `automation-governance`
- Suggested internal files to create: `talents/automation-governance.md`, `examples/automation-governance.md`, `templates/automation-verdict.md`
- Port / Adapt / Merge notes: Adapt almost directly; it already reads like a neutral governance talent once n8n bias is softened.
- Dependencies on any other talents: `workflow-mapping`
- Overlap risk: Low
- Implementation complexity: Medium
- Scores: Leverage `7` | Reusability `8` | Clarity `9` | Implementation Effort `4` | Differentiation `9` | Final Weighted Score `8.0`
- Confidence score: `9/10`

### Executive Briefing

- Slug: `executive-briefing`
- Category: Communication
- Source Repo(s): `agency-agents`
- Source File(s): `support/support-executive-summary-generator.md`, `strategy/EXECUTIVE-BRIEF.md`
- Original Source Name(s): `Executive Summary Generator`, `NEXUS Executive Brief`
- Purpose: Convert complex findings into concise, quantified, decision-ready executive communication.
- When to use it: Research synthesis, audit wrap-ups, launch recommendations, risk briefings, or stakeholder decision packets.
- When NOT to use it: Raw exploratory work that has not been validated enough to summarize decisively.
- Inputs: Source findings, business context, quantified evidence, stakeholders, decision needed.
- Outputs: Situation overview, key findings, impact, recommendations, next steps.
- Core operating rules: Keep it short; quantify every major claim; order by business impact; include owners and timelines; avoid unsupported assumptions.
- Suggested Tall Talents folder name: `executive-briefing`
- Suggested internal files to create: `talents/executive-briefing.md`, `examples/executive-briefing.md`, `templates/executive-brief.md`
- Port / Adapt / Merge notes: Adapt the output contract and strong quantification rules; drop consulting theatrics and keep the concise structure.
- Dependencies on any other talents: `trend-research`, `feedback-synthesis`, `release-readiness-audit`
- Overlap risk: Low
- Implementation complexity: Low
- Scores: Leverage `6` | Reusability `8` | Clarity `9` | Implementation Effort `3` | Differentiation `7` | Final Weighted Score `7.8`
- Confidence score: `9/10`

## Output D — Recommended Tall-Talents Folder Plan

Tall Talents currently operates as a flat live library. The recommended plan below is therefore conceptual first:

- Draft in category folders during acquisition.
- Activate into flat files using the same slugs under `~/.tall-talents/talents/`.
- Preserve category in metadata tags and in repo-side staging structure.

Suggested staging structure:

```text
incoming/acquisition-wave/
  planning/
    design-before-build/
    implementation-planning/
    plan-execution/
    product-requirements/
    sprint-prioritization/
  execution/
    subagent-task-loop/
    parallel-agent-dispatch/
    minimal-diff-execution/
  coordination/
    workflow-orchestration/
    handoff-contracts/
  quality/
    systematic-debugging/
    test-first-delivery/
    verification-gate/
    code-review/
    review-feedback-triage/
    release-readiness-audit/
    visual-evidence-qa/
    api-validation/
    performance-benchmarking/
  architecture/
    architecture-decisioning/
    workflow-mapping/
    repo-onboarding-map/
  documentation/
    documentation-pass/
    executive-briefing/
  operations/
    worktree-isolation/
    branch-finish-workflow/
    devops-automation/
    incident-response/
    automation-governance/
  research/
    feedback-synthesis/
    trend-research/
    ux-research/
  design/
    ux-foundation/
  compliance/
    compliance-review/
```

Recommended live flat-file naming remains:

- `~/.tall-talents/talents/design-before-build.md`
- `~/.tall-talents/talents/implementation-planning.md`
- and so on for every selected slug.

## Output E — Implementation Queue

### Wave 1 — Highest Leverage, Easiest Wins

- `design-before-build`
- `implementation-planning`
- `systematic-debugging`
- `verification-gate`
- `code-review`
- `review-feedback-triage`
- `worktree-isolation`
- `branch-finish-workflow`
- `minimal-diff-execution`
- `repo-onboarding-map`
- `handoff-contracts`
- `release-readiness-audit`

### Wave 2 — Important, More Involved

- `plan-execution`
- `subagent-task-loop`
- `parallel-agent-dispatch`
- `architecture-decisioning`
- `documentation-pass`
- `security-review`
- `devops-automation`
- `incident-response`
- `product-requirements`
- `sprint-prioritization`
- `feedback-synthesis`
- `trend-research`

### Wave 3 — Specialized or Optional

- `workflow-orchestration`
- `visual-evidence-qa`
- `api-validation`
- `performance-benchmarking`
- `ux-research`
- `ux-foundation`
- `compliance-review`
- `workflow-mapping`
- `automation-governance`
- `executive-briefing`

## Output F — Rejection Log

Rejected outright or folded into stronger talents:

| Candidate | Source Repo | Decision | Reason |
| --- | --- | --- | --- |
| `using-superpowers` | `superpowers` | Rejected | Too harness-specific; better as plugin bootstrap guidance than a Tall Talent. |
| `writing-skills` | `superpowers` | Rejected | Valuable meta-skill, but too skill-authoring-specific for this acquisition wave. Better as a future Tall Talents meta-pack. |
| `document-review-system` | `superpowers` | Merged into `design-before-build` | Strong review loop, but better embedded in the pre-code design gate. |
| `brainstorming` visual companion mode | `superpowers` | Rejected | Tool-specific browser behavior, not core reusable talent logic. |
| Deprecated commands (`brainstorm`, `execute-plan`, `write-plan`) | `superpowers` | Rejected | Thin aliases, no durable value. |
| `Frontend Developer` | `agency-agents` | Rejected | Too broad and implementation-generic once UX foundation and architecture talents are extracted. |
| `Backend Architect` as standalone | `agency-agents` | Merged into `architecture-decisioning` | Strong patterns, but better merged with Software Architect for a more durable architectural talent. |
| `Git Workflow Master` | `agency-agents` | Folded into `worktree-isolation` and `branch-finish-workflow` | Strong git ideas, but the highest reusable parts were already captured by the stronger Superpowers git workflows. |
| `Rapid Prototyper` | `agency-agents` | Rejected | Useful, but overly tool-stack-prescriptive and overlaps with product/design/planning talents. |
| `Project Shepherd` | `agency-agents` | Rejected | Too general as a PM wrapper once orchestration, prioritization, and handoff talents exist. |
| `Experiment Tracker` | `agency-agents` | Rejected | Valuable but lower-frequency than the final 35 and partly overlaps with product requirements and analytics work. |
| `Analytics Reporter` | `agency-agents` | Rejected | High value, but overlaps with feedback, trend, executive briefing, and release reporting in this first port wave. |
| `Test Results Analyzer` | `agency-agents` | Rejected | Useful, but lower leverage than direct QA, review, and readiness talents. |
| `Workflow Optimizer` | `agency-agents` | Rejected | Strong process consulting role, but less core than orchestration, handoffs, and automation governance. |
| `Document Generator` | `agency-agents` | Rejected | Durable, but output-format-specific and better added later once Tall Talents needs document-runtime packaging. |
| `Model QA Specialist` | `agency-agents` | Rejected | Too niche for the initial Tall Talents acquisition wave. |
| `UI Designer` | `agency-agents` | Rejected | Style-heavy role; extracted the operational UX foundation instead. |
| `Brand Guardian` | `agency-agents` | Rejected | Valuable, but too brand/marketing-specific for the current Tall Talents gap set. |
| `Visual Storyteller` | `agency-agents` | Rejected | More creative direction than reusable production operating talent. |
| `Whimsy Injector` | `agency-agents` | Rejected | Largely taste/style wrapper, not operationally durable enough. |
| `Image Prompt Engineer` | `agency-agents` | Rejected | Valuable but domain-specific to image generation, not core Tall Talents operating leverage. |
| `Inclusive Visuals Specialist` | `agency-agents` | Rejected | Important, but too medium-specific for this coding/product/system-focused pass. |
| `Trend Researcher` niche source/tool details | `agency-agents` | Folded into `trend-research` | Kept the method, rejected the vendor/tool name sprawl. |
| `Legal Compliance Checker` code examples | `agency-agents` | Folded into `compliance-review` | Kept the audit questions and governance flow, rejected bulky implementation samples. |
| `Evidence Collector` Playwright script assumptions | `agency-agents` | Folded into `visual-evidence-qa` | Kept evidence doctrine, rejected repo-specific capture commands. |
| `Reality Checker` aesthetic “luxury” checks | `agency-agents` | Folded into `release-readiness-audit` | Kept skepticism, rejected style-claim-specific examples. |
| `NEXUS-Full`, `NEXUS-Sprint`, `NEXUS-Micro` branding | `agency-agents` | Rejected | Strong packaging, but the durable value lives in orchestration and handoff talents, not the branded modes. |
| Many domain-specialist agents (sales, finance, China-market roles, game dev roles) | `agency-agents` | Rejected | High-quality specialists, but out of scope for this coding/product/system-focused Tall Talents acquisition pass. |
| `.claude-plugin`, `.cursor-plugin`, `.opencode` install wrappers | `superpowers` | Rejected | Integration scaffolding, not transferable talent content. |

## Output G — Machine-Readable JSON

The full machine-readable JSON array of final talents is in:

- [agency-agents-superpowers-talent-acquisition.json](/Users/shanewalker/.codex/worktrees/68d5/tall-talents/docs/agency-agents-superpowers-talent-acquisition.json)

