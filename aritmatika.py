a = 10
b = 3


#operasi tambah 
hasil = a + b
print(a,'+',b,'=', hasil)
#operasi kurang
hasil = a - b
print(a,'-',b,'=', hasil)
#operasi bagi 
hasil = a / b
print(a,'/',b,'=', hasil)
#operasi kali 
hasil = a * b
print(a,'*',b,'=', hasil)
#operasi exponent 
hasil = a ** b
print(a,'**',b,'=', hasil)
#operasi modulus % 
hasil = a % b
print(a,'mod',b,'=', hasil)
#operasi floor division 
hasil = a // b
print(a,'//',b,'=', hasil)

#operasi precedence 
x = 3
y = 2
z = 4


#prioritas operasi () -> exponent -> perkaliandkk -> pertambahandkk
hasil = x**y *4 + 3 /2 -2 % 4 //3   
print('hasilnya ', hasil)

hasil = x + y * z
