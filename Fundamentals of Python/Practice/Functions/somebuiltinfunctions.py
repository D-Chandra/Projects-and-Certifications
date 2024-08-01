#---------------abs()---------------------#
# print(abs(20-40) , 20-40)
#--------------all()-----------------------#
# val = None
# mytuple = (2,4,3,4,3,val,4,3,4)
# print(all(mytuple))
#---------------any()-----------------------#works opposite to a()
#---------------ascii()-------------------# for octal use '\' for hexa use '\x'  fro binary use '\b' or '0b' (not sure)
# x = "hell\157  world"
# print(ascii(x))
#--------------bin()----------------------#
# print(bin(\x6F))
# print(hex(678))
# print(oct(34))
# print(chr('o'))
# print(ascii('c'))
#---------------bool()-------------------#
# t1 = {False:True}
# t2 = 6j
# print(type(t1))
# print(t1,'is',bool(t1))
# print(type(t2))
# print(t2,'is',bool(t2))
#----------------complex numbers----------#
# c = (3 - 6j)
# print("A complex Number::",c)
# print("Real Part::",c.real)
# print("Imag Part::",c.imag)  #he complex conjugate of a complex number is obtained by changing the sign of its imaginary part.
# print("Conjugate parts::",c.conjugate())
# print("Complex Function::",complex(2,6))
#--------------bytearray() and bytes()----------------#
# str1 = "Hello World"
# immutable_bytes = bytes(2) #creates series of 2  bytes each of value zero
# mutable_bytes = bytearray(2) #creates a empty byte array of 2 bytes
# immdata_bytes = bytes(b'\xfa\xfb')
# mutdata_bytes = bytearray(b'\xDE\xAD\xfa\x11\x34')
# immutable_bytes.append(3)
# immutable_bytes.append(4)
# mutable_bytes.append(1)
# mutable_bytes.append(2)
# mutable_bytes.append(255)
# print(mutable_bytes)
# print(immdata_bytes)
# print(mutdata_bytes)
# print(bytearray(str1,'utf-8'))