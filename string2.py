#operator dalam method
#mengubah case dari string

salam = "brO!"
print(salam.upper()) 
print(salam.lower()) 

#contoh pengecekan lower case 
print(salam.islower())
print(salam.isupper())

#isalpha() untuk mengecek semuanya huruf
#isalnum() untuk mengecek huruf dan angka
#isdecimal() untuk mengecek angka saja 
#isspace() untuk mengecek spasi, tab, neline \n
#istitle() cek semua kata itu dimulai dengan huruf besar 
print(salam.istitle())

## mengecek komponen startswith() dan endwith()
cek_start = "Yes I Am".startswith("Y")
cek_start = "Yes I Am".endswith("m")
print(cek_start)

##penggabungan komponen join() split()
pisah = ['aku','dengan','kamu'] #ini adalah list (kumpulan data)
gabung = "*".join(pisah)
print(gabung) 

gabung = "sarah*haras"
print(gabung.split('*'))


#alokasi Karakter rjust() ljust center()
print(5* "=" + "data" + "="*5 )
kanan = "kananaaa".rjust(10)
print("'"+kanan+"'")
kanan = "kananaaa".ljust(10)
print("'"+kanan+"'")
kanan = "center".center(20,"*")
print(""+kanan+"")
kanan = kanan.strip("*") #menghilangkan tanda *
print("'"+kanan+"'")