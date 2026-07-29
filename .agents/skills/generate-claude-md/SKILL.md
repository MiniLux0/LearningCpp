---
name: generate-claude-md
description: >-
  Use this skill when the user asks to generate, create, or update a CLAUDE.md
  file for their project. This skill analyzes the current project structure,
  tech stack, conventions, and workflows to produce a high-quality CLAUDE.md
  that serves as persistent project context for Claude Code and Claude AI.
---

# Generate CLAUDE.md

This skill guides you through analyzing the current project and generating a
**CLAUDE.md** file — the project-context file used by Claude Code (Anthropic)
to understand the project without repeated explanations.

---

## What is CLAUDE.md?

`CLAUDE.md` is a persistent instruction file that Claude reads at the start of
every session. It acts as an "onboarding brief" so the AI understands your
project's architecture, conventions, and guardrails automatically.

### Placement Hierarchy

| Location                    | Scope                                    |
| :-------------------------- | :--------------------------------------- |
| `~/.claude/CLAUDE.md`       | Global — applies to ALL projects         |
| `./CLAUDE.md` (project root)| Project — applies to the current project |
| `./src/CLAUDE.md` (subdir)  | Directory — overrides for that directory |

---

## Step-by-Step Procedure

### Step 1: Analyze the Project

Before writing anything, you **must** gather the following information by
reading the project files:

1.  **Root files**: Read `README.md`, `package.json`, `Cargo.toml`,
    `pyproject.toml`, `CMakeLists.txt`, `makefile`, `Makefile`, `go.mod`,
    `*.sln`, `*.csproj`, or any project manifest to identify:
    -   Project name and purpose
    -   Programming language(s)
    -   Framework(s) and major libraries
    -   Build system and package manager

2.  **Directory structure**: Use `list_dir` on the project root to understand
    the architecture and folder organization.

3.  **Existing conventions**: Look for:
    -   `.editorconfig`, `.prettierrc`, `.eslintrc`, `.clang-format`,
        `rustfmt.toml`, or similar config files
    -   Existing `CONTRIBUTING.md`, `CODING_STANDARDS.md`, or style guides
    -   Test directories and testing frameworks
    -   CI/CD configuration (`.github/workflows/`, `.gitlab-ci.yml`, etc.)

4.  **Key commands**: Identify build, test, lint, and run commands from the
    project manifest or makefile.

5.  **Existing CLAUDE.md**: Check if one already exists. If it does, read it
    and ask the user if they want to update/replace it.

### Step 2: Generate the CLAUDE.md

Write the file to the **project root** using the following template structure.
Adapt sections based on what you found in Step 1 — **omit sections that don't
apply**.

```markdown
# Project: {Project Name}

## Overview
{1-3 sentence description of what this project does}

## Tech Stack
- **Language**: {e.g., C++17}
- **Build System**: {e.g., Make, CMake, Cargo}
- **Framework**: {if applicable}
- **Key Libraries**: {list major dependencies}

## Project Structure
```
{Simplified directory tree showing key folders and their purpose}
```

## Development Commands
```bash
# Build
{build command}

# Run
{run command}

# Test
{test command}

# Clean
{clean command}
```

## Coding Conventions
- {Convention 1: e.g., "Use snake_case for variables and functions"}
- {Convention 2: e.g., "All public functions must have docstrings"}
- {Convention 3}

## Architecture Notes
- {Key architectural decisions or patterns}
- {Important relationships between components}

## Important Rules
- {Critical guardrails: e.g., "Never modify files in /vendor"}
- {Safety rules: e.g., "Always run tests before committing"}
- {Project-specific rules}
```

### Step 3: Validate

After generating the file:

1.  Read back the generated `CLAUDE.md` to verify it is well-formed Markdown.
2.  Confirm the file is between **30–200 lines** (concise but complete).
3.  Ensure no generic/placeholder content remains — every line should be
    specific to the actual project.
4.  Present a summary to the user and ask if they want to adjust anything.

---

## Best Practices

-   **Keep it lean**: Aim for 30–200 lines. If more documentation is needed,
    create separate files and reference them.
-   **Focus on what the AI doesn't know**: Don't document standard language
    knowledge. Document project-specific conventions and decisions.
-   **Be action-oriented**: Use imperative sentences ("Use X", "Never do Y",
    "Always run Z").
-   **Update regularly**: Treat it as a living document. Add rules when you
    find yourself correcting the AI on the same issue twice.
-   **No duplication**: Don't repeat information already in README.md unless it
    is critical for AI behavior.
