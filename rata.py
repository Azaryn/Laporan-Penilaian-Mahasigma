import os  # import library os untuk interaksi dengan os

# Data Kosong
list_mahasiswa = [] # list untuk inputan nama mahasiswa
list_nilaimtk = [] # list untuk nilai dari mata kuliah matematika
list_nilaietika = [] # list untuk nilai dari mata kuliah etika profesi
list_nilaipemro = [] # list untuk nilai dari mata kuliah pemrograman
list_matakuliah = ["Matematika", "Etika Profesi", "Pemrograman"] # list untuk jenis jenis mata kuliah

def clear(): # fungsi dengan nama clear
    os.system("cls") #untuk menulis cls di terminal

def garis(): # fungsi dengan nama garis
    print("-"*75) #mencetak "-" sebanyak 75 kali

# inputan Data Mahasiswa
def data_mahasiswa(): # fungsi dengan nama data_mahasiswa
    while True: # pengulangan tidak terbatas selama tidak ada break
        mahasiswa = input("Masukkan nama mahasiswa: ",) # membuat variabel mahasiswa yang berisi inputan
        mahasiswa = mahasiswa.title().strip() # untuk mengubah setiap kata dalam string menjadi hurup kapital pada huruf pertama dan menghapus spasi di awal dan akhir string
        list_mahasiswa.append(mahasiswa) # memasukkan inputan nama mahasiswa ke dalam list 

        while True: # pengulangan tidak terbatas selama tidak ada break
            try: # mencoba menjalankan kode yang mmungkin menghasilkan kesalahan tetapi program tetap berjalan
                ana = int(input("Masukkan Nilai Matematika: ")) # membuat variabel ana yangberisi inputan nilai mata kuliah matematika, berbentuk int
                ani = int(input("Masukkan Nilai Etika Profesi: ")) # membuat variabel ana yangberisi inputan nilai mata kuliah etika profesi, berbentuk int
                anu = int(input("Masukkan Nilai Pemrograman: "))  # membuat variabel ana yangberisi inputan nilai mata kuliah pemrograman, berbentuk int
                break #keluar dari loop
            except ValueError: # menangkap kesalahan jika pengguna memasukkan sesuatu yang tidak dapat dikonversi menjadi integer
                print("Masukkan Nilai yang benar") # mencetak inputan salah

        list_nilaimtk.append(ana) # memasukkan inputan nilai matakuliah matematika ke dalam list
        list_nilaietika.append(ani) # memasukkan inputan nilai matakuliah etika profesi ke dalam list
        list_nilaipemro.append(anu) # memasukkan inputan nilai matakuliah Pemrograman ke dalam list
        choice = input("Tambahkan data mahasiswa lain? [y/n]: ") # membuat variabel yang berisi inputan unsur untuk menambahkan data mahasiswa atau tidak

        while True: # pengulangan tidak terbatas selama tidak ada break
            try: # mencoba menjalankan kode yang mmungkin menghasilkan kesalahan tetapi program tetap berjalan
                if choice == "y": # jika input dari user adalah "y"
                    break #keluar dari loop
                elif choice == "n": #jika inputan dari user adalah "n"
                    return # menghentikan loop
            except TypeError: # menangkap kesalahan jika pengguna memasukkan yang tidak sesuai dengan tipe data
                print("Pilih [y] atau [n]") # mencetak inputan salah
        
def rata_individu(): #fungsi dengan nama rata_individu untuk menghitung rata rata mata kuliah tiap mahasiswa
    rataind = [] #list untuk rata rata matakuliah tiap mahasiswa
    for i in range (len(list_nilaimtk)): #pengulangan dalam range 0 hingga jumlah value yang ada pada list
        total = list_nilaimtk[i] + list_nilaietika[i] + list_nilaietika[i] # membuat variabel dengan nama jumlah yang berisi penjumlahan dari matakuliah matematike, etika profesi, dan pemrograman pad aindex ke i
        rata = total/len(list_matakuliah) #membuat variabel dengan nama rata hasil dari pembagian jumlah nilai dengan jumlah mata kuliah yang ada dalam list
        rataind.append(rata) #memasukkan hasil dari variabel rata ke dalam list
    return rataind #mengembalikan nilai pada variabel rataind ke fungsi rata_individu, jika fungsi rata_individu dipanggil akan memunculkan nilai rata rata dari mahasiswa

