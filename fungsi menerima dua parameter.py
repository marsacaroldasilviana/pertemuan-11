def hitung_total_angka_yang_bisa_dibagi(daftar_angka, pemisah):
    total = 0
    for angka in daftar_angka:
        if angka % pemisah == 0:
            total += angka
    return total

# Contoh penggunaan fungsi dengan daftar angka [1, 2, 3, 4, 5] dan pemisah 2
daftar_angka_1 = [1, 2, 3, 4, 5]
pemisah_1 = 2
total_1 = hitung_total_angka_yang_bisa_dibagi(daftar_angka_1, pemisah_1)
print(f"Total angka yang bisa dibagi oleh {pemisah_1}: {total_1}")

# Contoh penggunaan fungsi dengan daftar angka [10, 15, 20, 25, 30] dan pemisah 5
daftar_angka_2 = [10, 15, 20, 25, 30]
pemisah_2 = 5
total_2 = hitung_total_angka_yang_bisa_dibagi(daftar_angka_2, pemisah_2)
print(f"Total angka yang bisa dibagi oleh {pemisah_2}: {total_2}")
