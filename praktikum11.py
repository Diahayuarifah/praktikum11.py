class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
    
    def get_nama(self):
        return self.nama
    
    def set_nama(self, nama):
        self.nama = nama
    
    def get_nilai(self):
        return self.nilai
    
    def set_nilai(self, nilai):
        self.nilai = nilai

# List untuk menampung objek mahasiswa
list_mhs = []

while True:
    # Tampilkan menu
    print("1. Mendeklarasikan objek")
    print("2. Menampilkan objek")
    print("3. Merubah nilai objek")
    print("4. Menghapus objek")
    print("5. Keluar dari program")
    pilihan = int(input("Masukkan pilihan Anda: "))