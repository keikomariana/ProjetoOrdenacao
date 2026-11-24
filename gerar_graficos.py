import matplotlib.pyplot as plt

# Tamanhos de N usados nos teus testes
tamanhos = [1000, 10000, 50000, 100000, 500000]

# SUBSTITUI OS NÚMEROS ABAIXO PELOS TEMPOS (EM MS) QUE APARECERAM NO TEU TERMINAL:
dados = {
    "Bubble Sort":    [0.0, 0.0, 0.0, 0.0, 0.0],
    "Selection Sort": [0.0, 0.0, 0.0, 0.0, 0.0],
    "Insertion Sort": [0.0, 0.0, 0.0, 0.0, 0.0],
    "Merge Sort":     [0.0, 0.0, 0.0, 0.0, 0.0],
    "Quick Sort":     [0.0, 0.0, 0.0, 0.0, 0.0],
    "Heap Sort":      [0.0, 0.0, 0.0, 0.0, 0.0],
    "Counting Sort":  [0.0, 0.0, 0.0, 0.0, 0.0],
    "Radix Sort":     [0.0, 0.0, 0.0, 0.0, 0.0],
    "Bucket Sort":    [0.0, 0.0, 0.0, 0.0, 0.0],
}

quadraticos = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
lineares = ["Counting Sort", "Radix Sort", "Bucket Sort"]

# 1. Gráfico Geral (Todos os 9 algoritmos)
plt.figure(figsize=(10, 6))
for nome, tempos in dados.items():
    estilo = '--' if nome in quadraticos else '-'
    plt.plot(tamanhos, tempos, marker='o', linestyle=estilo, label=nome)

plt.title("Comparação Geral: Tempo de Execução vs. Tamanho do Vetor (N)")
plt.xlabel("Tamanho do Vetor (N)")
plt.ylabel("Tempo Médio (ms)")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.savefig("grafico_geral.png", dpi=300)
plt.close()

# 2. Gráfico Zoom (Apenas O(n log n) e Lineares)
plt.figure(figsize=(10, 6))
for nome, tempos in dados.items():
    if nome not in quadraticos:
        estilo = '-.' if nome in lineares else '-'
        plt.plot(tamanhos, tempos, marker='s', linestyle=estilo, label=nome)

plt.title("Zoom: Algoritmos O(n log n) vs. Lineares (Sem O(n²))")
plt.xlabel("Tamanho do Vetor (N)")
plt.ylabel("Tempo Médio (ms)")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.savefig("grafico_rapidos.png", dpi=300)
plt.close()

print("Gráficos gerados com sucesso na pasta!")