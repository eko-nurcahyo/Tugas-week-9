class Mahasiswa:
    def __init__(self, nama, nim, prodi, nilai):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.nilai = nilai

def input_data_mahasiswa():
    mahasiswa_list = []
    while True:
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        prodi = input("Masukkan Prodi mahasiswa TI/SI: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        mahasiswa_list.append(Mahasiswa(nama, nim, prodi, nilai))
        
        lagi = input("Apakah ingin menambah data mahasiswa lagi? (yes/no): ").strip().lower()
        if lagi != 'yes':
            break
    return mahasiswa_list

def tampilkan_data_mahasiswa(mahasiswa_list):
    for mahasiswa in mahasiswa_list:
        print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Prodi: {mahasiswa.prodi}, Nilai: {mahasiswa.nilai}")

def hitung_rata_rata_nilai(mahasiswa_list):
    total_nilai = sum(mahasiswa.nilai for mahasiswa in mahasiswa_list)
    rata_rata_nilai = total_nilai / len(mahasiswa_list)
    print(f"Rata-rata Nilai: {rata_rata_nilai:.2f}")

def cari_nilai_tertinggi_terendah(mahasiswa_list):
    mahasiswa_nilai_tertinggi = max(mahasiswa_list, key=lambda m: m.nilai)
    mahasiswa_nilai_terendah = min(mahasiswa_list, key=lambda m: m.nilai)
    
    print(f"Mahasiswa dengan nilai tertinggi: {mahasiswa_nilai_tertinggi.nama} dengan nilai {mahasiswa_nilai_tertinggi.nilai}")
    print(f"Mahasiswa dengan nilai terendah: {mahasiswa_nilai_terendah.nama} dengan nilai {mahasiswa_nilai_terendah.nilai}")

def main():
    mahasiswa_list = input_data_mahasiswa()
    print("\nData Mahasiswa:")
    tampilkan_data_mahasiswa(mahasiswa_list)
    print("\nRata-rata Nilai Mahasiswa:")
    hitung_rata_rata_nilai(mahasiswa_list)
    print("\nMahasiswa dengan Nilai Tertinggi dan Terendah:")
    cari_nilai_tertinggi_terendah(mahasiswa_list)

if __name__ == "__main__":
    main()
