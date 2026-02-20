# Copilot / AI Agent Instructions — Performance-Task-

Summary
- This repo is a tiny, in-repo Python CLI for creating/studying flashcards. The active script is `try2.py` (run with `python try2.py`). `main.py` appears to be scratch/notes and not runnable.

Big picture
- Single-process, interactive CLI: user input drives flow; data is held in-memory as Python dicts (no persistence).
- No external dependencies, no tests, and no packaging — treat this as a small script refactor task rather than a full app.

Key implementation patterns & what to watch for
- Top-level entry: currently `try2.py` directly calls `menu()` at import/run time. Use `if __name__ == '__main__':` if you add CLI args or expect imports.
- Nested function defs: `create_cards()` and `study()` are defined inside `menu()` branches. Move these to top-level functions so they are testable and predictable.
- Early `return` and recursion issues: `create_cards()` currently returns a dict after creating the first card and calls `menu()` on 'Q', and `study()` recurses into itself. These create broken control flow and potential infinite recursion. Prefer loops and explicit returns.

Concrete examples from the code
- Problem: `create_cards()` returns immediately after one card, e.g. in `try2.py` it does `flashcard_dict[question] = answer` then `return flashcard_dict` — update to accumulate cards until the user quits and then return the full dict.
- Problem: `study(dictionary)` calls itself inside the loop. Replace recursion with a straight loop over items and count correct/missed cards.

Developer workflows & useful commands
- Run the script interactively: `python try2.py`
- Quick debug run with pdb: `python -m pdb try2.py`
- If you add tests, use `pytest` (not currently present).

Conventions and style for this repo
- Use top-level, small pure functions where possible: `create_cards() -> dict`, `study(cards: dict) -> dict` (return stats), `menu()` only orchestrates.
- Prefer `snake_case` for functions and clear return values rather than relying on globals.
- Keep user I/O separated from core logic so unit tests can call logic directly.

Integration points & suggested safe changes
- There are no external integrations now. If adding persistence, prefer a small JSON file under a new `data/` folder and load/save via `json.load` / `json.dump`.
- Adding CLI args: use `argparse` and keep interactive mode as default.

Suggested tasks for an AI agent starting here
1. Refactor `try2.py`: extract `create_cards`, `study`, and helper functions to top-level; fix loop/return logic.
2. Add `if __name__ == '__main__': menu()` and make `menu()` call pure functions.
3. Add minimal tests for `create_cards` and `study` (use dependency injection for input/output or separate I/O layer).
4. Optionally remove or archive `main.py` if it's only notes.

If anything is unclear or you want the agent to perform the refactor and add tests, tell me which step to take next.
