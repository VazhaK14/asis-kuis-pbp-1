# Personal Portofolio

Aplikasi "Personal Portfolio Website" — situs portofolio pribadi. Ini
adalah proyek referensi mata kuliah Pemrograman Berbasis Platform (PBP)
untuk Tutorial dan Tugas mingguan, yang sekarang berbagi tema dan kode
yang sama (bukan dua proyek terpisah).

## Struktur branch

Ada dua jalur branch yang berjalan paralel:

- **Jalur Tutorial** (baseline wajib, berurutan): `main → tutorial-1 →
  tutorial-2 → tutorial-3 → ...`. Tiap `tutorial-N` dibuat dari
  `tutorial-(N-1)`, tidak pernah dari branch tugas manapun, supaya jalur
  ini tetap konsisten sebagai pola yang diikuti tiap minggu.
- **Jalur Tugas** (per minggu, sifatnya lebih bebas/open-ended): tiap
  `tugas-N` dibuat dari `tutorial-N` (bukan dari `tugas-(N-1)`), karena
  spesifikasi tugas tidak ketat dan tidak menjadi prasyarat tutorial
  minggu berikutnya.

`git checkout <branch>` di titik manapun akan memberikan aplikasi yang
lengkap dan bisa langsung dijalankan untuk minggu/tahap itu.

Lihat `NOTES.md` untuk catatan apa yang dikerjakan di tiap tutorial/tugas
dan hubungannya dengan topik minggu itu.

## Menjalankan proyek

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
