from tabulate import tabulate
# Database Jamaah
database = {
    "Jama'ah 1": {"Nama": "Amin Angkasa", "NIK": 111, "Umur": 35, "Gender": "Pria", "Paket": "Paket Bronze", "Pelunasan": "Lunas", "Status": "Siap Berangkat"},
    "Jama'ah 2": {"Nama": "Bagas Bagaskara", "NIK": 222, "Umur": 38, "Gender": "Pria", "Paket": "Paket Silver", "Pelunasan": "Lunas", "Status": "Siap Berangkat"},
    "Jama'ah 3": {"Nama": "Cania Citta", "NIK": 333, "Umur": 29, "Gender": "Perempuan", "Paket": "Paket Gold", "Pelunasan": "Belum Lunas", "Status": "Belum Siap Berangkat"},
    "Jama'ah 4": {"Nama": "Danila Darmawongso", "NIK": 444, "Umur": 35, "Gender": "Perempuan", "Paket": "Paket Silver", "Pelunasan": "Lunas", "Status": "Siap Berangkat"},
    "Jama'ah 5": {"Nama": "Erlangga Emir", "NIK": 555, "Umur": 26, "Gender": "Pria", "Paket": "Paket UmTour Lite", "Pelunasan": "Belum Lunas", "Status": "Belum Siap Berangkat"},
    "Jama'ah 6": {"Nama": "FFadhil Fatahilah", "NIK": 666, "Umur": 45, "Gender": "Pria", "Paket": "Paket Gold", "Pelunasan": "Lunas", "Status": "Siap Berangkat"},
    "Jama'ah 7": {"Nama": "Gilang Ghazali", "NIK": 777, "Umur": 33, "Gender": "Pria", "Paket": "Paket Bronze", "Pelunasan": "Lunas", "Status": "Siap Berangkat"},
}
paket_umroh = {
    "Paket Bronze" : {"Durasi (Hari)" : 7 , "Penginapan" : "Hotel Bintang 3", "Opsi Tour" : "Tidak Ada", "Biaya" :20000000},
    "Paket Silver" : {"Durasi (Hari)" : 9 , "Penginapan" : "Hotel Bintang 4", "Opsi Tour" : "Tidak Ada", "Biaya" :25000000},
    "Paket Gold" : {"Durasi (Hari)" : 12 , "Penginapan" : "Hotel Bintang 5", "Opsi Tour" : "Tidak Ada", "Biaya" : 30000000},
    "Paket UmTour Lite" : {"Durasi (Hari)" : 14 , "Penginapan" : "Hotel Bintang 5", "Opsi Tour" : "Ada", "Biaya" : 40000000},
    "Paket UmTour Gold" : {"Durasi (Hari)" : 16 , "Penginapan" : "Hotel Bintang 5", "Opsi Tour" : "Ada", "Biaya" : 50000000}
}
# database[id_input] = {'nama': nama_input, 'NIK': nik_input, }

# Database 
id_pw_admin = {
    "admin" : "admin",
    "admin1" : "admin1"
}
def tabel_data():
    tabel_database = []
    for key, val in database.items():
        tabel_database.append([key, val["Nama"], val["NIK"], val["Umur"], val["Gender"], val["Paket"], val["Pelunasan"], val["Status"]])
    return tabulate(tabel_database, headers=["Jama'ah", "Nama", "NIK", "Umur", "Gender", "Paket", "Pelunasan", "Status"], tablefmt="fancy_grid")

def tabel_paket_umroh():
    tabel_paket = []
    for key, val in paket_umroh.items():
        tabel_paket.append([key, val["Durasi (Hari)"], val["Penginapan"], val["Opsi Tour"], val["Biaya"]])
    return tabulate(tabel_paket, headers=["Durasi (Hari)", "Penginapan", "Opsi Tour", "Biaya"], tablefmt="fancy_grid")
    
