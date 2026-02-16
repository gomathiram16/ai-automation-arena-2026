# AI Automation Arena – AutomationSTAR 2026

Welcome! This repo is for the hands-on tutorial.

## How to start (for attendees)
1. Click "Fork" (top right)
2. Click "Code" → "Open with Codespaces" → "Create codespace"
3. In the terminal run: `pip install -r requirements.txt`
4. Run tests: `pytest`

Follow the workshop challenges in order.

Instructor materials are in the prompts/ folder.

## Troubleshooting common issues

If you get `ModuleNotFoundError: No module named 'app'` when running pytest:

We added an empty `__init__.py` file in the `app/` folder — make sure it's there.
If still broken, run this once:

```bash
export PYTHONPATH=$PWD
