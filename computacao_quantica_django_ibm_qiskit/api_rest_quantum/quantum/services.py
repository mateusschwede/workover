import os
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import SamplerV2
from .ibm_quantum import IBMQuantumProvider

class QuantumService:
    @staticmethod
    def health():
        return {"status": "quantum-service-ok"}
    
    @staticmethod
    def test_ibm_connection():
        backend = IBMQuantumProvider.get_backend()

        return {
            "connected": True,
            "backend": backend.name
        }

    @staticmethod
    def generate_random_bit():
        backend = IBMQuantumProvider.get_backend()

        circuit = QuantumCircuit(1)
        circuit.h(0)
        circuit.measure_all()

        circuit_ascii = circuit.draw(output="text").single_string()
        
        transpiled_circuit = transpile(circuit, backend=backend)
        sampler = SamplerV2(mode=backend)
        job = sampler.run([transpiled_circuit], shots=1)

        result = job.result()
        bitstrings = result[0].data.meas.get_bitstrings()
        bit = int(bitstrings[0])

        return {
            "bit": bit,
            "backend": backend.name,
            "circuit": circuit_ascii
        }
    
    @staticmethod
    def coin_flip():
        random_result = QuantumService.generate_random_bit()

        return {
            "result": (
                "heads"
                if random_result["bit"] == 0
                else "tails"
            ),
            "backend": random_result["backend"],
            "circuit": random_result["circuit"]
        }
    
    @staticmethod
    def generate_random_number(bits):
        if bits < 1 or bits > 16:
            raise ValueError("Bits devem ser entre 1 e 16")

        backend = IBMQuantumProvider.get_backend()
        circuit = QuantumCircuit(bits)

        for i in range(bits):
            circuit.h(i)

        circuit.measure_all()

        circuit_ascii = circuit.draw(output="text").single_string()

        transpiled_circuit = transpile(circuit, backend=backend)
        sampler = SamplerV2(mode=backend)
        job = sampler.run([transpiled_circuit], shots=1)

        result = job.result()
        bitstrings = result[0].data.meas.get_bitstrings()
        binary = bitstrings[0]
        decimal = int(binary, 2)

        return {
            "bits": bits,
            "binary": binary,
            "decimal": decimal,
            "backend": backend.name,
            "circuit": circuit_ascii
        }