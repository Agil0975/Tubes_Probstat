import numpy as np
import pandas as pd
data = pd.read_csv("phone.csv")

banyak_data = len(data)
# print(banyak_data)

# # menghitung mean setiap kolom numerik
# # rumus sendiri
# def sumData(atribut):
#     jumlah = 0
#     for i in range(banyak_data):
#         jumlah += data[atribut][i]
#     return jumlah
# # rumus dari pandas

# # battery_power
# battery_power_mean = sumData('battery_power') / banyak_data
# battery_power_mean_with_pandas = data['battery_power'].sum() / banyak_data
# print(battery_power_mean)
# print(battery_power_mean_with_pandas)
# # clock_speed
# # ram
# # n_cores
# # use_time
# # px_width
# # px_height
# # brand
# # 5g
# # grade
# # price

# from scipy import stats

# Fungsi deskriptif statistik untuk data numerik menggunakan metode sendiri
# def descriptive_statistics_custom(df):
#     desc = {}
#     desc['mean'] = df.mean()
#     desc['median'] = df.median()
#     desc['mode'] = df.mode().iloc[0] if not df.mode().empty else np.nan
#     desc['std_dev'] = df.std()
#     desc['variance'] = df.var()
#     desc['range'] = df.max() - df.min()
#     desc['min'] = df.min()
#     desc['max'] = df.max()
#     desc['q1'] = df.quantile(0.25)
#     desc['q3'] = df.quantile(0.75)
#     desc['iqr'] = desc['q3'] - desc['q1']
#     desc['skewness'] = df.skew()
#     desc['kurtosis'] = df.kurtosis()
#     return desc

# # Fungsi deskriptif statistik untuk data numerik menggunakan library
# def descriptive_statistics_library(df):
#     desc = df.describe().T
#     desc['skew'] = df.skew()
#     desc['kurt'] = df.kurtosis()
#     return desc

# # Contoh DataFrame
# data = pd.DataFrame({
#     'values': np.random.randn(1000) * 10 + 50
# })

# # Menghitung statistik deskriptif menggunakan kedua metode
# custom_stats = descriptive_statistics_custom(data['values'])
# library_stats = descriptive_statistics_library(data['values'])

# Membuat template untuk format output
# template = "{:<20} | {:<30} | {:<30}"

# # Mencetak header
# print(template.format("Deskriptif Statistik", "Fungsi Sendiri", "Fungsi Library"))
# print(template.format("Mean", "123.123", "1214.2312"))

# Mencetak setiap statistik
# for stat in custom_stats.keys():
#     print(template.format(
#         stat.capitalize(),
#         f"{custom_stats[stat]:<30.10f}",
#         f"{library_stats.get(stat, 'N/A'):<30.10f}"
#     ))

def mymax(atribut):
    max = data[atribut][0]
    for i in range(1, banyak_data):
        if data[atribut][i] > max:
            max = data[atribut][i]
    return max

def mymin(atribut):
    min = data[atribut][0]
    for i in range(1, banyak_data):
        if data[atribut][i] < min:
            min = data[atribut][i]
    return min

print(mymax('battery_power'))
print(mymin('battery_power'))
print(data['battery_power'].max())
print(data['battery_power'].min())

def find_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 == 0:
        # Jika jumlah elemen genap, median adalah rata-rata dari dua nilai tengah
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        # Jika jumlah elemen ganjil, median adalah nilai tengah
        median = sorted_data[mid]
    
    return median

# Contoh penggunaan
data = [1, 2, 3, 4, 5]
print("Median (tanpa numpy):", find_median(data))

data = [1, 2, 3, 4, 5, 6]
print("Median (tanpa numpy):", find_median(data))

def find_mode(data):
    frequency = {}
    
    # Menghitung frekuensi setiap elemen
    for item in data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    # Mencari frekuensi maksimum
    max_freq = max(frequency.values())
    
    # Mengumpulkan semua elemen yang memiliki frekuensi maksimum
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    # Jika hanya ada satu elemen dengan frekuensi maksimum, kembalikan elemen tersebut
    if len(modes) == 1:
        return modes[0]
    else:
        # Jika ada lebih dari satu elemen dengan frekuensi maksimum, kembalikan semua
        return modes

# Contoh penggunaan
data = [1, 2, 2, 3, 4, 4, 4, 5]
print("Modus (tanpa library):", find_mode(data))

data = [1, 1, 2, 2, 3, 3]
print("Modus (tanpa library):", find_mode(data))


from collections import defaultdict

def find_mode(data, tolerance=1e-5):
    frequency = defaultdict(int)
    
    # Menghitung frekuensi dengan pengelompokan berdasarkan toleransi
    for item in data:
        found = False
        for key in frequency:
            if abs(key - item) < tolerance:
                frequency[key] += 1
                found = True
                break
        if not found:
            frequency[item] += 1
    
    # Mencari frekuensi maksimum
    max_freq = max(frequency.values())
    
    # Mengumpulkan semua elemen yang memiliki frekuensi maksimum
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    # Jika hanya ada satu elemen dengan frekuensi maksimum, kembalikan elemen tersebut
    if len(modes) == 1:
        return modes[0]
    else:
        # Jika ada lebih dari satu elemen dengan frekuensi maksimum, kembalikan semua
        return modes

# Contoh penggunaan
data = [1.2, 2.3, 2.3, 3.4, 4.500000001, 4.500000004, 4.5, 5.6]
print("Modus (tanpa library):", find_mode(data))

data = [1.1, 1.100001, 1.100002, 2.2, 2.200001, 2.200002]
print("Modus (tanpa library):", find_mode(data))
