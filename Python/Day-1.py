#----------------------------{Day - 1 [Nov. 2 , 2026]}----------------------------------

#data-types - 

#1. Number and its methods

int_value = 25
dec_value = 28.5
complex_value = 2 + 3j
value = -12.87

print(int_value, type(int_value))
print(dec_value, type(dec_value))
print(complex_value, type(complex_value))
print(value, type(value))
#-------------------------------------------------------------------------------------
#Operations...
print("Absolute:", abs(value))
print("Rounded:", round(value,2))
print("Integer ratio:", value.as_integer_ratio())


num = 6578 #123,345,2
dec_num = 12.49

#int methods
print("Binary representation:", num.bit_length())
print("Binary:", bin(num))
print("Number of 1 bits:", num.bit_count())
print("6578 as bytes:", num.to_bytes(2, byteorder='big'))
print("6578 as bytes:", num.to_bytes(2, byteorder='little'))
print("interger ratio:", num.as_integer_ratio())

#float methods
print("decimal ratio:", dec_num.as_integer_ratio())
print("is decimal an integer? :- ", dec_num.is_integer())
print("Hexadecimal form:- ", dec_num.hex())
print("Restored from hex:- ", float.fromhex(dec_num.hex()))

#Some other built-in functions
print("Absolute value:", abs(-dec_num))
print("Rounded value:- ", round(dec_num))
