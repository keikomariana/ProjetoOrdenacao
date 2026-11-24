import time
import random
import matplotlib.pyplot as plt
from sorting_algorithms import (
    bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort, heap_sort,
    counting_sort, radix_sort, bucket_sort
)

def executar_e_gerar_graficos():
    # Tamanhos completos para os algoritmos rápidos (O(n log n) e Lineares)
    tamanhos_rapidos = [1_000, 10_000, 50_000, 100_000, 500_000]
    # Reduzido para 25.000 para correr instantaneamente sem travar
    tamanhos_quadraticos = [1_000, 5_000, 10_000, 25_000]
    seed_fixa = 42
    
    algoritmos = [
        ("Comparação O(n²)", "Bubble Sort", bubble_sort, tamanhos_quadraticos),
        ("Comparação O(n²)", "Selection Sort", selection_sort, tamanhos_quadraticos),
        ("Comparação O(n²)", "Insertion Sort", insertion_sort, tamanhos_quadraticos),
        ("Comparação O(n log n)", "Merge Sort", merge_sort, tamanhos_rapidos),
        ("Comparação O(n log n)", "Quick Sort", quick_sort, tamanhos_rapidos),
        ("Comparação O(n log n)", "Heap Sort", heap_sort, tamanhos_rapidos),
        ("Não Comparação (Linear)", "Counting Sort", counting_sort, tamanhos_rapidos),
        ("Não Comparação (Linear)", "Radix Sort", radix_sort, tamanhos_rapidos),
        ("Não Comparação (Linear)", "Bucket Sort", bucket_sort, tamanhos_rapidos),
    ]
    
    resultados = {}
    
    print("Iniciando bateria de testes otimizada...\n")
    
    for categoria, nome, func_sort, lista_tamanhos in algoritmos:
        tempos_alg = []
        print(f"Testando {nome}...")
        for n in lista_tamanhos:
            random.seed(seed_fixa)
            vetor_base = [random.randint(0, 1_000_000) for _ in range(n)]
            
            tempos = []
            for _ in range(3):
                copia_vetor = list(vetor_base)
                inicio = time.perf_counter()
                func_sort(copia_vetor)
                fim = time.perf_counter()
                tempos.append((fim - inicio) * 1000)
            
            media_ms = sum(tempos) / len(tempos)
            tempos_alg.append(media_ms)
            
        resultados[nome] = (lista_tamanhos, tempos_alg)

    # 1. IMPRIMIR TABELA FORMATADA
    print("\n" + "="*95)
    print("TABELA COMPARATIVA DE RESULTADOS (Tempos em ms)")
    print("="*95)
    cabecalho = f"| {'Categoria':<23} | {'Algoritmo':<15} | " + " | ".join([f"N={t:<7}" for t in tamanhos_rapidos]) + " |"
    print(cabecalho)
    print("-" * len(cabecalho))
    
    for categoria, nome, func_sort, lista_tamanhos in algoritmos:
        tamanhos_usados, valores = resultados[nome]
        valores_str_parts = []
        for t in tamanhos_rapidos:
            if t in tamanhos_usados:
                idx = tamanhos_usados.index(t)
                val = valores[idx]
                valores_str_parts.append(f"{val:>8.2f}")
            else:
                valores_str_parts.append(f"{'Excedido':>8}")
        valores_str = " | ".join(valores_str_parts)
        print(f"| {categoria:<23} | {nome:<15} | {valores_str} |")
    print("="*95)

    # 2. GERAR GRÁFICO GERAL
    plt.figure(figsize=(10, 6))
    for categoria, nome, func_sort, lista_tamanhos in algoritmos:
        tamanhos_usados, valores = resultados[nome]
        estilo = '--' if "O(n²)" in categoria else '-'
        plt.plot(tamanhos_usados, valores, marker='o', linestyle=estilo, label=nome)
    
    plt.title("Comparação Geral: Tempo de Execução vs. Tamanho do Vetor (N)")
    plt.xlabel("Tamanho do Vetor (N)")
    plt.ylabel("Tempo Médio (ms)")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.savefig("grafico_geral.png", dpi=300)
    plt.close()

    # 3. GERAR GRÁFICO ZOOM
    plt.figure(figsize=(10, 6))
    for categoria, nome, func_sort, lista_tamanhos in algoritmos:
        if "O(n²)" not in categoria:
            tamanhos_usados, valores = resultados[nome]
            estilo = '-.' if "Linear" in categoria else '-'
            plt.plot(tamanhos_usados, valores, marker='s', linestyle=estilo, label=nome)
            
    plt.title("Zoom: Algoritmos O(n log n) vs. Lineares (Sem O(n²))")
    plt.xlabel("Tamanho do Vetor (N)")
    plt.ylabel("Tempo Médio (ms)")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.savefig("grafico_rapidos.png", dpi=300)
    plt.close()
    print("\n[CONCLUÍDO] Gráficos salvos e tabela gerada com sucesso!")

if __name__ == "__main__":
    executar_e_gerar_graficos()