# ⚛️ The Q Word

A daily word puzzle where the secret word is chosen by a **real IBM quantum computer**.

**Play:** https://theqword.netlify.app

## How it works
Every day, a GitHub Action runs an experiment on IBM Quantum hardware:
8 qubits are placed in superposition and measured. The resulting bitstring
becomes the day's seed — selecting the word from a 5,757-word pool, painting
the game's background, and displayed in-game with the backend name. Every
seed is verifiable via its IBM job ID, recorded in `seed.json`.

## Stack
- `index.html` — the entire game (vanilla JS, no frameworks)
- `quantum_seed_job.py` — daily quantum experiment (Qiskit / IBM Runtime)
- `.github/workflows/daily-seed.yml` — scheduled automation
- Hosted on Netlify, auto-deployed from this repo

## Credits
Created by Colin O'Reilly (Colin O'Reilly Studios / Artphorm),
built with AI collaborators: Claude (Anthropic) and ChatGPT (OpenAI).

## License
MIT
