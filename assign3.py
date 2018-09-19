#!/home/kurt/Documents python

MF=0.03125
s1=input("Enter CAN message, in HEX, MSB to LSB")
print("You entered",s1)
type(s1)
converted_value2=int(s1,16)
decoded_value1=converted_value2*MF
print("Decoded value for CAN message 1 is",decoded_value1)

