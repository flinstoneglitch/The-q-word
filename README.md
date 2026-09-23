# ⚛️ The Q Word

A daily word puzzle where the secret word is chosen by quantum-sourced entropy.

**Play:** https://flinstoneglitch.github.io/The-q-word/

## How it works
Every day, a scheduled GitHub Action fetches a fresh seed from **QeNTROPY**, a
hybrid entropy engine that mixes several sources together:

- Local cryptographic entropy (always on)
- [ANU QRNG](https://qrng.anu.edu.au) — real hardware quantum randomness, via ANU's public API
- Amazon Braket — a real superposition-and-measure circuit run on Braket's SDK simulator
- IBM Quantum hardware — real qubits in superposition, when IBM access is available

The combined seed selects the word from a curated pool of 724 common
five-letter words, paints the
game's daily background image, and is displayed in-game along with its
source. Every seed is recorded in `seed.json`.

## Stack
- `index.html` — the entire game (vanilla JS, no frameworks)
- `.github/workflows/daily-seed.yml` — scheduled automation, pulls the daily seed from QeNTROPY
- Hosted on GitHub Pages, auto-deployed from this repo

## Credits
Created by Colin O'Reilly (Colin O'Reilly Studios / Artphorm),
built with AI collaborators: Claude (Anthropic) and ChatGPT (OpenAI).

## License
MIT
