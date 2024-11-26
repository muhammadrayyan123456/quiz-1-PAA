import random

# Fungsi untuk membangkitkan bilangan acak
def generate_random_numbers(count, lower, upper, seed):
    random.seed(seed)  # Menetapkan seed
    return [random.randint(lower, upper) for _ in range(count)]

def merge_sort_with_best_case_check(arr):
    # Jika array sudah terurut, langsung kembalikan
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return arr
    
    # Lanjutkan ke merge sort jika tidak terurut
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort_with_best_case_check(arr[:mid])
    right_half = merge_sort_with_best_case_check(arr[mid:])
    
    return merge(left_half, right_half)


# Fungsi untuk menggabungkan dua array yang terurut
def merge(left, right):
    sorted_array = []
    i = j = 0
    
    # Menggabungkan elemen secara berurutan
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # Menambahkan elemen yang tersisa
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array



# Parameter
count = 50
lower = 0
upper = 100
seed = 40


# Menghasilkan bilangan acak
random_numbers = generate_random_numbers(count, lower, upper, seed)
print("Bilangan Acak Sebelum Sorting:")
print(random_numbers)

# Melakukan sorting
sorted_numbers = merge_sort_with_best_case_check(random_numbers)
print("\nBilangan Acak Setelah Sorting:")
print(sorted_numbers)