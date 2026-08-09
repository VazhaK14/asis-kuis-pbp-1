# Personal Portofolio

Aplikasi "Personal Portfolio Website" — situs showcase proyek pribadi. Ini
adalah proyek referensi untuk Proyek Individu (dinilai per milestone) mata
kuliah Pemrograman Berbasis Platform (PBP), dibangun bertahap mengikuti
pola yang sama dengan proyek Tutorial (lihat `reelist/`), cuma beda tema.

## Struktur branch

Setiap branch `milestone-N` merepresentasikan kondisi proyek tepat setelah
milestone itu selesai. Branch-branch ini **bertumpuk** (`milestone-2`
dibuat dari `milestone-1`, dst.), jadi `git checkout milestone-N` di titik
manapun akan memberikan aplikasi yang lengkap dan bisa langsung dijalankan
untuk milestone itu.

Lihat `NOTES.md` untuk catatan apa yang dikerjakan di setiap milestone dan
tutorial minggu mana yang mengajarkan pola yang sama.

## Menjalankan proyek

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
