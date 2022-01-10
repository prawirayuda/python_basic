#format string 

#contoh genereic
nama = "mar"
format_str = f"hello {nama}"

print(format_str)

#angka 
angka = 2022.2
format_str = f"angka {angka}"
print(format_str)

#boolean
boolean = False
format_str = f"nilai boolean = {boolean}"
print(format_str)


#bilangan bulat 
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

#bilangan ribuan 
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)


#bilangan desimal 

angka = 200.4321
format_str = f"ribuan = {angka:.2f}"
print(format_str)


#menampilkan leading zero 
angka = 2005.12345
format_str  = f"desimal = {angka:09.3f}"
print(format_str)


#menampilkan tanda + atau - 
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"minus = {angka_plus:+}"


print(format_minus)
print(format_plus)

#formatting persen 
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"

print(format_persen)

#melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
format_str = f"harga total =Rp.{harga*jumlah}"
print(format_str)

#format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary =f"binary = {bin(angka)}"
format_octal =f"octal = {oct(angka)}"
format_hexa =f"hexa = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexa)

