Nama   : Muhammad Ardhika Prasanjayu

NIM    : 108

Kelas  : C

Soal   : Genap

PENJELASAN

Di program, saya memakai FUNCTION hitung_biaya_parkir(jenis_kendaraaan, lama_parkir) -> ini untuk menghintung total biaya parkir berdasarkan jenis kendaraan dan lama parkir. 

Dan saya juga menggunakan percabangan atau IF-ELIF -> ini untuk menentukan tarif per jam-Rp5000 buat mobil,Rp3000 buat motor.

total_biaya = tarif * lama_parkir -> rumus utama: tarif per jam dikali lama parkir.

return total_biaya -> mengembalikan hasil perhitungan ke pemanggil function.

total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir) -> nah, kalau in memanggil function atau mengirim data jenis kendaraan dan lama parkir (hasil dari jam masuk-keluar) ke function hitunng_biaya_parkir , lalu hasilnya(return) dan ditampung di variabel total_biaya.

<img width="460" height="87" alt="Screenshot 2026-09-22 203720" src="https://github.com/user-attachments/assets/bf62be68-ab19-4f96-9393-e8be19f069aa" />

mengubah selisih menit jadi satuan jam, dengan pembulatan ke atas.
- // (floor division) -> membulatkan ke bawah dulu, dapat jumlah jam penuh.
- % (modulus/sisa bagi) -> mengecek apakah ada sisa menit; kalau ada, ditambah 1 jam (karena tempat parkir biasanya membulatkan ke atas, bukan ke bawah).

<img width="1920" height="1140" alt="Screenshot 2026-09-22 194726" src="https://github.com/user-attachments/assets/ca38055e-ae32-48d5-8a34-02ae29346b55" />
