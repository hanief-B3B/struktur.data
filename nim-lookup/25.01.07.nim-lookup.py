# Tugas Struktur Data Hanief Bintang Tri Buana (I.2410153)

class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __repr__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return int(key.replace("I.", "").replace("l.", "")) % self.size

    def insert(self, mahasiswa):
        index = self.hash_function(mahasiswa.nim)
        if not self.table[index]:
            self.table[index] = []
        self.table[index].append(mahasiswa)

    def search_by_nim(self, nim):
        index = self.hash_function(nim)
        if self.table[index]:
            for mahasiswa in self.table[index]:
                if mahasiswa.nim == nim:
                    return mahasiswa
        return None

    def search_by_name(self, name):
        for bucket in self.table:
            if bucket:
                for mahasiswa in bucket:
                    if name.lower() in mahasiswa.nama.lower():
                        return mahasiswa
        return None

# Fungsi untuk menampilkan data mahasiswa yang telah diurutkan berdasarkan nama
def sort_mahasiswa_by_name(mahasiswa_list):
    return sorted(mahasiswa_list, key=lambda x: x.nama)

# Data Mahasiswa
mahasiswa_data = [
    Mahasiswa("I.2410188", "Agil Ardiansyah", "Ilmu Komputer"),
    Mahasiswa("I.2410169", "Muhammad Nazar", "Ilmu Komputer"),
    Mahasiswa("I.2410167", "Ariyanto", "Ilmu Komputer"),
    Mahasiswa("I.2410343", "Virza Shahnara", "Ilmu Komputer"),
    Mahasiswa("I.2410153", "Hanief Bintang Tri Buana", "Ilmu Komputer"),
    Mahasiswa("l.2410157", "Muhammad Radja Rivaldi", "Ilmu Komputer"),
    Mahasiswa("I.2410207", "Nazwa Hafizah Tanjung", "Ilmu Komputer"),
    Mahasiswa("I.2410022", "Said Amir Ismail", "Ilmu Komputer"),
    Mahasiswa("I.2410127", "Annisa", "Ilmu Komputer"),
    Mahasiswa("I.2410605", "Mohamad Isa Bagus", "Ilmu Komputer"),
    Mahasiswa("I.2410162", "Luqman", "Ilmu Komputer"),
    Mahasiswa("I.2410034", "Paisal Nugraha", "Ilmu Komputer"),
    Mahasiswa("I.2410147", "Muhammad Tangguh Haikal A.W", "Ilmu Komputer"),
]

# Inisialisasi Hash Table
hash_table = HashTable(10)
for mhs in mahasiswa_data:
    hash_table.insert(mhs)

# Menu Pilihan Pencarian
while True:
    print("\nMenu Pencarian:")
    print("1. Cari berdasarkan NIM")
    print("2. Cari berdasarkan Nama")
    print("3. Tampilkan semua data (urut berdasarkan nama)")
    print("4. Keluar")
    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == "1":
        nim_cari = input("Masukkan NIM untuk mencari: ")
        mahasiswa_ditemukan_nim = hash_table.search_by_nim(nim_cari)
        if mahasiswa_ditemukan_nim:
            print("Mahasiswa ditemukan berdasarkan NIM:")
            print(mahasiswa_ditemukan_nim)
        else:
            print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
    elif pilihan == "2":
        nama_cari = input("Masukkan Nama untuk mencari: ")
        mahasiswa_ditemukan_nama = hash_table.search_by_name(nama_cari)
        if mahasiswa_ditemukan_nama:
            print("Mahasiswa ditemukan berdasarkan Nama:")
            print(mahasiswa_ditemukan_nama)
        else:
            print("Mahasiswa dengan Nama tersebut tidak ditemukan.")
    elif pilihan == "3":
        print("\nData Mahasiswa yang diurutkan berdasarkan nama:")
        sorted_mahasiswa = sort_mahasiswa_by_name(mahasiswa_data)
        for mhs in sorted_mahasiswa:
            print(mhs)
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
