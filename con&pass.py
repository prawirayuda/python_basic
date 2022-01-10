""" # pass tidak akan dieksekusi 
angka = 0
while angka < 5:
    angka +=1
    
    if angka == 4:
        pass #ini tidak akan di eksekusi ntar buat oop atau function
        print("sfrf")
    print(angka)
     """

angka = 0
print (f"angka sekarang {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    if angka == 3:
        print("good")
        continue #akan membuat loopo meloncat ke step selanjut nya
    print("whatsapp@")
    
print("end")
     