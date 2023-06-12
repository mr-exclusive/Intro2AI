from qiskit import QuantumCircuit, Aer, QuantumRegister, ClassicalRegister, execute

# инициализируем квантовый регистр
q = QuantumRegister(1, 'circuit')  # 1 кубит
# инициализируем классический регистр (нужен чтобы записать результат измерений - 0 или 1)
c = ClassicalRegister(1, 'result')
qc = QuantumCircuit(q, c)

# получаем суперпозицию, применив оператор Адамара (что-то типа вероятности 50/50)
qc.h(q[0])
# qc.x(q[0])  # отрицание
# qc.cx(q[0], q[1])  # контролируемое отрицание. В случае с 2-мя кубитами, если первый в состоянии 1, то второй инвертируем.

# измеряем состояние кубита
qc.measure(q, c)

# локальный эмулятор квантовых вычислений
backend_p = Aer.get_backend('aer_simulator')
job = execute(qc, backend_p, shots=1024)  # будет сделано 1024 измерений
result = job.result().get_counts()
# print(result)

for state in list(result.keys()):
    print(f"Состояние {state} встречается {result[state]} раз")

# результат почти никогда не получается ровно 50/50,
# из-за существующих помех и ошибок (особенно если выполняется в эмуляторе),
# над которыми работают, но еще не смогли полностью избавиться