def tampilkan_data_nik(nik):
    if nik in database:
        data_nik = database[nik]
        return tabulate([[data_nik["NIK"], data_nik["Nama"], data_nik["Umur"], data_nik["Gender"], data_nik["Paket"], data_nik["Pelunasan"], data_nik["Status"]]], headers=["NIK", "Nama", "Umur", "Gender", "Paket", "Pelunasan", "Status"], tablefmt="fancy_grid")
    else :
        return "Data tidak ditemukan."
    
def main_menu():
    return '''
Selamat Datang di Travel Ramadhyan

List Menu:
1. Masuk Sebagai Admin
2. Exit Program
'''

def menu_admin():
    return '''Menu :
1. Tampilkan Data
2. Tambahkan Data
3. Edit Data
4. Hapus Data
5. Kembali ke main menu
'''

def admin_tampilin_data():
    return '''
1. Tampilkan Data Seluruh Jama'ah
2. Tampilkan Data seluruh Jama'ah Berdasarkan kata kunci
3. Sorting Data Jamaah Berdasaarkan Umur, Nama, dan Gender
4. Tampilkan Paket Umroh yang Tersedia
5. Tampilkan Paket Umroh yang Tersedia Berdasarkan kata kunci
6. Kembali ke Menu Awal
'''

def cari_data_menggunakan_kata_kunci():
    return'''
1. Cari data menggunakan Primary Key(NIK)
2. Cari data menggunakan kata kunci
3. Kembali ke menu sebelumnya
'''
def cari_jamaah_nik(NIK):
    for key, val in database.items():
            if val["NIK"] == NIK: 
                # Cocokkan NIK secara penuh
                return tabulate([[val["Nama"], val["NIK"], val["Umur"], val["Gender"], val["Paket"], val["Pelunasan"], val["Status"]]],
                                headers=["Nama", "NIK", "Umur", "Gender", "Paket", "Pelunasan", "Status"], tablefmt="fancy_grid")
    return "Data dengan NIK tersebut tidak ditemukan."

# Fungsi untuk sorting data jamaah berdasarkan umur
def sort_jamaah_umur(ascending=True):
    sorted_data = sorted(database.items(), key=lambda x: x[1]["Umur"], reverse=not ascending)
    hasil_sorting = []
    for key, val in sorted_data:
        hasil_sorting.append([val["Nama"], val["NIK"], val["Umur"], val["Gender"], val["Paket"], val["Pelunasan"], val["Status"]])
    return tabulate(hasil_sorting, headers=["Nama", "NIK", "Umur", "Gender", "Paket", "Pelunasan", "Status"], tablefmt="fancy_grid")

# Fungsi untuk sorting data jamaah berdasarkan nama (alfabetis)
def sort_jamaah_nama():
    sorted_data = sorted(database.items(), key=lambda x: x[1]["Nama"])
    hasil_sorting = []
    for key, val in sorted_data:
        hasil_sorting.append([val["Nama"], val["NIK"], val["Umur"], val["Gender"], val["Paket"], val["Pelunasan"], val["Status"]])
    return tabulate(hasil_sorting, headers=["Nama", "NIK", "Umur", "Gender", "Paket", "Pelunasan", "Status"], tablefmt="fancy_grid")

# Fungsi untuk filter data jamaah berdasarkan gender
def filter_jamaah_gender(gender):
    filtered_data = [val for key, val in database.items() if val["Gender"].lower() == gender.lower()]
    hasil_filter = []
    for val in filtered_data:
        hasil_filter.append([val["Nama"], val["NIK"], val["Umur"], val["Gender"], val["Paket"], val["Pelunasan"], val["Status"]])
    if hasil_filter:
        return tabulate(hasil_filter, headers=["Nama", "NIK", "Umur", "Gender", "Paket", "Pelunasan", "Status"], tablefmt="fancy_grid")
    else:
        return f"Tidak ada jamaah dengan gender {gender}."

