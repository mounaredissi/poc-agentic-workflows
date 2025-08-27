---
name: Simple Code Review
on:
  pull_request:
    types: [opened, synchronize]
engine: codex
---

When a pull request is opened:

1. Look at the Python files that changed
2. Check for these problems:
   - Hardcoded API keys or passwords
   - Functions that could crash (like dividing by zero)  
   - Missing type hints
   - Functions without documentation
   - Magic numbers without explanation

3. Look at the test files:
   - Are there tests for new functions?
   - Do tests check error cases?

4. Write a helpful comment on the PR with:
   - What you found
   - How to fix it
   - Why it matters

Be encouraging and educational. Focus on the biggest problems first.