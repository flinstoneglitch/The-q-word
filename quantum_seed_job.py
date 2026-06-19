import os
import json
from datetime import datetime

# IBM Quantum imports (REAL hardware)
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

# -------------------------
# RUN ON REAL QUANTUM HARDWARE
# -------------------------
def run_quantum():
    token = os.environ["IBM_QUANTUM_TOKEN"]
    service = QiskitRuntimeService(
        channel="ibm_quantum_platform",
        token=token,
    )

    # Pick the least-busy real QPU (never a simulator)
    backend = service.least_busy(operational=True, simulator=False)
    print("Using real backend:", backend.name)

    qc = QuantumCircuit(8, 8)
    qc.h(range(8))                      # superposition
    qc.measure(range(8), range(8))

    isa_qc = transpile(qc, backend=backend)
    sampler = SamplerV2(mode=backend)
    job = sampler.run([isa_qc], shots=1)
    print("Job ID:", job.job_id())

    result = job.result()
    counts = result[0].data.c.get_counts()
    bitstring = list(counts.keys())[0]
    return bitstring, backend.name, job.job_id()

# -------------------------
# CONVERT TO SEED
# -------------------------
def bits_to_seed(bits):
    return int(bits, 2)

# -------------------------
# MAIN DAILY SEED
# -------------------------
def generate_seed():
    bits, backend_name, job_id = run_quantum()
    seed = bits_to_seed(bits)

    today = datetime.utcnow().strftime("%Y-%m-%d")

    data = {
        "date": today,
        "quantum_bits": bits,
        "seed": seed,
        "backend": backend_name,
        "job_id": job_id
    }

    with open("seed.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Quantum seed generated:", data)

if __name__ == "__main__":
    generate_seed()