def cari_paket_berdasarkan_kata_kunci(kata_kunci):
    hasil_pencarian = []

    # Loop untuk mencari kata kunci di setiap field dalam paket_umroh
    for key, val in paket_umroh.items():
        if (kata_kunci.lower() in key.lower() or
            kata_kunci.lower() in str(val["Durasi (Hari)"]).lower() or
            kata_kunci.lower() in val["Penginapan"].lower() or
            kata_kunci.lower() in val["Opsi Tour"].lower() or
            kata_kunci.lower() in str(val["Biaya"]).lower()):
            
            # Jika cocok, tambahkan ke hasil pencarian
            hasil_pencarian.append([key, val["Durasi (Hari)"], val["Penginapan"], val["Opsi Tour"], val["Biaya"]])
    
    if hasil_pencarian:
        return tabulate(hasil_pencarian, headers=["Paket", "Durasi (Hari)", "Penginapan", "Opsi Tour", "Biaya"], tablefmt="fancy_grid")
    else:
        return "Tidak ada paket umroh yang cocok dengan kata kunci tersebut."

## ===================================================================================
## Cari data jamaah menggunakan kata kunci
## ===================================================================================

def cari_jamaah_berdasarkan_kata_kunci(kata_kunci):
    hasil_pencarian = []
    
    # Loop untuk mencari kata kunci di setiap field dalam database
    for key, val in database.items():
        # Cek jika kata kunci ada di salah satu field
        if (kata_kunci.lower() in str(val["Nama"]).lower() or
            kata_kunci.lower() in str(val["NIK"]).lower() or
            kata_kunci.lower() in str(val["Umur"]).lower() or
            kata_kunci.lower() in str(val["Gender"]).lower() or
            kata_kunci.lower() in str(val["Paket"]).lower() or
            kata_kunci.lower() in str(val["Pelunasan"]).lower() or
            kata_kunci.lower() in str(val["Status"]).lower()):
            
            # Jika cocok, tambahkan ke hasil pencarian
            hasil_pencarian.append([val["Nama"], val["NIK"], val["Umur"], val["Gender"], val["Paket"], val["Pelunasan"], val["Status"]])
    
    if hasil_pencarian:
        return tabulate(hasil_pencarian, headers=["Nama", "NIK", "Umur", "Gender", "Paket", "Pelunasan", "Status"], tablefmt="fancy_grid")
    else:
        return "Tidak ada data yang cocok dengan kata kunci tersebut."

def admin_tambah_data():
    return'''
1. Tambahkan Data Jama'ah
2. Tambahkan Paket Umroh
3. Kembali ke Menu Awal
'''
## ===================================================================================
# Fungsi untuk menambahkan jamaah baru
## ===================================================================================

