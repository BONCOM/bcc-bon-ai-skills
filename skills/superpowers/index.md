# Superpowers skills

# Installed Superpowers skills

* [brainstorming](./brainstorming.md) - Creative implementation and behavior changes start with this design workflow. It explores the current project, asks one focused question at a time, compares app
* [dispatching-parallel-agents](./dispatching-parallel-agents.md) - Two or more tasks with separate state, separate causes, and no ordering dependency can be dispatched through this skill. It assigns one isolated agent per probl
* [executing-plans](./executing-plans.md) - A reviewed implementation plan can be run in a separate session with this workflow when subagent-driven work is unavailable. It checks the plan for blockers, ex
* [finishing-a-development-branch](./finishing-a-development-branch.md) - Branch integration is the final step after implementation and tests are complete. This skill freshly verifies tests, detects whether the workspace is a normal c
* [receiving-code-review](./receiving-code-review.md) - Review feedback should pass through this technical check before implementation, particularly when a suggestion is ambiguous or may not fit the codebase. The ski
* [requesting-code-review](./requesting-code-review.md) - A completed plan task, major feature, or pending merge is the point to request this review. The skill gives a fresh reviewer precise requirements and a bounded 
* [subagent-driven-development](./subagent-driven-development.md) - An approved plan with mostly independent tasks can run in the current session through this workflow. It creates a fresh implementer per task, follows each with 
* [systematic-debugging](./systematic-debugging.md) - Bugs, test failures, build errors, integration issues, and unexplained performance problems all start with root-cause investigation here. The skill gathers evid
* [test-driven-development](./test-driven-development.md) - Implementation code for a feature, bug fix, refactor, or behavior change follows the test in this workflow. It requires a focused failure for the expected reaso
* [using-git-worktrees](./using-git-worktrees.md) - Plan execution and isolated feature work can use this worktree setup. It first detects managed worktrees and submodules, prefers the platform's native isolation
* [using-superpowers](./using-superpowers.md) - This is the session-level routing rule for the library. It requires checking applicable skills before responding or acting, orders process skills before impleme
* [verification-before-completion](./verification-before-completion.md) - Completion, fix, pass, and merge-readiness claims need this evidence gate. It identifies the command that proves the claim, runs it fresh and in full, reads the
* [writing-plans](./writing-plans.md) - An approved design or multi-step requirement becomes an implementation handoff through this skill. It maps file responsibilities, splits work into independently
* [writing-skills](./writing-skills.md) - Agent skill authoring, revision, and verification use pressure tests here rather than prose review alone. The workflow captures baseline failures, writes the sm
