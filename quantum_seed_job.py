import json
import hashlib
from datetime import datetime

# IBM Quantum imports (real backend)
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# ----------------------------
# RUN QUANTUM CIRCUIT
# ----------------------------
def run_quantum():
    qc = QuantumCircuit(8, 8)
    qc.h(range(8))          # superposition
    qc.measure(range(8), range(8))

    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts()

    bitstring = list(counts.keys())[0]
    return bitstring


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