def tambah_jamaah():
    # Input Primary Key
    while True:
        try:
            nik = int(input("Masukkan NIK: "))
            break
        except:
            print("Data NIK hanya bisa berupa integer/angka")
    
    # Cek jika NIK sudah ada
    if nik in [data["NIK"] for data in database.values()]:
        print("NIK sudah ada. Jamaah tidak dapat ditambahkan.")
        return False  # Mengembalikan False untuk menandakan proses gagal dan kembali ke menu
    
    nama = input("Masukkn Nama Jama'ah: ").title()
    while True:
        try:
            umur = int(input("Masukkan Umur: "))
            break
        except:
            print("Data umur hanya bisa berupa integer/angka")
    
    while True:
        gender = input('''
1. Pria
2. Perempuan
    
(Pilih 1 untuk Pria, Pilih 2 untuk Perempuan)
Masukan gender Anda: ''')
        if gender == "1":
            gender = "Pria"
            break
        elif gender == "2":
            gender = "Perempuan"
            break
        else:
            print("Data gender tidak valid, coba gunakan 1 untuk gender Pria dan gunakan 2 untuk gender Perempuan")
    
    while True:
        paket = input('''
1. Paket Bronze
2. Paket Silver
3. Paket Gold
4. Paket UmTour Lite
5. Paket UmTour Gold                     
    
Masukkan Paket Anda: ''')
        if paket == "1":
            paket = "Paket Bronze"
            break
        elif paket == "2":
            paket = "Paket Silver"
            break
        elif paket == "3":
            paket = "Paket Gold"
            break
        elif paket == "4":
            paket = "Paket UmTour Lite"
            break
        elif paket == "5":
            paket = "Paket UmTour Gold"
            break
        else:
            print("Data paket tidak valid, coba gunakan 1 s/d 5")
    
    while True:
        pelunasan = input('''
1. Lunas
2. Belum Lunas
Masukkan Status Pelunasan: ''')
        if pelunasan == "1":
            pelunasan = "Lunas"
            break
        elif pelunasan == "2":
            pelunasan = "Belum Lunas"
            break
        else:
            print("Data pelunasan tidak valid, coba gunakan 1 atau 2")
    
    while True:
        status = input('''
1. Siap Berangkat
2. Belum Siap Berangkat
Masukkan Status keberangkatan: ''')
        if status == "1":
            status = "Siap Berangkat"
            break
        elif status == "2":
            status = "Belum Siap Berangkat"
            break
        else:
            print("Data status tidak valid, coba gunakan 1 atau 2")
    
    # Menampilkan data yang akan disimpan dalam bentuk tabel
    new_data = [[nama, nik, gender, umur, paket, pelunasan, status]]
    
    print("\nBerikut data yang akan dimasukkan:")
    print(tabulate(new_data, headers=["Nama", "NIK", "Gender", "Umur", "Paket", "Pelunasan", "Status"], tablefmt="fancy_grid"))
    
    # Konfirmasi simpan data
    while True:
        konfirmasi = input("\nApakah Anda yakin ingin menyimpan data ini? (y/n): ")
        if konfirmasi.lower() == "y":
            # Menyimpan data ke database
            database[f"Jama'ah {len(database) + 1}"] = {
                "NIK": nik,
                "Nama": nama,
                "Umur": umur,
                "Gender": gender,
                "Paket": paket,
                "Pelunasan": pelunasan,
                "Status": status
            }
            return True  # Menandakan bahwa proses berhasil
        elif konfirmasi.lower() == "n":
            print("Penambahan jamaah dibatalkan.")
            return False  # Menandakan bahwa proses dibatalkan
        else:
            print("Pilihan tidak valid, gunakan opsi y untuk menyimpan dan n untuk tidak menyimpan data.")

def menu_update():
    return '''Menu Update Data :
1. Nama
2. Umur
3. Gender
4. Paket
5. Pelunasan
6. Status
7. Kembali ke Menu Sebelum'''

def fungsi_sorting():
    return '''
Pilih opsi sorting:
1. Urutkan berdasarkan umur (terkecil ke terbesar)
2. Urutkan berdasarkan umur (terbesar ke terkecil)
3. Urutkan berdasarkan nama (A-Z)
4. Filter berdasarkan gender (Pria)
5. Filter berdasarkan gender (Perempuan)
6. Kembali ke menu sebelumnya
    '''
