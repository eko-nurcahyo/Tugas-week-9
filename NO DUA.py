class Barang:
    def __init__(self, nama, kode, jumlah):
        self.nama = nama
        self.kode = kode
        self.jumlah = jumlah

def input_data_barang():
    barang_list = []
    while True:
        nama = input("Masukkan nama barang: ")
        kode = input("Masukkan kode barang: ")
        jumlah = int(input("Masukkan jumlah barang: "))
        barang_list.append(Barang(nama, kode, jumlah))
        
        lagi = input("Apakah ingin menambah data barang lagi? (yes/no): ").strip().lower()
        if lagi != 'yes':
            break
    return barang_list

def tampilkan_semua_barang(barang_list):
    if not barang_list:
        print("Tidak ada data barang.")
    else:
        for barang in barang_list:
            print(f"Nama: {barang.nama}, Kode: {barang.kode}, Jumlah: {barang.jumlah}")

def cari_barang_berdasarkan_kode(barang_list, kode):
    for barang in barang_list:
        if barang.kode == kode:
            return barang
    return None

def hapus_barang_berdasarkan_kode(barang_list, kode):
    barang = cari_barang_berdasarkan_kode(barang_list, kode)
    if barang:
        barang_list.remove(barang)
        return True
    return False

def main():
    barang_list = []
    while True:
        print("\nMenu Inventaris Barang:")
        print("1. Tambah Barang")
        print("2. Tampilkan Semua Barang")
        print("3. Cari Barang Berdasarkan Kode")
        print("4. Hapus Barang Berdasarkan Kode")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ").strip()

        if pilihan == '1':
            barang_list.extend(input_data_barang())
        elif pilihan == '2':
            tampilkan_semua_barang(barang_list)
        elif pilihan == '3':
            kode = input("Masukkan kode barang yang dicari: ").strip()
            barang = cari_barang_berdasarkan_kode(barang_list, kode)
            if barang:
                print(f"Barang ditemukan: Nama: {barang.nama}, Kode: {barang.kode}, Jumlah: {barang.jumlah}")
            else:
                print("Barang tidak ditemukan.")
        elif pilihan == '4':
            kode = input("Masukkan kode barang yang akan dihapus: ").strip()
            if hapus_barang_berdasarkan_kode(barang_list, kode):
                print("Barang berhasil dihapus.")
            else:
                print("Barang tidak ditemukan.")
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
