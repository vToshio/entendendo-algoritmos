def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Escolha do pivô
        pivot = arr[len(arr) // 2]
        # Particiona o array
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Chama recursivamente quicksort para as sublistas
        return quicksort(left) + middle + quicksort(right)

# Exemplo de uso
array = [2, 4, 1, 16, 9, 27, 12]
sorted_array = quicksort(array)
print("Array ordenado:", sorted_array)