#Fungsi Read
def read():
    while True:
        print(admin_tampilin_data())
        opsi_admin_1 = input("Pilih opsi yang anda inginkan : ")

        # Opsi untuk melihat data jamaah
        if opsi_admin_1 == "1":
            if len(database) == 0:
                print("Tidak ada data tersimpan di database")
            else:
                print(tabel_data())

        # Opsi untuk mencari data jamaah
        elif opsi_admin_1 == "2":
            print(cari_data_menggunakan_kata_kunci())
            opsi_admin_1_2_1 = input("Pilih opsi yang anda inginkan : ")

            # Pencarian berdasarkan NIK
            if opsi_admin_1_2_1 == "1":
                while True:
                    try:
                        NIK = int(input("Masukkan NIK: "))
                        print(cari_jamaah_nik(NIK))
                    except ValueError:
                        print("Data NIK harus berupa integer. Tolong masukkan data integer.")

                    kembali = input("Apakah anda ingin mencari data menggunakan NIK lagi? [y/n] ").lower()
                    if kembali == "n":
                        break
                    elif kembali != "y":
                        print("Ketik 'y' untuk melanjutkan pencarian atau 'n' untuk berhenti.")

            # Pencarian berdasarkan kata kunci
            elif opsi_admin_1_2_1 == "2":
                while True:
                    kata_kunci = input("Masukan kata kunci yang anda inginkan : ")
                    print(cari_jamaah_berdasarkan_kata_kunci(kata_kunci))

                    kembali = input("Apakah anda ingin mencari data menggunakan kata kunci lagi? [y/n] ").lower()
                    if kembali == "n":
                        break
                    elif kembali != "y":
                        print("Ketik 'y' untuk melanjutkan pencarian atau 'n' untuk berhenti.")

        # Opsi untuk sortir data jamaah
        elif opsi_admin_1 == "3":
            while True:
                print(fungsi_sorting())

                opsi_sorting = input("Pilih opsi sorting yang Anda inginkan: ")

                if opsi_sorting == "1":
                    print("\nData Jamaah berdasarkan umur (terkecil ke terbesar):")
                    print(sort_jamaah_umur(ascending=True))
                elif opsi_sorting == "2":
                    print("\nData Jamaah berdasarkan umur (terbesar ke terkecil):")
                    print(sort_jamaah_umur(ascending=False))
                elif opsi_sorting == "3":
                    print("\nData Jamaah berdasarkan nama (A-Z):")
                    print(sort_jamaah_nama())
                elif opsi_sorting == "4":
                    print("\nData Jamaah berdasarkan gender (Pria):")
                    print(filter_jamaah_gender("Pria"))
                elif opsi_sorting == "5":
                    print("\nData Jamaah berdasarkan gender (Perempuan):")
                    print(filter_jamaah_gender("Perempuan"))
                elif opsi_sorting == "6":
                    break  # Kembali ke menu sebelumnya
                else:
                    print("Opsi tidak valid, silakan coba lagi.")
                
                # Tanyakan apakah ingin kembali ke menu sorting
                kembali = input("\nApakah Anda ingin kembali ke menu sorting? [y/n]: ").lower()
                if kembali == 'n':
                    break

        # Opsi untuk melihat data paket umroh
        elif opsi_admin_1 == "4":
            if len(paket_umroh) == 0:
                print("Tidak ada data paket umroh yang tersimpan di database")
            else:
                print(tabel_paket_umroh())

        # Opsi untuk mencari paket umroh
        elif opsi_admin_1 == "5":
            while True:
                kata_kunci_paket = input("Masukkan kata kunci untuk mencari paket umroh: ")
                print(cari_paket_berdasarkan_kata_kunci(kata_kunci_paket))

                kembali_paket = input("Apakah Anda ingin mencari paket umroh lagi? [y/n]: ").lower()
                if kembali_paket == "n":
                    break
                elif kembali_paket != "y":
                    print("Ketik 'y' untuk melanjutkan pencarian dan 'n' untuk berhenti.")

        # Opsi untuk keluar
        elif opsi_admin_1 == "6":
            return  # Mengakhiri fungsi jika pengguna memilih untuk keluar
        
