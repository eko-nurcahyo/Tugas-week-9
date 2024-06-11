class Transaksi:
    def __init__(self, jenis, jumlah, keterangan):
        self.jenis = jenis  # 'pemasukan' atau 'pengeluaran'
        self.jumlah = jumlah
        self.keterangan = keterangan

def input_transaksi():
    transaksi_list = []
    while True:
        jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ").strip().lower()
        jumlah = float(input("Masukkan jumlah transaksi: "))
        keterangan = input("Masukkan keterangan transaksi: ")
        transaksi_list.append(Transaksi(jenis, jumlah, keterangan))
        
        lagi = input("Apakah ingin menambah transaksi lagi? (yes/no): ").strip().lower()
        if lagi != 'yes':
            break
    return transaksi_list

def tampilkan_semua_transaksi(transaksi_list):
    if not transaksi_list:
        print("Tidak ada transaksi.")
    else:
        for transaksi in transaksi_list:
            print(f"Jenis: {transaksi.jenis.capitalize()}, Jumlah: {transaksi.jumlah}, Keterangan: {transaksi.keterangan}")

def hitung_total_pemasukan(transaksi_list):
    total_pemasukan = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.jenis == 'pemasukan')
    print(f"Total Pemasukan: {total_pemasukan}")

def hitung_total_pengeluaran(transaksi_list):
    total_pengeluaran = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.jenis == 'pengeluaran')
    print(f"Total Pengeluaran: {total_pengeluaran}")

def hitung_saldo_akhir(transaksi_list):
    total_pemasukan = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.jenis == 'pemasukan')
    total_pengeluaran = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.jenis == 'pengeluaran')
    saldo_akhir = total_pemasukan - total_pengeluaran
    print(f"Saldo Akhir: {saldo_akhir}")

def main():
    transaksi_list = []
    while True:
        print("\nMenu Pengelolaan Keuangan Pribadi:")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Semua Transaksi")
        print("3. Hitung Total Pemasukan")
        print("4. Hitung Total Pengeluaran")
        print("5. Hitung Saldo Akhir")
        print("6. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5/6): ").strip()

        if pilihan == '1':
            transaksi_list.extend(input_transaksi())
        elif pilihan == '2':
            tampilkan_semua_transaksi(transaksi_list)
        elif pilihan == '3':
            hitung_total_pemasukan(transaksi_list)
        elif pilihan == '4':
            hitung_total_pengeluaran(transaksi_list)
        elif pilihan == '5':
            hitung_saldo_akhir(transaksi_list)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
