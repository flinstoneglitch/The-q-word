import json
import requests
import hashlib
from datetime import datetime

# IBM Quantum imports (real backend)

# ----------------------------
# RUN QUANTUM CIRCUIT
# ----------------------------
def run_quantum():
    data = requests.get(
        "https://q-runtime.onrender.com/api/random",
        timeout=30
    ).json()

    return data["bitstring"]

# ----------------------------
# CONVERT TO SEED
# ----------------------------
def bits_to_seed(bits):
    return int(bits, 2)


# ----------------------------
# MAIN DAILY SEED
# ----------------------------
def generate_seed():
    bits = run_quantum()
    seed = bits_to_seed(bits)

    today = datetime.utcnow().strftime("%Y-%m-%d")

    data = {
        "date": today,
        "quantum_bits": bits,
        "seed": seed
    }

    with open("seed.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Quantum seed generated:", data)


if __name__ == "__main__":
    generate_seed()
