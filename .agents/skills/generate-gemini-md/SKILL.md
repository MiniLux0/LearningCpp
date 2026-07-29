---
name: generate-gemini-md
description: >-
  Use this skill when the user asks to generate, create, or update a GEMINI.md
  file for their project. This skill analyzes the current project structure,
  tech stack, conventions, and workflows to produce a high-quality GEMINI.md
  that serves as persistent project context for Gemini CLI and Gemini Code Assist.
---

# Generate GEMINI.md

This skill guides you through analyzing the current project and generating a
**GEMINI.md** file — the project-context file used by Gemini CLI and
Gemini Code Assist (Google) to understand the project without repeated
explanations.

---

## What is GEMINI.md?

`GEMINI.md` is a persistent context file that the Gemini CLI automatically
reads at session start. It acts as a "system prompt" for your specific project,
defining coding standards, architecture, and behavioral expectations.

### Placement Hierarchy

| Location                      | Scope                                     |
| :---------------------------- | :---------------------------------------- |
| `~/.gemini/GEMINI.md`         | Global — applies to ALL projects          |
| `./GEMINI.md` (project root)  | Project — applies to the current project  |
| `./src/GEMINI.md` (subdir)    | Directory — component-specific overrides  |

Files are loaded bottom-up: subdirectory rules override project rules, which
override global rules.

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

5.  **Existing GEMINI.md**: Check if one already exists. If it does, read it
    and ask the user if they want to update/replace it.

### Step 2: Generate the GEMINI.md

Write the file to the **project root** using the following template structure.
Adapt sections based on what you found in Step 1 — **omit sections that don't
apply**.

```markdown
# Project: {Project Name}

## General Instructions
- {Instruction 1: e.g., "Use C++17 standard for all code"}
- {Instruction 2: e.g., "Write comments in English"}
- {Instruction 3: e.g., "Prefer const references over copies"}

## Architecture
- {Architecture detail 1: e.g., "Each chapter is in its own numbered directory"}
- {Architecture detail 2: e.g., "Shared utilities live in /common"}
- {Key patterns and relationships}

## Tech Stack
- **Language**: {e.g., C++17}
- **Build System**: {e.g., Make, CMake}
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
- {Convention 1: e.g., "Use snake_case for file names"}
- {Convention 2: e.g., "Header files use .h extension, source files use .cpp"}
- {Convention 3: e.g., "Include guards use #pragma once"}

## Persona
- Respond in {language, e.g., Spanish}
- Act as a {role, e.g., "senior C++ tutor"}
- {Other behavioral instructions}

## Important Rules
- {Critical guardrails}
- {Safety rules}
- {Project-specific rules}
```

### Step 3: Validate

After generating the file:

1.  Read back the generated `GEMINI.md` to verify it is well-formed Markdown.
2.  Confirm the file is **concise but complete** — avoid bloat.
3.  Ensure no generic/placeholder content remains — every line should be
    specific to the actual project.
4.  Present a summary to the user and ask if they want to adjust anything.

---

## Best Practices

-   **Keep it focused**: Don't bloat the file with unnecessary information.
    Large context files impact performance.
-   **Use it for recurring rules**: If you find yourself telling the AI the
    same thing every session, add it to GEMINI.md.
-   **Version control it**: Commit `GEMINI.md` to the repository so all team
    members benefit from the same AI guidance.
-   **Use the hierarchy**: Put personal preferences in `~/.gemini/GEMINI.md`
    and project-specific rules in the project root's `GEMINI.md`.
-   **Be directive**: Use imperative sentences ("Use X", "Never do Y",
    "Always run Z"). The AI follows clear directives better than suggestions.
-   **No duplication**: Don't repeat what the README already says unless it
    is critical for shaping AI behavior.

---

## Compatibility Note

`GEMINI.md` is also recognized by Google Antigravity (AGY). When placed in the
project root, it serves as a directory-level rule that applies to the directory
and all subdirectories. See the
[Rules documentation](../../.gemini/antigravity-cli/builtin/skills/agy-customizations/docs/rules.md)
for more details on the Antigravity customization system.
