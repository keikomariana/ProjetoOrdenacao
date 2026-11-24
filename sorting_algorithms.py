# =====
# FAMÍLIA 1: ALGORITMOS BASEADOS EM COMPARAÇÃO
# =====

# 1. Bubble Sort O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:
            break
    return arr


# 2. Selection Sort O(n^2)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 3. Insertion Sort O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr


# 4. Merge Sort O(n log n)
def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]
        merge_sort(esquerda)
        merge_sort(direita)
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1
    return arr


# 5. Quick Sort O(n log n) médio
def quick_sort(arr, baixo=0, alto=None):
    if alto is None:
        alto = len(arr) - 1
    if baixo < alto:
        pi = _partition(arr, baixo, alto)
        quick_sort(arr, baixo, pi - 1)
        quick_sort(arr, pi + 1, alto)
    return arr

def _partition(arr, baixo, alto):
    pivo = arr[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1


# 6. Heap Sort O(n log n)
def _heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    if dir < n and arr[dir] > arr[maior]:
        maior = dir
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        _heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
    return arr


# =====
# FAMÍLIA 2: ALGORITMOS NÃO BASEADOS EM COMPARAÇÃO (LINEARES)
# =====

# 7. Counting Sort
def counting_sort(arr):
    if not arr:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    amplitude = max_val - min_val + 1
    contagem = [0] * amplitude
    saida = [0] * len(arr)
    for num in arr:
        contagem[num - min_val] += 1
    for i in range(1, len(contagem)):
        contagem[i] += contagem[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        saida[contagem[arr[i] - min_val] - 1] = arr[i]
        contagem[arr[i] - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = saida[i]
    return arr


# 8. Radix Sort
def _counting_sort_radix(arr, exp):
    n = len(arr)
    saida = [0] * n
    contagem = [0] * 10
    for i in range(n):
        indice = (arr[i] // exp)
        contagem[indice % 10] += 1
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]
    i = n - 1
    while i >= 0:
        indice = (arr[i] // exp)
        saida[contagem[indice % 10] - 1] = arr[i]
        contagem[indice % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = saida[i]

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        _counting_sort_radix(arr, exp)
        exp *= 10
    return arr


# 9. Bucket Sort (Otimizado)
def bucket_sort(arr):
    if not arr:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    if min_val == max_val:
        return arr
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]
    amplitude = max_val - min_val + 1
    for num in arr:
        indice = int((num - min_val) / amplitude * num_buckets)
        if indice == num_buckets:
            indice = num_buckets - 1
        buckets[indice].append(num)
    arr.clear()
    for bucket in buckets:
        bucket.sort()  # Usa a ordenação nativa ultra-rápida em C
        arr.extend(bucket)
    return arr