def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    if jenis_kendaraan.lower() == "mobil":
        tarif = 5000
    elif jenis_kendaraan.lower() == "motor":
        tarif = 3000
    else:
        return

    total_biaya = tarif * lama_parkir
    return total_biaya

def jam_ke_menit(jam_str):
    jam, menit = map(int, jam_str.split(":"))
    return jam* 60 + menit

jenis_kendaraan = "mobil"
jam_masuk = "10:25"
jam_keluar = "15:55"

menit_masuk = jam_ke_menit(jam_masuk)
menit_keluar = jam_ke_menit(jam_keluar)
selisih_menit = menit_keluar - menit_masuk

lama_parkir = selisih_menit // 60
if selisih_menit % 60 != 0:
    lama_parkir += 1

total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

print("=== STRUK PSRKIRA ===")
print(f"jenis kendaraan : {jenis_kendaraan}")
print(f"jam masuk       : {jam_masuk}")
print(f"jam keluar      : {jam_keluar}")
print(f"lama parkir     : {lama_parkir} jam")
print(f"total biaya     :Rp{total_biaya:,}".replace(",", "."))