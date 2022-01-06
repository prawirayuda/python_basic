
#komparasi dapat bekerja pada syntak literal (literal itu tidak memakan memmory ) is membandingkan memory atau object

a = 1
b = 0

# > (lebih besar)|| >= lebih besar sama dengan || <= lebih kecil sama dengan || < lebih kecil  
hasil = a > b
print(a, '>', b, 'hasil  :' ,hasil)
hasil = a <   b
print(a, '<', b, 'hasil  :' ,hasil)
hasil = a <=  b
print(a, '<=',b, 'hasil :' ,hasil)


# sama dengan (==) and tidak sama dengan (!==)

hasil = a == b 
print(hasil)



#is and is not tidak utk lieral , untuk object identity

x = 3
y = 3
tell = x is y
print(tell)

print("object identity(is)")
x = 5
y = 5
print('nilai x =', x, 'id x = ', hex(id(x)))
print('nilai y =', y, 'id y = ', hex(id(y)))