class Barang:
    def __init__(self, nama, harga, jumlah=1):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

class Keranjang:
    def __init__(self):
        self.barang = []

    def tambah_barang(self, barang):
        self.barang.append(barang)

    def hapus_barang(self, nama_barang):
        for i, barang in enumerate(self.barang):
            if barang.nama == nama_barang:
                self.barang.pop(i)
                break

    def total_harga(self):
        total = 0
        for barang in self.barang:
            total += barang.harga * barang.jumlah
        return total

    def cetak_struk(self):
        print("Struk:")
        for barang in self.barang:
            print(f"{barang.jumlah} x {barang.nama}: Rp {barang.harga * barang.jumlah}")
        print(f"Total Harga: Rp {self.total_harga()}")

def main():
    keranjang = Keranjang()

    while True:
        print("\n1. Tambah Barang")
        print("2. Lihat Keranjang")
        print("3. Hitung Total")
        print("4. Cetak Struk")
        print("5. Keluar")

        pilihan = int(input("Masukkan pilihan Anda: "))

        if pilihan == 1:
            nama = input("Masukkan nama barang: ")
            harga = float(input("Masukkan harga barang: "))
            jumlah = int(input("Masukkan jumlah barang: "))
            barang = Barang(nama, harga, jumlah)
            keranjang.tambah_barang(barang)
            print("Barang telah ditambahkan ke keranjang.")

        elif pilihan == 2:
            print("Keranjang:")
            for barang in keranjang.barang:
                print(f"{barang.jumlah} x {barang.nama}: Rp {barang.harga}")

        elif pilihan == 3:
            total_harga = keranjang.total_harga()
            print(f"Total Harga: Rp {total_harga}")

        elif pilihan == 4:
            keranjang.cetak_struk()

        elif pilihan == 5:
            print("Keluar...")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
