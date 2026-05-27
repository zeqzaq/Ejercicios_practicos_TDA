cola = []

cola.append("cliente 1")
cola.append("cliente 2")
cola.append("cliente 3")

print(f'Cola actual: {cola}')

atendido = cola.pop(0)
print(f'Cliente atendido: {atendido}')
print(f'Restante: {cola}')