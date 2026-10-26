
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


# Data utama
nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))


# Test case
print("\n=== HASIL RETEST ===")

test_case = [
    ("T1", hitung_rata_rata([80, 60, 90, 70]), 75.0),
    ("T2", hitung_rata_rata([100, 80]), 90.0),
    ("T3", status(60), "Lulus"),
    ("T4", status(59), "Tidak lulus"),
    ("T5", nilai_tertinggi([80, 60, 90, 70]), 90),
]

for test_id, actual, expected in test_case:
    hasil = "PASS" if actual == expected else "FAIL"
    print(
        f"{test_id} | Expected: {expected} "
        f"| Actual: {actual} | {hasil}"
    )
