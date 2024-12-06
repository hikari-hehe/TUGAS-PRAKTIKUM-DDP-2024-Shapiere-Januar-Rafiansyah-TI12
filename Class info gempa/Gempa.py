class Gempa :
    # Konstruktor inisialisasi atribut lokassi dan skala
    def __init__(self, lokasi, skala):
        
        # Atribut
        self.lokasi = lokasi
        self.skala = skala
# Method menentukan dampak skala gempa
    def dampak(self):

        # Statement / Logika
        if self.skala <= 2:
            print('Dampak gempa tidak berasa')
        elif self.skala >=2 and self.skala <= 4:
            print('Dampak gempa bangunan retak-retak')
        elif self.skala >4 and self.skala <= 6:
            print('Dampak gempa bangunan roboh')
        elif self.skala >6:
            print('Dampak bangunan roboh dan berpotensi tsunami')

        # Menampilkan lokassi dan Skala
        print(f'Lokasi gempa: {self.lokasi}')
        print(f'Skala gempa: {self.skala}')

    