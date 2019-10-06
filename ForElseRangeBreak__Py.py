Garis = "-"
JUDUL1 = "BAGIAN 1: PENGGUNAAN 'RANGE' DALAM FOR"
JUDUL2 = "BAGIAN 2: PENGGUNAAN 'RANGE' DALAM FOR MENGGUNAKAN INCREMENT" 
JUDUL3 = "BAGIAN 3: PRINT RANGE DI KOLOM AWAL TANPA FOR"
JUDUL4 = "BAGIAN 4: PENGGUNAKAN 'RANGE' DALAM MENCARI NILAI MENGGUNAKAN IF"
JUDUL5 = "BAGIAN 5: PENGGUNAKAN 'RANGE' DALAM MENCARI NILAI MENGGUNAKAN IF DAN BREAK"
JUDUL6 = "BAGIAN 6: PENGGUNAKAN 'RANGE' DALAM MENCARI NILAI MENGGUNAKAN IF, BREAK DAN ELSE"

#BAGIAN 1: PENGGUNAAN 'RANGE' DALAM FOR
print(Garis * 3, JUDUL1, Garis * 3)

for X in range(0, 11):      #Biasa
    print(X)



#BAGIAN 2: PENGGUNAAN 'RANGE' DALAM FOR MENGGUNAKAN INCREMENT
print('\n', Garis * 3, JUDUL2, Garis * 3)

for X in range(1, 50, 7):   #Menggunakan Increment Namun Harus Bernilai: Integer (Contoh: 7)
    print(X)                #Akan menghasilkan nilai dengan kelipatan 7



#BAGIAN 3: PRINT 'RANGE' DI KOLOM AWAL TANPA FOR
print('\n', Garis * 3, JUDUL3, Garis * 3)
print(range(0, 50, 7))      #Akan menghasilkan output print biasa karena 'range' bukan sebuah List



#BAGIAN 4: PENGGUNAKAN 'RANGE' DALAM MENCARI NILAI MENGGUNAKAN IF
print('\n', Garis * 3, JUDUL4, Garis * 3)

Angka = 7
for X in range(1, 16):                          #Definisikan nilai X berisi rentang nilai antara 1 sd 15
    print(X)                                    #Cetak terlebih dahulu daftar angka
    if X == Angka:                              #Jika terdapat angka 7 dalam rentang nilai antara 1 sd 15 maka
        print('(Angka Ditemukan:', X, ')')      #Beritahukan bahwa angka ditemukan.



#BAGIAN 5: PENGGUNAKAN 'RANGE' DALAM MENCARI NILAI MENGGUNAKAN IF DAN BREAK
print('\n', Garis * 3, JUDUL5, Garis * 3)

Angka = 11
for X in range(1, 100):                         #Definisikan nilai X berisi rentang nilai antara 1 sd 99
    print(X)                                    #Cetak terlebih dahulu daftar angka
    if X == Angka:                              #Jika terdapat angka 11 dalam rentang nilai antara 1 sd 99 maka
        print('(Angka Ditemukan:', X, ')', 
              '\n', 
              '(Pengurutan Angka Dihentikan!)') #Beritahukan bahwa angka ditemukan.
        break                                   #Berhenti untuk menampilkan deret angka jika angka yang dicari sudah ditemukan.


#BAGIAN 6: PENGGUNAKAN 'RANGE' DALAM MENCARI NILAI MENGGUNAKAN IF, BREAK DAN ELSE (Part 1)
print('\n', Garis * 3, JUDUL6, '(Part 1)', Garis * 3)

Angka = 12
for X in range(0, 11):                          #Definisikan nilai X berisi rentang nilai antara 0 sd 10
    print(X)                                    #Cetak terlebih dahulu daftar angka
    if X == Angka:                              #Jika terdapat angka 12 dalam rentang nilai antara 0 sd 10 maka
        print('(Angka Ditemukan :', X, ')')     
        break                                   #Berhenti untuk menampilkan deret angka jika angka yang dicari sudah ditemukan.
else:                                           #Jika TIDAK terdapat angka 12 dalam rentang nilai antara 0 sd 10 maka, 
    print("Angka", Angka, "Tidak Ditemukan!")



#BAGIAN 7: PENGGUNAKAN 'RANGE' DALAM MENCARI NILAI MENGGUNAKAN IF, BREAK DAN ELSE (Part 2)
print('\n', Garis * 3, JUDUL6, '(Part 2)', Garis * 3)

Angka = 12
for X in range(0, 11):                              #Definisikan nilai X berisi rentang nilai antara 0 sd 10
    print(X)                                        #Cetak terlebih dahulu daftar angka
    if X == Angka:                                  #Jika terdapat angka 12 dalam rentang nilai antara 0 sd 10 maka
        print('(Angka Ditemukan :', X, ')')     
        break                                       #Berhenti untuk menampilkan deret angka jika angka yang dicari sudah ditemukan.
    else:                                           #Jika TIDAK terdapat angka 12 dalam rentang nilai antara 0 sd 10 maka, 
        print("Angka", Angka, "Tidak Ditemukan!")