# myportofolio

Proyek referensi mata kuliah Pemrograman Berbasis Platform (PBP) untuk Tutorial dan Individual Assignment mingguan (Proyek Individu - website portofolio pribadi). Repositori ini dipakai bersama oleh tim asisten dosen sebagai acuan saat menyusun materi Tutorial/Tugas minggu berikutnya.

## Struktur branch

Ada dua jalur branch yang berjalan paralel:

- **Jalur Tutorial** (baseline wajib, berurutan): `main → tutorial-1 → tutorial-2 → tutorial-3 → ...`. Tiap `tutorial-N` dibuat dari `tutorial-(N-1)` saja, tidak pernah dari branch tugas manapun, supaya jalur ini tetap konsisten sebagai pola yang diikuti tiap minggu.
- **Jalur Tugas** (per minggu, sifatnya lebih bebas/open-ended): tiap `tugas-N` dibuat dari `tutorial-N` (bukan dari `tugas-(N-1)`), karena spesifikasi tugas tidak ketat dan tidak menjadi prasyarat tutorial minggu berikutnya.

`git checkout <branch>` di titik manapun memberikan aplikasi yang lengkap dan bisa langsung dijalankan untuk minggu/tahap itu. `main` merepresentasikan hasil akhir Tutorial 0 (setup proyek).

## Menjalankan proyek

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env   # isi PRODUCTION=False untuk development lokal
python manage.py migrate
python manage.py runserver
```

## Menambah Tutorial/Tugas baru

Kalau menyusun materi untuk minggu berikutnya:

1. Buat branch `tutorial-N` dari `tutorial-(N-1)`, lanjutkan kode di branch itu sesuai topik minggu itu.
2. Buat branch `tugas-N` dari `tutorial-N` (branch yang baru dibuat di atas), untuk versi Individual Assignment minggu itu.
3. Halaman dokumentasi Tutorial/Tugas yang berpasangan ada di repositori `website-quarto` (`tutorial/tutorial-N.qmd` dan `assignments/individual/tugas-N.qmd`), pakai template di `_templates/` pada repositori itu.
