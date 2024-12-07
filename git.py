data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen':{
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
}

print("1. Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.")
for lokasi, data in data_panen.items():
    print(f"Nama Lokasi: {data['nama_lokasi']}")
    for z, x in data['hasil_panen'].items():
        print(f"{z}: {x}")

print("2. Tampilkan jumlah hasil panen jagung dari lokasi2")
jagunglok2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung di lokasi2: {jagunglok2}")

print("3. Tampilkan nama lokasi dari lokasi3")
namalok3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {namalok3}")

print("4. Masukkan jumlah hasil panen padi dan kedelai ke dalam variabel yang berbeda")
padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']

padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']

padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']

padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']

padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']
print("Hasil panen padi dan kedelai untuk setiap lokasi:")
print(f"Kebun A: Padi = {padi_lokasi1}, Kedelai = {kedelai_lokasi1}")
print(f"Kebun B: Padi = {padi_lokasi2}, Kedelai = {kedelai_lokasi2}")
print(f"Kebun C: Padi = {padi_lokasi3}, Kedelai = {kedelai_lokasi3}")
print(f"Kebun D: Padi = {padi_lokasi4}, Kedelai = {kedelai_lokasi4}")
print(f"Kebun E: Padi = {padi_lokasi5}, Kedelai = {kedelai_lokasi5}")

print("5. Percabangan untuk memeriksa kondisi lokasi")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {data['nama_lokasi']} dalam kondisi baik.")