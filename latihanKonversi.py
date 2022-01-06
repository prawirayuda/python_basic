print("\nPROGRAM KONVERSI TEMP\n")

celcius = float(input("masukan suhu in Celcius : "))
print("Suhu : ", celcius, "Celcius")

#reamur

reamur = (4/5) * celcius
print("suhu dalam reamur : ", reamur, "Reamur")


#farenheit
fahrenheit = ((9/5)*celcius)+32
print("suhu dalam fahrenheit", fahrenheit, "fahrenheit")


#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin : ", kelvin, "kelvin")


# pr
#fahrenheit -> kelvin

hasilfahrenheitkekelvin = (kelvin - 273.15) * 9/5 +32
print("konversi dari fahrenheit ke kelvin :", hasilfahrenheitkekelvin, "kelvin")

#kelvin -> fahrenheit
hasilkelvinkefahrenheit = (hasilfahrenheitkekelvin -32) * 5/9 +273.15
print("konversi dari kelvin ke fahrenheit :", hasilkelvinkefahrenheit, "fahrenheit")
