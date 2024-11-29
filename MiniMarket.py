def tampilkan_menu():
    print("\n=== Sistem Kasir Mini Market ===")
    print("1. Atur Data Pelanggan")
    print("2. Tambah Barang")
    print("3. Lihat Daftar Barang")
    print("4. Update Barang")
    print("5. Hapus Barang")
    print("6. Hitung Total Belanja")
    print("7. Bayar")
    print("0. Keluar")


def tambah_barang(daftar_barang):
    nama = input("\nMasukkan nama barang: ")
    for barang in daftar_barang:
        if barang['nama'].lower() == nama.lower():
            print(f"Barang '{nama}' sudah ada. Gunakan opsi Update Barang.")
            return
    harga = int(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))
    daftar_barang.append({"nama": nama, "harga": harga, "jumlah": jumlah})
    print(f"Barang '{nama}' berhasil ditambahkan.")


def update_barang(daftar_barang):
    nama = input("\nMasukkan nama barang yang akan diupdate: ")
    for barang in daftar_barang:
        if barang['nama'].lower() == nama.lower():
            print(f"Barang '{nama}' ditemukan. Harga: Rp{barang['harga']}, Jumlah: {barang['jumlah']}")
            barang['harga'] = int(input("Masukkan harga baru: "))
            barang['jumlah'] = int(input("Masukkan jumlah baru: "))
            print(f"Barang '{nama}' berhasil diperbarui.")
            return
    print(f"Barang '{nama}' tidak ditemukan.")


def lihat_daftar_barang(daftar_barang):
    if not daftar_barang:
        print("\nTidak ada barang.")
        return
    print("\n=== Daftar Barang ===")
    for i, barang in enumerate(daftar_barang, start=1):
        print(f"{i}. {barang['nama']} - Rp{barang['harga']} x {barang['jumlah']} = Rp{barang['harga'] * barang['jumlah']}")


def hapus_barang(daftar_barang):
    lihat_daftar_barang(daftar_barang)
    if not daftar_barang:
        return
    indeks = int(input("Masukkan nomor barang yang akan dihapus: ")) - 1
    if 0 <= indeks < len(daftar_barang):
        barang = daftar_barang.pop(indeks)
        print(f"Barang '{barang['nama']}' berhasil dihapus.")
    else:
        print("Nomor barang tidak valid.")


def hitung_total(daftar_barang):
    total = sum(barang['harga'] * barang['jumlah'] for barang in daftar_barang)
    print(f"\nTotal belanja: Rp{total}")
    return total


def cetak_struk(daftar_barang, total, pelanggan):
    print("\n=== Struk Pembelian ===")
    print(f"Pelanggan ke: {pelanggan['id'] if pelanggan['id'] else 'Tidak diketahui'}")
    print("=====================================")
    for barang in daftar_barang:
        print(f"{barang['nama']} - Rp{barang['harga']} x {barang['jumlah']} = Rp{barang['harga'] * barang['jumlah']}")
    print("=====================================")
    print(f"Total: Rp{total}")
    print("=====================================")
    print("Terima kasih telah berbelanja di Mini Market kami :)!\n")


def bayar(daftar_barang, pelanggan):
    total = hitung_total(daftar_barang)
    if total == 0:
        print("Tidak ada barang untuk dibayar.")
        return

    # Member diskon berdasarkan level pelanggan
    diskon = 0
    if pelanggan['level_member'] == "Silver":
        diskon = 0.05 * total
    elif pelanggan['level_member'] == "Gold":
        diskon = 0.10 * total

    if diskon > 0:
        print(f"Diskon member ({pelanggan['level_member']}): Rp{diskon}")
        total -= diskon
        print(f"Total setelah diskon: Rp{total}")

    uang = int(input("Masukkan jumlah uang: "))
    if uang < total:
        print("Uang tidak cukup.")
    else:
        print(f"Pembayaran berhasil! Kembalian: Rp{uang - total}")
        cetak_struk(daftar_barang, total, pelanggan)
        daftar_barang.clear()
 

def atur_pelanggan(pelanggan):
    print("\n=== Atur Data Pelanggan ===")
    pelanggan['id'] = input("Pelanggan ke: ")
    print("Pilih Level Member:")
    print("1. Silver (Diskon 5%)")
    print("2. Gold (Diskon 10%)")
    print("3. Tidak ada")
    pilihan = input("Pilih level member: ")
    if pilihan == "1":
        pelanggan['level_member'] = "Silver"
    elif pilihan == "2":
        pelanggan['level_member'] = "Gold"
    else:
        pelanggan['level_member'] = None
    print(f"Data pelanggan berhasil disimpan. Level member: {pelanggan['level_member']}")


def main():
    daftar_barang = []
    pelanggan = {"id": None, "nama": None, "level_member": None}
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            atur_pelanggan(pelanggan)
        elif pilihan == "2":
            tambah_barang(daftar_barang)
        elif pilihan == "3":
            lihat_daftar_barang(daftar_barang)
        elif pilihan == "4":
            update_barang(daftar_barang)
        elif pilihan == "5":
            hapus_barang(daftar_barang)
        elif pilihan == "6":
            hitung_total(daftar_barang)
        elif pilihan == "7":
            bayar(daftar_barang,pelanggan)
        elif pilihan == "0":
            print("Terima kasih telah menggunakan sistem kasir!")
            break
        else:
            print("Pilihan tidak valid.")


main()