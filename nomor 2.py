hitung_luas = int(input("""pilih salah satu :
    1. Hitunglah persgi
    2. Hitunglah lingkaran
    3. Hitunglah segitiga
"""))

match hitung_luas :
    case 1:
        print('menghitung luas persegi')
        sisi = int(input('masukkan sisi :'))
        print('luas persegi adalah :', sisi * sisi, 'cm')

    case 2:
        print('menghitung luas lingkaran')
        r = int(input('masukkan jari-jari :'))
        print('luas lingkaran adalah :', 3.14 * r * r)
    case 3:
        print('menghitung luas segitiga')
        a = int(input('masukkan alas : '))
        t = int(input('masukkan tinggi : '))
        print('luas segitiga adalah :', 0.5 * a * t)
    case _:
        print('pilihan tidak valid')