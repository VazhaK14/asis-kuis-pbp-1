## MVT

Buatlah model `Projects` dengan ketentuan berikut:

1. `Projects` menggunakan field `id` yang bertipe uuidv4 sebagai primary key dan tidak bisa diedit
2. Mempunyai field `title` bertipe `CharField` dengan panjang maksimal 255 characters
3. Mempunyai field `description` yang tidak memiliki batas panjang maksimal
4. Mempunyai field `url` ke link projectnya dan wajib diisi
5. Mempunyai field `thumbnail` yang tidak wajib diisi
6. Mempunyai field `stars` yang merupakan bilangan integer positif dengan nilai default 0
7. Mempunyai property `is_popular` yang akan bernilai true jika jumblah stars > 50
8. Mempunyai fungsi `increment_stars` untuk menambah starsnya


Gunakan template berikut, pastikan bahwa projects ditaruh di halaman yang berbeda dari landing page dan dapat diakses melalui navbar