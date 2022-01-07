nama = "yuda5678910 " 
panjang = len(nama)
print(panjang)

#cek apakah ada komponen char atau string 
#in -- not in

d = "d"
status = d in nama
status = d not in nama
print(status)


#mengulang string 
print("wk"*10)

#indexing (mengambil data dari string)
print("Index ke-0 : " + nama[2])

#ambil dari belakang
print("index ke (-1) : " + nama[-1] )

#ambil 1 sampai 4
print("index ke 0 sampai 3 : "+ nama[0:3])

#ambil data string pakai jeda yang ketiga adalah increment jadi lompat satu
print(nama[1:4:1])
print("paling kecil : " + min(nama))

#paling besar berdasarkan ascii code 
print("paling besar : "+ max(nama))

#cek ascii code 
spasi = ord(" ")
print("spasi :" + str(spasi))

#operator dalam bentuk method 
data = "otong surotong"
jumlah = data.count("o")
print(str(jumlah))