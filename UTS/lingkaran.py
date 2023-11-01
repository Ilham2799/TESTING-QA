import math

# Fungsi untuk menghitung keliling lingkaran
def hitung_keliling_lingkaran(jari_jari):
    if jari_jari < 0:
        raise ValueError("Jari-jari lingkaran tidak boleh negatif")
    return 2 * math.pi * jari_jari
