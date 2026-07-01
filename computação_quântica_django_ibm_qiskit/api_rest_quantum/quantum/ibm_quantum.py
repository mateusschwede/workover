import os
from qiskit_ibm_runtime import QiskitRuntimeService

class IBMQuantumProvider:
    @staticmethod
    def get_service():
        return QiskitRuntimeService(
            channel="ibm_quantum_platform",
            token=os.getenv("IBM_QUANTUM_TOKEN")
        )

    @staticmethod
    def get_backend():
        service = IBMQuantumProvider.get_service()
        return service.least_busy(
            simulator=False,
            operational=True
        )