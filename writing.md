# Writing skills

## `humanizer`

Text that sounds machine-generated can be revised with this skill without changing its meaning or intended technical voice. It looks for inflated significance, promotional claims, vague attribution, repetitive sentence rhythm, stock transitions, forced groups of three, excessive em dashes, and chatbot residue, then requires a final "what still sounds generated?" self-review.

- Source: https://github.com/blader/humanizer/blob/main/SKILL.md
- Installed at: `~/.claude/skills/humanizer/SKILL.md`
- Available in: Cursor and Claude Code
- License: MIT
- Trust notes: Declares Read, Write, Edit, Grep, Glob, and AskUserQuestion; instruction-only with no bundled executable scripts or network calls. It can rewrite the user's files, so scope the input and preserve factual claims and citations.
- Install/update: `npx -y skills@1.5.18 add blader/humanizer --skill humanizer -g -a claude-code -y --copy`
