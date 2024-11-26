import random

# Fungsi untuk menghasilkan bilangan acak
def generate_random_numbers(count, lower, upper, seed):
    random.seed(seed)  # Menetapkan seed
    return [random.randint(lower, upper) for _ in range(count)]

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag untuk mendeteksi pertukaran
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Jika tidak ada pertukaran, array sudah terurut
        if not swapped:
            break
    return arr


# Parameter
count = 50
lower = 0
upper = 100
seed = 40

# Menghasilkan bilangan acak
random_numbers = generate_random_numbers(count, lower, upper, seed)
print("Bilangan Acak Sebelum Sorting:")
print(random_numbers)

# Melakukan sorting dengan Bubble Sort
sorted_numbers = bubble_sort_optimized(random_numbers)
print("\nBilangan Acak Setelah Sorting:")
print(sorted_numbers)