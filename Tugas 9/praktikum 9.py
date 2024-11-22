print()
print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    konversi=(celcius*9/5)+32
    return konversi

print(celcius_ke_fahrenheit(0)) #32.0
print(celcius_ke_fahrenheit(100)) #212.0

print()
print('## Nomor 2 ##')
def ganjil_genap(bilangan):
    penentu=bilangan % 2 == 0
    return penentu

print(ganjil_genap(4)) #True
print(ganjil_genap(7)) #False

print()
print('## nomor 3 ##')
def nilai(keterangan):
    if keterangan >= 80: #Lulus
        print("Lulus")
    elif keterangan <= 60: #Gagal
        print("Gagal")
    else:                   #Tidak lulus
        print("Tidak lulus")
    
nilai(80)
nilai(60)

print()
print('## Nomor 4 ##')
def bilangan_ganjil(bilangan):
    return[i for i in range(1, bilangan, 2)]
print(bilangan_ganjil(20)) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]