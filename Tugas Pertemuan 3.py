def frekuensi(jumlah_putaran, waktu):
    frekuensi = jumlah_putaran / waktu
    print(f'Frekuensi = {frekuensi} Hz')

frekuensi = frekuensi(300, 30)

def kecepatan_anguler(dua, phi, frekuensi):
    kecepatan_anguler = (dua * phi * frekuensi)
    print(f'Kecepatan Anguler = {kecepatan_anguler} rad/s')

kecepatan_anguler = kecepatan_anguler(2, 3.14, 100)

def percepatan_sentripetal(kecepatan_anguler, kecepatan_sudut, radius):
    percepatan_sentripetal = kecepatan_anguler * kecepatan_sudut * radius
    print(f'Percepatan Sentripetal = {percepatan_sentripetal} m/^2')

percepatan_sentripetal = percepatan_sentripetal(628, 628, 10)