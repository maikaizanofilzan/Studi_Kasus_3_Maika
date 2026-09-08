daftar_buku = (
    "Basis Data",
    "Algoritma",
    "Jaringan Komputer",
    "Matematika Diskrit",
    "Analisis Sistem"
)

pinjaman = []

print("DAFTAR BUKU:")
for buku in daftar_buku:
    print("-", buku)

pilihan = ""

while pilihan != "4":
    print("\nMENU:")
    print("1. Pinjam Buku")
    print("2. Hapus Pinjaman")
    print("3. Lihat Daftar Buku")
    print("4. Selesai")
    
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        judul = input("Masukkan judul buku: ")
        if judul in daftar_buku:
            pinjaman.append(judul)
            print("buku berhasil dipinjam")
        else:
            print("buku tidak tersedia")

    elif pilihan == "2":
        if pinjaman == []:
            print("Belum ada buku yang dipinjam")
        else:
            print("Pinjaman saat ini:")
            for b in pinjaman:
                print("-", b)
            
            hapus = input("Masukkan judul yang mau dihapus: ")
            if hapus in pinjaman:
                pinjaman.remove(hapus)
                print("Buku berhasil dihapus")
            else:
                print("Buku tidak ada di daftar pinjaman")

    elif pilihan == "3":
        print("DAFTAR BUKU:")
        for buku in daftar_buku:
            print("-", buku)

    elif pilihan == "4":
        print("Proses selesai.")

    else:
        print("Pilihan salah")

print("\n-------------------------")
print(" BUKU YANG DIPINJAM:")
if pinjaman == []:
    print("Tidak ada")
else:
    for b in pinjaman:
        print("-", b)
print("-------------------------")