def rata_matkul(): # fungsi dengan nama rata_matkul 
    List_rataMatkul = [] #list untuk rata rata tiap mata kuliah
    ratamtk = sum(list_nilaimtk)/len(list_nilaimtk) # variabel untuk menghitung jumlah dari semua elemen dalam list dan dibagi dengan jumlah yang ada dalam list
    rataetika = sum(list_nilaietika)/len(list_nilaietika) # variabel untuk menghitung jumlah dari semua elemen dalam list dan dibagi dengan jumlah yang ada dalam list
    ratapemro = sum(list_nilaipemro)/len(list_nilaipemro)# variabel untuk menghitung jumlah dari semua elemen dalam list dan dibagi dengan jumlah yang ada dalam list

    List_rataMatkul.append(ratamtk) # memasukkan hasil dari variabel rata ke dalam list
    List_rataMatkul.append(rataetika) # memasukkan hasil dari variabel rata ke dalam list
    List_rataMatkul.append(ratapemro)# memasukkan hasil dari variabel rata ke dalam list
    return List_rataMatkul # mengembalikan nilai pada bariabel list_rataMatkul ke fungsi rata_matkul, jika fungsi ini dipanggil akan memunculkan nilai rata rata tiap mata kuliah

def tampilkan_laporan(): # fungsi dengan nama tampilkan_laporan yang berisi laporan akhir dari
    clear() # memanggil fungsi clear untuk membersihkan terminal

    for i in range(len(list_mahasiswa)): #pengulangan untuk setiap elem dalam list_mahasiswa 
        print(f"Nama Mahasiswa: {list_mahasiswa[i]}") #mencetak nama mahasiswa setiap value dari list ke i
        print(f"Mata Kuliah: {', '.join(list_matakuliah)}") #mencetak nama nama mata kuliah dari list ke i
        print(f"Nilai: {list_nilaimtk[i]}, {list_nilaietika[i]}, {list_nilaipemro[i]}") #mencetak nilai nilai dari tiap mata kuliah dari list ke i
        print(" ") #mencetak spasi

    garis() #memanggil fungsi garis sebagai pembatas
    print(f"{'NAMA MAHASISWA':^50} | {'RATA RATA':^10} | {'GRADE':^9}") #mencetak dengan lebar 50/10/9 dengan menempatkan nama mahasiswa, rata rata dan grade di tengah
    garis() #memanggil fungsi garis sebagai pembatas
    rataindividu = rata_individu() #memanggil fungsi rata_individu ke dalam variabel
    for i in range(len(rataindividu)): # pengulangan yang memanggil index ke i pada rataindividu
        rataindividu[i] = f"{rataindividu[i]:.2f}" #memanggil setiap value dari list rata_individu dan diubah menjadi hanya ada 2 angka dibelakang koma
    grade = penentuan_grade() #memanggil fungsi penentuan_grade ke dalam variabel grade
    nama = list_mahasiswa #memanggil variabel list_mahasiswa ke dalam variabel nama
    for i in range (len(list_mahasiswa)): # pengulangan yang sama seperti di atas
        print(f"{nama[i]:^50}|{rataindividu[i]:^10}|{grade[i]:^9}|") # mencetak data mulai dari mahasiswa, rata-rata dan nilai akhir dalam betuk tabel dengan urutan mulai dari index ke i
        garis() #memanggil fungsi garis sebagai pembatas
    print(" ") #mencetak spasi
    garis() #memanggil fungsi garis sebagai pembatas
    print(f"{'MATA KULIAH':^50} | {'RATA RATA':^10}") #mencetak dengan lebar 50/10 Matakuliah dan Rata rata di tengah
    garis() #memanggil fungsi garis sebagai pembatas
    listratmatkul = rata_matkul() # memanggil fungsi rata_matkul() ke dalam variabel
    for i in range(len(list_matakuliah)): # pengulangan yang sama seperti di atas
        print(f"{list_matakuliah[i]:^50} | {listratmatkul[i]:^10}") #encetak setiap value dari list_matakuliah dan listratmatkul pada index ke i dengan lebar 50/10

