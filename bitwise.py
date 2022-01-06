#binary operation

a = 9
b = 5

#OR (|)
c = a & b # bernilai true jika semua nya true
c = a | b # bernilai true jika salah ada yg true dan kedua nilai true 
c = a ^ b # XORbernilai true jika salah satu true dan tidak bernilai true jika keduanya true
c = ~a #NOT (~)
print("\n nilai: ",a, 'binari: ', format(a,'08b'))  
print("\n nilai: ",b, 'binari: ', format(b,'08b'))  
print("\n nilai:",c,'binari: ', format(c,'08b'))

d = 0b0000001001  
e = 0b1111111111  
print('\n nilai :',e^d, 'binary: ', format(e^d, '08b'))

#shift right (>>) and shift left (<<)
c = a << 5 
print ('nilai : ',a,' , binary : ',format(a,'08b'))
print ('nilai : ',c,' , binary : ',format(c,'08b'))

