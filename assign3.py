#!/home/kurt/Documents python

MF=0.03125
x=input("Enter CAN message, in HEX, MSB to LSB")
print("You entered",x)
type(x)
converted_value=int(x,16)
decoded_value1=converted_value*MF
print("Decoded value for CAN message 1 is",decoded_value1)

