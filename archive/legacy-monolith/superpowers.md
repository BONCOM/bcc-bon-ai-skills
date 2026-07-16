---
type: Archive
title: superpowers
description: Legacy catalog or SDD artifact retained for history; prefer live OKF concepts under /skills/.
tags: [archive, legacy]
timestamp: 2026-07-16T00:00:00Z
---

# Superpowers

Superpowers 6.1.1 is a third-party plugin authored by Jesse Vincent/Obra and distributed to both clients through their official marketplaces. Cursor resolves it at `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99`; Claude Code resolves it at `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1`. The Claude plugin also registers one synchronous `SessionStart` hook. The 14 skill names below are counted once, not once per client.

## `brainstorming`

Creative implementation and behavior changes start with this design workflow. It explores the current project, asks one focused question at a time, compares approaches, gets approval on a written design, and only then hands the work to planning.

- Source: https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/brainstorming/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/brainstorming/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Bundles shell and Node scripts for an optional local visual-companion server, WebSocket helper, browser launcher, and HTML frame. It also writes design documents and may dispatch a spec reviewer; the companion is offered only when a visual question warrants it.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `dispatching-parallel-agents`

Two or more tasks with separate state, separate causes, and no ordering dependency can be dispatched through this skill. It assigns one isolated agent per problem with deliberately scoped context, then reconciles the independent results in the parent session.

- Source: https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/dispatching-parallel-agents/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/dispatching-parallel-agents/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only; no bundled executable scripts. It can launch several subagents concurrently, so tasks must not share files, mutable services, or a working directory where simultaneous edits would conflict.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `executing-plans`

A reviewed implementation plan can be run in a separate session with this workflow when subagent-driven work is unavailable. It checks the plan for blockers, executes each task with its prescribed verification, and then routes branch completion through the finishing workflow.

- Source: https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/executing-plans/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/executing-plans/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only; no bundled executable scripts. Following a plan can edit code, run project commands, and change Git state, so it stops on missing context, unclear instructions, or repeated verification failure.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `finishing-a-development-branch`

Branch integration is the final step after implementation and tests are complete. This skill freshly verifies tests, detects whether the workspace is a normal checkout or managed worktree, presents merge, PR, keep, or cleanup choices, and executes only the selected path.

- Source: https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/finishing-a-development-branch/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/finishing-a-development-branch/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only, but it runs tests and Git inspection and can merge branches, create a PR, remove a worktree, or delete a branch after the user chooses. Cleanup is not automatic.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `receiving-code-review`

Review feedback should pass through this technical check before implementation, particularly when a suggestion is ambiguous or may not fit the codebase. The skill separates understanding from agreement, verifies the claim, and supports reasoned pushback before applying one change at a time.

- Source: https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/receiving-code-review/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/receiving-code-review/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only; no bundled executable scripts or external service. Subsequent implementation still edits and tests the reviewed code, but the skill itself adds a verification gate before those changes.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `requesting-code-review`

A completed plan task, major feature, or pending merge is the point to request this review. The skill gives a fresh reviewer precise requirements and a bounded Git range rather than the author's full session history, then classifies findings by severity.

- Source: https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/requesting-code-review/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/requesting-code-review/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Bundles a reviewer prompt, reads Git SHAs, and dispatches a general-purpose subagent. It does not post to a remote review service or modify a pull request by itself.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `subagent-driven-development`

An approved plan with mostly independent tasks can run in the current session through this workflow. It creates a fresh implementer per task, follows each with specification and code-quality review, keeps a progress ledger, and adds a broad final review after all task gates pass.

- Source: https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/subagent-driven-development/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/subagent-driven-development/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Bundles three shell utilities for task briefs, SDD workspace state, and review packages plus several agent prompts. It launches implementers and reviewers and writes `.superpowers/sdd` records; agents must receive non-overlapping scope.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `systematic-debugging`

Bugs, test failures, build errors, integration issues, and unexplained performance problems all start with root-cause investigation here. The skill gathers evidence, traces the failure to its source, tests one hypothesis at a time, and revisits the model after repeated failed fixes.

- Source: https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/systematic-debugging/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/systematic-debugging/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Bundles `find-polluter.sh`, a TypeScript condition-waiting example, and diagnostic references. The shell helper repeatedly runs tests to isolate shared-state pollution and can be expensive on large suites.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `test-driven-development`

Implementation code for a feature, bug fix, refactor, or behavior change follows the test in this workflow. It requires a focused failure for the expected reason, the minimum code to pass, a fresh full verification, and cleanup only after the green state is established.

- Source: https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/test-driven-development/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/test-driven-development/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only with an anti-pattern reference. It directs file edits and test execution and may require discarding implementation written before the failing test; generated code and configuration exceptions require user approval.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `using-git-worktrees`

Plan execution and isolated feature work can use this worktree setup. It first detects managed worktrees and submodules, prefers the platform's native isolation, and falls back to Git only after checking location, ignore rules, branch state, and project setup.

- Source: https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/using-git-worktrees/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/using-git-worktrees/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only, but it runs Git commands and can create a branch, directory, and linked worktree. It asks for consent when no isolation preference exists and avoids nesting a worktree inside an already managed worktree.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `using-superpowers`

This is the session-level routing rule for the library. It requires checking applicable skills before responding or acting, orders process skills before implementation guidance, and exempts dispatched task subagents so their supplied task brief remains authoritative.

- Source: https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/using-superpowers/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/using-superpowers/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only with platform reference files. The plugin's `SessionStart` hook loads Superpowers context on startup, clear, and compact events; the hook runs synchronously but adds no MCP or agent component.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `verification-before-completion`

Completion, fix, pass, and merge-readiness claims need this evidence gate. It identifies the command that proves the claim, runs it fresh and in full, reads the result and exit status, and reports the actual state when evidence disagrees.

- Source: https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/verification-before-completion/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/verification-before-completion/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only; no bundled executable scripts. It runs project-specific verification commands and reads their complete output but does not define a universal test runner.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `writing-plans`

An approved design or multi-step requirement becomes an implementation handoff through this skill. It maps file responsibilities, splits work into independently reviewable tasks, specifies exact edits and tests, and saves the plan under `docs/superpowers/plans`.

- Source: https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/writing-plans/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/writing-plans/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Instruction-only with a plan-reviewer prompt. It reads project context and writes a detailed plan; it does not implement the planned code.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor

## `writing-skills`

Agent skill authoring, revision, and verification use pressure tests here rather than prose review alone. The workflow captures baseline failures, writes the smallest instruction that changes behavior, reruns scenarios, and closes newly observed loopholes.

- Source: https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md
- Installed at: `/Users/rramesh/.cursor/plugins/cache/cursor-public/superpowers/d884ae04edebef577e82ff7c4e143debd0bbec99/skills/writing-skills/SKILL.md`; `/Users/rramesh/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/skills/writing-skills/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Bundles a Node graph renderer, DOT examples, references, and test prompts. Its verification method dispatches subagents for baseline and with-skill pressure scenarios and can write rendered process graphs.
- Install/update: `claude plugin install superpowers@claude-plugins-official --scope user` for Claude Code; update the `cursor-public/superpowers` plugin through Cursor for Cursor
