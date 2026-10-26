
def baca_nilai(nama_file):
    with open(nama_file, "r", encoding="utf-8") as file:
        isi = file.read()
    return isi


try:
    data = baca_nilai("nilai.txt")
    print("Isi file:", data)
except FileNotFoundError:
    print("File nilai.txt tidak ditemukan.")