def penentuan_grade(): #fungsi dengan nama penentuan_grade 
    grademahasiswa = [] #list untuk grade dari rata mahasiswa
    ratamahasiswa = rata_individu() # memanggil fungsi rata_individu untuk mmengumpulakn data grade dari mahasiswa 
    for i in range(len(ratamahasiswa)): # pengulangan dari index ke i dengan jumlah value yang ada pada list ratamahasiswa
        if ratamahasiswa[i] >= 85: #jika nilai ratamahasiswa index ke i lebih dari sama dengan 85
            grade = "A" # membuat variabel grade berisi nilai "A" 
        elif ratamahasiswa[i] >= 70 < 85: # jika nilai ratamahasiswa index ke i lebih dari sama dengan 70 dan kurang dari 85
            grade = "B" # membuat variabel grade berisi nilai "B"
        elif ratamahasiswa[i] >= 50 < 70: # jika nilai ratamahasiswa index ke i lebih dari sama dengan 50 dan kurang dari 70
            grade = "C" # membuat variabel grade berisi nilai "C"
        elif ratamahasiswa[i] < 50: # jika nilai ratamahasiswa index ke i kurang dari 50
            grade = "D" # membuat variabel grade berisi nilai "D"
        grademahasiswa.append(grade) # memasukkan nilai dari variabel grade ke dalam list grademahasiswa
    return grademahasiswa # mengembalikan nilai grade mahasiswa ke fungsi penentuan_grade. jika fungsi dipanggil akan menghasilkan nilai yang sama dengan nilai dari grademahasiswa

while True: # pengulangan tidak terbatas selama tidak ada break
    print("""
    Hai Mahasigma selamat datang di program laporan penilaian, Yuk hitung nilaimu!!!
    1. Tambahkan Data Mahasigma 
    2. Tampilkan Rapot Mahasigma (Pastikan Tambahkan data terlebih dahulu sebelum menampilkan laporan!!)
    3. Exit
    """) #Mencetak pilihan pilihan yang ada di program ini
    try: # mencoba menjalankan kode yang mmungkin menghasilkan kesalahan tetapi program tetap berjalan
        pilih = int(input("Silahkan pilih menu [1/2/3]: ")) #variabel inputan untuk memilih pilihan yang ada
    except ValueError: # menangkap kesalahan jika pengguna memasukkan sesuatu yang tidak dapat dikonversi menjadi integer
        print("Dimohon memasukkan pilihan yang benar") # mencetak pesan setelah pengguna salah memasukkan inputan
    else: # melanjutkan program ketika inputan sudah benar
        if pilih == 1: # jika input dari pengguna angka 1
            data_mahasiswa() # memanggil fungsi data_mahasiswa
        elif pilih == 2: # jika input dari pengguna angka 2
            tampilkan_laporan() # memanggil fungsi tampilkan_laporan
        elif pilih == 3: # jika input dari pengguna angka 3
            clear() #memanggil fungsi clear() dan menghapus terminal
            print("""
            NAMA         : RAFI HADIANTO ARIBOWO 
            Program studi: TEKNOLOGI INFORMASI
            NIM          : 242410102006
            KELAS        : ALGORITMA DAN PEMROGRAMAN D
            """) #mencetak identitas pembuat program
            exit() #keluar dari program