import pandas as pd
from collections import defaultdict

data = pd.read_csv("phone.csv")

# variabel global
n = len(data)                           # jumlah data
template = "{:<20} | {:<30} | {:<30}"   # template untuk print

# Rumus untuk menghitung data numerik
# Mean
def myMean(atribut):
    # mean = Σx / n
    jumlah = 0
    for i in range(n):
        jumlah += data[atribut][i]
    return jumlah/n

# Median
def myMedian(atribut):
    sorted_data = sorted(data[atribut])
    mid = n // 2
    
    if n % 2 == 0:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median = sorted_data[mid]
    
    return median

# Modus
def myModus(atribut, tolerance=1e-5):
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
def myMax(atribut):
    max = data[atribut][0]
    for i in range(1, n):
        if data[atribut][i] > max:
            max = data[atribut][i]
    return max

def myMin(atribut):
    min = data[atribut][0]
    for i in range(1, n):
        if data[atribut][i] < min:
            min = data[atribut][i]
    return min

def myRange(atribut):
    # range = max - min
    return myMax(atribut) - myMin(atribut)

# Variance dan Standard Deviation
def myVariance(atribut):
    # variance = Σ(x - mean)^2 / (n - 1)
    mean = myMean(atribut)
    jumlah = 0
    for i in range(n):
        jumlah += (data[atribut][i] - mean) ** 2
    return jumlah / (n - 1)

def myStdDev(atribut):
    # stdDev = sqrt(variance)
    return myVariance(atribut) ** 0.5

# Quartile dan Interquartile Range
def percentile(data, p):
    k = (n - 1) * p / 100
    f = int(k)      # indeks bawah terdekat dari k
    c = k - f       # nilai desimal dari k
    if f + 1 < len(data):   # menghindari index out of range
        return data[f] * (1 - c) + data[f + 1] * c
    else:
        return data[f]

def myQ1(atribut):
    data_sorted = sorted(data[atribut])
    return percentile(data_sorted, 25)

def myQ3(atribut):
    data_sorted = sorted(data[atribut])
    return percentile(data_sorted, 75)
    
def myIQR(atribut):
    return myQ3(atribut) - myQ1(atribut)

# Skewness
# https://www.slideshare.net/slideshow/3-skewness-kurtosispptx/255323562
def mySkewness(atribut):
    # koefisien_skewness = Σ((x - mean) / stdDev)^3
    # pengali = n / ((n - 1) * (n - 2))
    # skewness = pengali * koefisien_skewness
    mean = myMean(atribut)
    stdDev = myStdDev(atribut)
    koefisien_skewness = 0
    pengali = n / ((n - 1) * (n - 2))
    for i in range(n):
        koefisien_skewness += (((data[atribut][i] - mean) / stdDev) ** 3)
    return koefisien_skewness * pengali

# Kurtosis
def myKurtosis(atribut):
    # koefisien_kurtosis = Σ((x - mean) / stdDev)^4
    # pengali = n * (n + 1) / ((n - 1) * (n - 2) * (n - 3))
    # pengurang = 3 * (n - 1)² / ((n - 2) * (n - 3))
    mean = myMean(atribut)
    stdDev = myStdDev(atribut)
    koefisien_kurtosis = 0
    pengali = n*(n + 1) / ((n - 1) * (n - 2) * (n - 3))
    pengurang = 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    for i in range(n):
        koefisien_kurtosis += (((data[atribut][i] - mean) / stdDev) ** 4)
    return pengali * koefisien_kurtosis - pengurang
