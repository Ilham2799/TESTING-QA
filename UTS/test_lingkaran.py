import lingkaran
import math  # Import the math module

# Unit Test
def test_hitung_keliling_lingkaran():
    # Kasus uji positif
    assert lingkaran.hitung_keliling_lingkaran(0) == 0.0
    assert lingkaran.hitung_keliling_lingkaran(1) == 2 * math.pi
    assert lingkaran.hitung_keliling_lingkaran(5) == 10 * math.pi

    # Kasus uji negatif
    try:
        lingkaran.hitung_keliling_lingkaran(-1)
    except ValueError as e:
        assert str(e) == "Jari-jari lingkaran tidak boleh negatif"

if __name__ == '__main__':
    # Jalankan unit test
    test_hitung_keliling_lingkaran()
    print("Semua tes berhasil dilewati.")
