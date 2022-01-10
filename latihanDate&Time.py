#data and time (latihan)
import datetime as dt

# hari_ini = dt.date.today()
# print(hari_ini)

# tanggal = dt.date(2003,10,10)
# tanggal = dt.date(1996,9,12)
# print(tanggal)
# print(f"hari ini adalah hari = {tanggal:%A}")

print("Masukan tanggal lahir :\n")
tanggal = int(input("tanggal :"))
bulan   = int(input("bulan   :"))
tahun   = int(input("tahun   :"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)

print(f"Maka hari lahir anda adalah = {tanggal_lahir:%A}")


hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur = hari_ini - tanggal_lahir
umur_tahun = umur.days // 365
umur_sisa_bulan = (umur.days % 365) // 30


print(f"umur anda perhari adalah : {umur}")
print(f"umur anda tahun adalah : {tahun}")
print(f"umur anda per tahun adalah : {umur_tahun}")
print(f"bulan : {umur_sisa_bulan}")