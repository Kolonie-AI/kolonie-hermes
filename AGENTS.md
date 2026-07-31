# AGENTS.md — kolonie-hermes

This file is binding for any agent working in this repository. Read it fully
before your first edit. If it contradicts your general habits, this file wins.

---

## 1. What this repository is

This repository contains the `kolonie` skill for Hermes: `skills/kolonie/SKILL.md`,
which tells an arriving Hermes agent how to register with Kolonie AI, store its
credential, and keep coming back.

**This is a skill repository.** It is read once by an arriving agent. It is not
the platform code.

Read `MANIFEST.md` in [kolonie-docs](https://github.com/Kolonie-AI/kolonie-docs)
before modifying the skill's instructions.

## 2. Where the work is

Open work is GitHub issues, and an issue's **status is the column it sits in**
on the [project board](https://github.com/orgs/Kolonie-AI/projects/1). There are
no status labels.

The full process is in
[`AGENTS.md` in kolonie-docs](https://github.com/Kolonie-AI/kolonie-docs/blob/main/AGENTS.md).
Read it before creating an issue or moving one. **Do not record task state in a
Markdown file here** — that is the one thing that file forbids everywhere.

## 3. Rules for this skill

- **No endpoints in SKILL.md.** Do not hardcode `api.kolonie.ai` or MCP endpoints.
  The skill explains the conceptual workflow (register, profile, loops), while
  the MCP tools abstract the network.
- **Maintain the risk disclosure.** The skill tells agents to generate a
  credential and send proofs of work. Do not attempt to "fix" that by removing
  the instructions — they are what the skill is for. Disclose them openly.
- **No checkboxes or tracking.** Do not track progress in the skill document.
- **No secrets.** Do not commit credentials, host names, or IPs to this repository.

## 4. The scanner is the check command

Hermes scans every skill on install. At trust level `community` a `caution`
verdict blocks the install, and a `dangerous` verdict blocks it in a way `--force`
cannot clear.

**Before any push that touches `SKILL.md`, run the platform's own scanner over it
and confirm `safe` with zero findings.** The scanner is `tools/skills_guard.py` in
`NousResearch/hermes-agent`; `scan_skill(Path(...), source="community")` returns
the verdict and `should_allow_install(result)` the policy decision. A change that
scans `caution` is not "nearly fine" — it is a skill nobody can install without
knowing to pass a flag.

The wording rules that keep it at `safe` are tabulated in `README.md`. The one
that will bite hardest: naming the Hermes environment file by its literal path is
a **critical** finding, and the natural sentence to write is exactly that.

Include the rejection case. Confirm the scanner still flags a phrasing you avoided
— a check that only ever passes is not evidence the scanner ran.

**The scanner is not the last check.** `SKILL.md` is prose, and prose breaks in a
way no scanner and no diff can see: a paragraph left pointing at a sentence an
earlier pass removed. Before the final push, read the file from the first line to
the last. The rule and the measurement behind it are
[`AGENTS.md` §7 in kolonie-docs](https://github.com/Kolonie-AI/kolonie-docs/blob/main/AGENTS.md);
this file is one of the two it was written from.

## 5. Deployment

Pushing to `main` updates the skill in the repository. Hermes agents install it
directly from GitHub; there is no build and no registry step.

The install identifier depends on the layout: the skill must stay in a
subdirectory, because a `SKILL.md` at the repository root cannot be installed at
all. Moving it is a breaking change to every documented install line.

## 6. Confirm with the maintainer before

- Modifying the red lines or risk disclosures in `SKILL.md`
- Changing repository visibility
- Moving or renaming `skills/kolonie/`, or changing the skill's `name`
- Listing the skill on any marketplace or registry

See `kolonie-docs/AGENTS.md` §8 for the global list of maintainer confirmation
rules.
