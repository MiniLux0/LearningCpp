---
name: generate-lesson-notes
description: >-
  Use this skill when the user asks to generate, create, or update study notes
  (.md files) for their C++ lessons or sections. This skill analyzes the source
  code files in a section folder and produces a well-structured markdown summary
  following the user's established note-taking style. Activate when the user
  mentions creating notes, summaries, or documentation for their classes/lessons.
---

# Generate Lesson Notes (.md)

This skill guides you through analyzing C++ lesson source files and generating
structured study notes in markdown — following the user's established style from
their LearningCpp repository.

---

## Context: The User's Project

This is a **learning repository** for C++ (John Purcell's Udemy course). Key facts:

- Each section lives in a numbered folder: `01_GettingStarted/`, `02_BasicSyntax/`, etc.
- Each lesson is a `.cpp` file: `L06_Variables.cpp`, `L16_ComparingFloats.cpp`, etc.
- Study notes go in `<section>/summary/<SectionName>_Notes.md`
- The user is a Physics student at UNI (Lima, Perú)
- Notes are written in **English** (code comments may mix English/Spanish)
- C++17 with GCC 15.2.0 on Windows

---

## The User's Note-Taking Style

**You MUST match this style exactly.** Study the patterns below:

### Header Format
```markdown
# Section Title — Study Notes

Personal notes from section NN of **John Purcell's** course on Udemy. Brief
description of what this section covers.

---
```

### Lesson Entry Format
```markdown
## LNN — Lesson Title

- Key concept explained in one clear sentence
- Another concept — with a brief clarification after the dash
- `code_example` shown inline when relevant
- Pattern: `code pattern` means "explanation in quotes"
- **Bold** for emphasis on critical terms
- Practical tip or gotcha at the end
```

### Style Rules (MUST FOLLOW)
1. **Bullet points only** — no numbered lists inside lessons
2. **One concept per bullet** — concise, not paragraphs
3. **Inline code** for C++ syntax: `int`, `cout`, `#include <header>`
4. **Bold** for important terms on first mention: **overflow**, **epsilon**
5. **Horizontal rules** (`---`) to separate major sections (between header and
   first lesson, and before "Good practices" section)
6. **Em dash** (`—`) for inline clarifications, not parentheses
7. **No code blocks inside notes** — keep it prose with inline code
8. **Group related lessons** when they share a concept (e.g., "L13–L15 — Conditionals")
9. **Mark unfinished lessons** with `*(pending)*` after the title
10. End with a "Good practices so far" section summarizing best practices learned
11. Last line: `*Last updated: LNN — Lesson Title*`

---

## Step-by-Step Procedure

### Step 1: Identify the Target Section

Ask the user which section to document, or detect it from context. Valid sections:

| Folder | Section | Lessons |
|:-------|:--------|:--------|
| `01_GettingStarted` | Getting Started | L01–L05 |
| `02_BasicSyntax` | Basic Syntax | L06–L26 |
| `03_Subroutines` | Subroutines | L27–L30 |
| `04_ObjectOriented` | Object Oriented Coding | L31–L38 |
| `05_PointersMemory` | Pointers and Memory | L39–L52 |
| `06_Inheritance` | Inheritance | L53–L55 |
| `07_OddsAndEnds` | Odds and Ends | L56–L57 |
| `08_ParticleFire` | Particle Fire Simulation | L58–L75 |
| `09_Conclusion` | Conclusion | L76–L77 |
| `10_Bonus` | Bonus | L78–L81 |
| `11_Advanced` | Advanced C++ | L82 |

### Step 2: Read All Source Files

For each `.cpp` file in the section folder:

1. Read the file content
2. Identify if it's **empty** (no code), **notes-only** (comments but no
   executable code), or **has code**
3. For files with code, extract:
   - What C++ concepts are demonstrated
   - Key patterns and techniques used
   - Any block comments with explanations
   - Common pitfalls or gotchas shown
4. For empty files, mark the lesson as `*(pending)*`

### Step 3: Read Existing Notes (if any)

Check if `<section>/summary/` already exists and has notes:
- If yes, read them and ask the user: "Update existing notes or regenerate?"
- If no, create the `summary/` directory and generate fresh notes

### Step 4: Generate the Notes File

Create `<section>/summary/<SectionName>_Notes.md` following the template:

```markdown
# {Section Title} — Study Notes

Personal notes from section {NN} of **John Purcell's** course on Udemy.
{Brief description of what this section covers — one or two sentences}.

---

## L{NN} — {Lesson Title}

- {Concept 1 — clear and concise}
- {Concept 2 with `inline_code` when showing syntax}
- {Concept 3 — **bold** for key terms}
- {Practical tip or common mistake}

## L{NN} — {Lesson Title}

- {Continue for each lesson...}

## L{NN}–L{NN} — {Group Title} *(pending)*

- {Brief preview of what these lessons cover if known}
- {Can be filled in later}

---

## Good practices so far

- {Practice 1 learned from this section}
- {Practice 2}
- {Practice 3}

---

*Last updated: L{NN} — {Last Lesson with Content}*
```

### Step 5: Validate

After generating the notes:

1. **Read back** the file to verify well-formed Markdown
2. **Check style** matches the user's existing notes
3. **Verify accuracy** — every concept mentioned must come from the actual
   source code, not invented
4. **Confirm completeness** — every `.cpp` file in the section should have a
   corresponding entry (even if marked pending)
5. **Present summary** to the user and ask for adjustments

---

## Additional Note Types

### GLOSSARY.md Updates

If the user asks to update the glossary, follow this format:

```markdown
## {Letter}

- **{Term}** — {Simple explanation in one sentence}
```

- Alphabetical order by section letter
- Terms from all lessons learned so far
- Simple language — explain like teaching someone new

### MISTAKES.md Updates

If the user asks to update mistakes, follow this format:

```markdown
## {Mistake Title}

**What happened:** {Brief description}
**Why:** {Root cause}
**Fix:** {How to avoid it}
```

### LearningProgress.md Updates

If the user asks to update progress, follow this format for each file:

```markdown
## {Section Folder}
- **{Filename}** — {One-line description of what the file demonstrates, or "Empty — no content yet"}
```

End with a `## Coding Notes` section highlighting observed patterns.

---

## Best Practices

- **Never invent concepts** — only document what the source code actually shows
- **Match the user's voice** — study notes feel personal, not formal documentation
- **Keep bullets short** — if a bullet is more than ~15 words, split it
- **Show the pattern** — when there's a common code pattern, show it inline:
  `pattern` means "explanation"
- **Highlight gotchas** — these are the most valuable parts of notes
  (e.g., "Integer division trap: `1/3 = 0`")
- **Spanish comments are OK** — the user sometimes writes comments in Spanish
  in their code, but notes should be in English
