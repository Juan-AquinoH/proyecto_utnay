 ##Explain in detail the expression s *= n, where s is a mutable sequence 
#and n is a number between 0 and 255. 
s = [1, 2, 3]
s *= 5
print(f"\n{s}")

s = bytearray([65, 66, 67])
s *= 4
print(s)

s1 = ["a", "b", "c", "d", "f"]
s1 *= 3
print(s1)

s2 = [230, 235, 240, 245, 250]
s2 *= 2
print(s2)

#Resultados esperados
#[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
#bytearray(b'ABCABCABCABC')
#'a', 'b', 'c', 'd', 'f', 'a', 'b', 'c', 'd', 'f', 'a', 'b', 'c', 'd', 'f']
#[230, 235, 240, 245, 250, 230, 235, 240, 245, 250]