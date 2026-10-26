
def hitung_total(data):
    total = 0

    for nilai in data:
        total += nilai

    return total


data_nilai = [80, 60, 90, 70]
hasil = hitung_total(data_nilai)

print("Data nilai:", data_nilai)
print("Total nilai:", hasil)
