import time

# Implementasi Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Memilih pivot di tengah
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Implementasi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Fungsi untuk mengukur waktu eksekusi
def measure_time(sort_function, arr):
    start_time = time.perf_counter()  # Gunakan perf_counter untuk presisi tinggi
    sort_function(arr.copy())  # Menggunakan salinan array untuk menjaga data asli tidak berubah
    end_time = time.perf_counter()
    return end_time - start_time

# Data uji
data_a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # Kelas A: Data terurut menurun
data_b = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]  # Kelas B: Data sebagian terurut naik, lalu menurun

# Mengukur waktu eksekusi Bubble Sort
bubble_time_a = measure_time(bubble_sort, data_a)
bubble_time_b = measure_time(bubble_sort, data_b)

# Mengukur waktu eksekusi Quick Sort
quick_time_a = measure_time(quick_sort, data_a)
quick_time_b = measure_time(quick_sort, data_b)

# Menampilkan hasil pengukuran waktu
print(f"Waktu eksekusi Kelas A (Bubble Sort): {bubble_time_a:.10f} detik")
print(f"Waktu eksekusi Kelas A (Quick Sort): {quick_time_a:.10f} detik")
print(f"Waktu eksekusi Kelas B (Bubble Sort): {bubble_time_b:.10f} detik")
print(f"Waktu eksekusi Kelas B (Quick Sort): {quick_time_b:.10f} detik")
