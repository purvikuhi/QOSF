import qiskit as q

def find_negative_numbers(list_number):

    # number of qubits depending on the input list
    n_qubits = len(list_number)

    circuit = q.QuantumCircuit(n_qubits)

    # encoding each number in the list 
    for i, num in enumerate(list_number):
        circuit.h(i)
        if num < 0:
            circuit.x(i)  # flipping for -ve numbers

    circuit.measure_all() 
    print(circuit) # printing for visualisation 

    simulator = q.Aer.get_backend('qasm_simulator')
    result = simulator.run(circuit).result()

    # result for the first measurement 
    # it shall be same for all qubits
    counts = result.get_counts()
    first_measurement = next(iter(counts.keys()))

    # checking for any "1" in the measurement outcome
    # it indicates that a -ve number was detected
    return "1" in first_measurement

# example:
example = find_negative_numbers([1, -3, 2, 15])
print(example)  
