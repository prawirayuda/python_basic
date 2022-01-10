#widht and multiline 
#Data 
data_nama = "yudddasassssssss"
data_umur = 12
data_tinggi = 169.2
data_nomor= 41

#string multiline
data_string = f"nama = {data_nama},\numur = {data_tinggi}, \ntinggi = {data_tinggi}, \nnomor = {data_nomor}"
print(5*"="+"data string"+5*"=")

print(data_string)

# data multiline(kutip triplets)
data_string = f"""
nama    = {data_nama:>5}
tinggi  = {data_tinggi:>5}


"""

print(data_string)