#Fungsi Tambah Paket Umroh
def tambah_paket_umroh():
    # Input nama paket
    nama_paket = input("Masukkan Nama Paket: ")

    # Input durasi paket
    while True:
        try:
            durasi = int(input("Masukkan Durasi (Hari): "))
            break
        except:
            print("Durasi harus berupa angka.")
    
    # Input penginapan
    penginapan = input("Masukkan Tipe Penginapan (contoh: Hotel Bintang 5): ")

    # Input opsi tour
    opsi_tour = input("Masukkan Opsi Tour (Ada/Tidak Ada): ")

    # Input biaya
    while True:
        try:
            biaya = int(input("Masukkan Biaya Paket: "))
            break
        except:
            print("Biaya harus berupa angka.")

    # Tampilkan data yang akan ditambahkan dalam bentuk tabel
    new_paket = [[nama_paket, durasi, penginapan, opsi_tour, biaya]]
    print("\nBerikut paket umroh yang akan ditambahkan:")
    print(tabulate(new_paket, headers=["Nama Paket", "Durasi (Hari)", "Penginapan", "Opsi Tour", "Biaya"], tablefmt="fancy_grid"))

    # Konfirmasi simpan data
    while True:
        konfirmasi = input("\nApakah Anda yakin ingin menyimpan paket umroh ini? (y/n): ")
        if konfirmasi.lower() == "y":
            # Menyimpan data ke paket_umroh
            paket_umroh[nama_paket] = {
                "Durasi (Hari)": durasi,
                "Penginapan": penginapan,
                "Opsi Tour": opsi_tour,
                "Biaya": biaya
            }
            return True  # Proses berhasil
        elif konfirmasi.lower() == "n":
            print("Penambahan paket umroh dibatalkan.")
            return False  # Proses dibatalkan
        else:
            print("Pilihan tidak valid, gunakan opsi y untuk menyimpan dan n untuk tidak menyimpan data.")

# Fungsi Create
def create():
    while True:
        print(admin_tambah_data())
        opsi_tambah = input("Pilih opsi untuk menambah jamaah : ")
        
        if opsi_tambah == "1":
            if tambah_jamaah() is False:
                continue  # Kembali ke menu jika NIK duplikat
            else:
                print("Jamaah berhasil ditambahkan.")
        
        elif opsi_tambah == "2":
            if tambah_paket_umroh() is False:
                continue  # Kembali ke menu jika proses dibatalkan
            else:
                print("Paket umroh berhasil ditambahkan.")
        
        elif opsi_tambah == "3":
            break  # Kembali ke menu utama
        
        else:
            print("Opsi tidak valid.")

# Fungsi Update
def update():
    while True:
        nik = int(input("Masukkan NIK jamaah yang ingin diupdate: "))
        # Cek apakah NIK ada dalam database
        if nik in [data["NIK"] for data in database.values()]:
            print("Data yang ada saat ini:")
            print(cari_jamaah_nik(nik))  # Menampilkan data saat ini

            # Memilih apa yang ingin diupdate
            while True:
                print(menu_update())
                opsi_update = input("Pilih opsi yang ingin diupdate: ")
                
                if opsi_update == "1":  # Update Nama
                    nama_baru = input("Masukkan Nama Baru: ").title()
                    for key, val in database.items():
                        if val["NIK"] == nik:
                            val["Nama"] = nama_baru
                            print("Nama berhasil diupdate.")
                            break
                            
                elif opsi_update == "2":  # Update Umur
                    while True:
                        try:
                            umur_baru = int(input("Masukkan Umur Baru: "))
                            for key, val in database.items():
                                if val["NIK"] == nik:
                                    val["Umur"] = umur_baru
                                    print("Umur berhasil diupdate.")
                                    break
                            break
                        except ValueError:
                            print("Umur harus berupa angka.")

                
                
                elif opsi_update == "3":  # Update Gender
                    gender_baru = input('''Masukkan Gender Baru (Pria/Perempuan): ''')
                    for key, val in database.items():
                        if val["NIK"] == nik:
                            val["Gender"] = gender_baru
                            print("Gender berhasil diupdate.")
                            break
                    
                elif opsi_update == "4":  # Update Paket
                    paket_baru = input('''Masukkan Paket Baru (Paket Bronze/Silver/Gold/UmTour Lite/UmTour Gold): ''')
                    for key, val in database.items():
                        if val["NIK"] == nik:
                            val["Paket"] = paket_baru
                            print("Paket berhasil diupdate.")
                            break

                elif opsi_update == "5":  # Update Pelunasan
                    pelunasan = input('''Masukkan Status Pelunasan(Lunas/Belum Lunas): ''')
                    for key, val in database.items():
                        if val["NIK"] == nik:
                            val["Pelunasan"] = pelunasan
                            print("Pelunasan berhasil diupdate.")
                            break



                elif opsi_update == "6":  # Update Status
                    status = input('''Masukkan Status (Siap Berangkat / Belum Siap Berangkat): ''')
                    for key, val in database.items():
                        if val["NIK"] == int(nik):
                            val["Status"] = status
                            print("Status berhasil diupdate.")
                            break
                
                elif opsi_update == "7":  # Kembali ke Menu Sebelumnya
                    break
                
                else:
                    print("Opsi tidak valid, silakan coba lagi.")
        
        else:
            print("NIK tidak ditemukan.")
        
        # Tanyakan apakah ingin mengupdate data lain
        lanjut = input("Apakah Anda ingin mengupdate data jamaah lain? [y/n]: ").lower()
        if lanjut == "n":
            break

