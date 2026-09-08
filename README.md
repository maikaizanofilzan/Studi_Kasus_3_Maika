Studi_Kasus_3_Maika

Dalam program ini, ada dua tipe data utama yang dipakai:
- Tuple (daftar_buku) Dipakai buat nampung daftar buku perpustakaan. Sifatnya immutable (tetap/gak bisa diubah), jadi cocok buat data
 yang udah pasti.
- List (pinjaman) Dipakai buat nampung buku yang dipinjam. Sifatnya mutable (dinamis), jadi kita bisa bebas nambah atau hapus buku di dalamnya.

Cara Kerja Program:
1. Pas pertama kali dijalankan, program bakal langsung nampilin daftar buku yang ada di perpustakaan.
2. Abis itu masuk ke perulangan while buat nampilin menu interaktif:
   - Pilih 1 (Pinjam Buku): Program bakal ngecek judul buku yang diinput. Kalau bukunya ada di daftar_buku, otomatis masuk ke list pinjaman pakai perintah .append(). Kalau gak ada, bakal muncul pesan kalau buku gak tersedia.
   - Pilih 2 (Hapus Pinjaman): Digunakan buat ngapus buku yang gak jadi dipinjam dari list pinjaman pakai perintah .remove().
   - Pilih 3 (Lihat Daftar Buku): Buat nampilin ulang katalog buku perpustakaan.
   - Pilih 4 (Selesai): Keluar dari menu utama.
3. Di bagian akhir (setelah keluar dari menu), program bakal nampilin ringkasan semua buku yang berhasil dipinjam.
Berikut bukti tampilan pas programnya dijalankan:



