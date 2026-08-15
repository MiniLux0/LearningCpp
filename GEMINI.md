# LearningCpp - Agent Custom Rules

These rules apply to any AI agent working within this repository.

## 1. File Encoding (CRITICAL)
- When writing scripts (especially PowerShell) to modify files, **ALWAYS enforce UTF-8 without BOM**.
- Emojis (like 🚀) and special characters (like —) will be corrupted if saved as UTF-16 LE (the PowerShell default).
- Example for PowerShell: `[System.IO.File]::WriteAllText($path, $text, [System.Text.UTF8Encoding]::new($false))`

## 2. Markdown Mathematics Formatting (CRITICAL)
- **Inline Math:** NEVER use standard `$ equation $`. Always wrap inline math in backticks to prevent Markdown parser collisions on GitHub. Format: `` $`O(N)`$ ``.
- **Block Math:** NEVER use `$$ ... $$` for multiline equations. Always use GitHub's math code blocks so backslashes (`\`) aren't stripped:
  ```math
  F_n = \left\{ ... \right.
  ```

## 3. Footer Standard
- All `.md` files must end with this exact footer:
```markdown
---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
```
