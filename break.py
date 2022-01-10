#break 
angka = 0
data_int = int(input("masukan angka: "))
while True:
    angka+=1
    print(f"angka : {angka}")
    if angka == data_int:
        print("nice")
        break
    print("whatsup")
print("end")