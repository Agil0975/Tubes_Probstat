import pandas as pd
from collections import defaultdict

DATA = pd.read_csv("phone.csv")

# variabel global
n = len(DATA)                           # jumlah data
template = "{:<20} | {:<30} | {:<30}"   # template untuk print

# Rumus untuk menghitung data numerik
# Mean
def myMean(data, atribut):
    # mean = Σx / n
    jumlah = 0
    for i in range(n):
        jumlah += data[atribut][i]
    return jumlah/n

# Median
def myMedian(data, atribut):
    sorted_data = sorted(data[atribut])
    mid = n // 2
    
    if n % 2 == 0:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median = sorted_data[mid]
    
    return median

# Modus
def myModus(data, atribut, tolerance=1e-5):
    frequency = defaultdict(int)
    
    for num in data[atribut]:
        found = False
        for key in frequency.keys():
            if abs(num - key) < tolerance:
                frequency[key] += 1
                found = True
                break
        if not found:
            frequency[num] += 1
    
    max_count = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_count]
    
    return modes[0]

# Maximum, Minimum, Range
def myMax(data, atribut):
    max = data[atribut][0]
    for i in range(1, n):
        if data[atribut][i] > max:
            max = data[atribut][i]
    return max

def myMin(data, atribut):
    min = data[atribut][0]
    for i in range(1, n):
        if data[atribut][i] < min:
            min = data[atribut][i]
    return min

def myRange(data, atribut):
    # range = max - min
    return myMax(data, atribut) - myMin(data, atribut)

# Variance dan Standard Deviation
def myVariance(data, atribut):
    # variance = Σ(x - mean)^2 / (n - 1)
    mean = myMean(data, atribut)
    jumlah = 0
    for i in range(n):
        jumlah += (data[atribut][i] - mean) ** 2
    return jumlah / (n - 1)

def myStdDev(data, atribut):
    # stdDev = sqrt(variance)
    return myVariance(data, atribut) ** 0.5

# Quartile dan Interquartile Range
def percentile(data, p):
    k = (n - 1) * p / 100
    f = int(k)      # indeks bawah terdekat dari k
    c = k - f       # nilai desimal dari k
    if f + 1 < len(data):   # menghindari index out of range
        return data[f] * (1 - c) + data[f + 1] * c
    else:
        return data[f]

def myQ1(data, atribut):
    data_sorted = sorted(data[atribut])
    return percentile(data_sorted, 25)

def myQ3(data, atribut):
    data_sorted = sorted(data[atribut])
    return percentile(data_sorted, 75)
    
def myIQR(data, atribut):
    return myQ3(data, atribut) - myQ1(data, atribut)

# Skewness
# https://www.slideshare.net/slideshow/3-skewness-kurtosispptx/255323562
def mySkewness(data, atribut):
    # koefisien_skewness = Σ((x - mean) / stdDev)^3
    # pengali = n / ((n - 1) * (n - 2))
    # skewness = pengali * koefisien_skewness
    mean = myMean(data, atribut)
    stdDev = myStdDev(data, atribut)
    koefisien_skewness = 0
    pengali = n / ((n - 1) * (n - 2))
    for i in range(n):
        koefisien_skewness += (((data[atribut][i] - mean) / stdDev) ** 3)
    return koefisien_skewness * pengali

# Kurtosis
def myKurtosis(data, atribut):
    # koefisien_kurtosis = Σ((x - mean) / stdDev)^4
    # pengali = n * (n + 1) / ((n - 1) * (n - 2) * (n - 3))
    # pengurang = 3 * (n - 1)² / ((n - 2) * (n - 3))
    mean = myMean(data, atribut)
    stdDev = myStdDev(data, atribut)
    koefisien_kurtosis = 0
    pengali = n*(n + 1) / ((n - 1) * (n - 2) * (n - 3))
    pengurang = 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    for i in range(n):
        koefisien_kurtosis += (((data[atribut][i] - mean) / stdDev) ** 4)
    return pengali * koefisien_kurtosis - pengurang

# Print Deskripsi Data
def printDescriptiveStatistics(data, atribut):
    print("Deskriptif Statistik | Fungsi Sendiri                 | Fungsi Library")
    print(template.format("Mean", myMean(data, atribut), data[atribut].mean()))
    print(template.format("Median", myMedian(data, atribut), data[atribut].median()))
    print(template.format("Modus", myModus(data, atribut), data[atribut].mode()[0]))
    print(template.format("Standar Deviasi", myStdDev(data, atribut), data[atribut].std()))
    print(template.format("Variansi", myVariance(data, atribut), data[atribut].var()))
    print(template.format("Range", myRange(data, atribut), data[atribut].max() - data[atribut].min()))
    print(template.format("Minimum", myMin(data, atribut), data[atribut].min()))
    print(template.format("Maksimum", myMax(data, atribut), data[atribut].max()))
    print(template.format("Q1", myQ1(data, atribut), data[atribut].quantile(0.25)))
    print(template.format("Q3", myQ3(data, atribut), data[atribut].quantile(0.75)))
    print(template.format("IQR", myIQR(data, atribut), data[atribut].quantile(0.75) - data[atribut].quantile(0.25)))
    print(template.format("Skewness", mySkewness(data, atribut), data[atribut].skew()))
    print(template.format("Kurtosis", myKurtosis(data, atribut), data[atribut].kurt()))