# Fungsi Delete
def delete():
    while True:
        print('''Menu Hapus Data:
1. Hapus Data Jama'ah berdasarkan NIK
2. Hapus Semua Data Jama'ah
3. Kembali ke Menu Sebelumnya
''')
        pilihan_hapus = input("Pilih opsi yang anda inginkan: ")

        if pilihan_hapus == "1":  # Hapus berdasarkan NIK
            nik_hapus = int(input("Masukkan NIK jamaah yang ingin dihapus: "))
            if nik_hapus in [data["NIK"] for data in database.values()]:
                # Menampilkan data yang akan dihapus untuk konfirmasi
                for key, val in database.items():
                    if val["NIK"] == nik_hapus:
                        print(f"Data yang akan dihapus: {val}")
                        konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
                        if konfirmasi.lower() == "y":
                            del database[key]  # Menghapus data jamaah
                            print("Data jamaah berhasil dihapus.")
                        else:
                            print("Penghapusan data dibatalkan.")
                        break
            else:
                print("NIK tidak ditemukan.")
        
        elif pilihan_hapus == "2":  # Hapus Semua Data
            konfirmasi = input("Apakah Anda yakin ingin menghapus semua data? (y/n): ")
            if konfirmasi.lower() == "y":
                print("Semua data jamaah akan dihapus.")
                konfirmasi_lagi = input("Apakah Anda yakin? (y/n): ")
                if konfirmasi_lagi.lower() == "y":
                    database.clear()  # Menghapus semua data
                    print("Semua data jamaah berhasil dihapus.")
                else:
                    print("Penghapusan data dibatalkan.")
            else:
                print("Penghapusan data dibatalkan.")
        
        elif pilihan_hapus == "3":  # Kembali ke Menu Sebelumnya
            break
        
        else:
            print("Opsi tidak valid, silakan coba lagi.")

# Fungsi Utama
while True:
    print(main_menu())
    kode = input("Pilih opsi yang anda inginkan: ")

    if kode in ["1", "2"]:
        print(f"\nAnda memilih opsi {kode}.\n")
    else:
        print("\nMaaf, opsi yang anda pilih tidak tersedia... Coba gunakan opsi ( 1 / 2 )\n")
        # konfirmasi mau jalanin program lagi atau tidak
        coba_lagi = input("Apakah anda ingin mencoba kembali? [y/n]: ")
        if coba_lagi != 'y':
            print("\nProgram dihentikan. Terima kasih!\n")
            break
        continue
    if kode == "1":
        while True:
            id = input("Masukan ID admin: ")
            pw = input("Masukan Password admin: ")
            if id in id_pw_admin and pw == id_pw_admin[id]:
                print(f"Selamat datang kembali, admin !")
                while True: 
                    print(menu_admin())
                    opsi_admin = input("Pilih opsi yang anda inginkan : ")
                    if opsi_admin == "1" : # Read data
                        read()
                    elif opsi_admin =="2": # Create data
                        create()
                    elif opsi_admin =="3": # Update data
                        update()      
                    elif opsi_admin =="4": # Delete data
                        delete()
                    elif opsi_admin =="5": 
                        break
            else :
                print("ID atau Password anda salah, silahkan coba lagi")
    if kode =="2":
        print("Terima Kasih Sudah Menggunakan Program ini. ")
        break
