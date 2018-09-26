from threading import Thread, Lock
#this imports thread and lock from the threading package

mutex = Lock()
#locks the mutex so that the threads don't access the memory at the same time
CAN_message_1= [0x01, 0x40, 0x00, 0x00, 0x00]
#This creates an array for the CAN data, values displayed in hex

def CANDecode():
  #this function decodes the matrix to give the value
  mutex.acquire()
  #acquires the mutex for this thread
  CAN_message_1[0]=CAN_message_1[0] & 0x3f
  #bitwise operation to mask the 1st bit
  decoded = (CAN_message_1[0] << 3) + (CAN_message_1[1] >> 5)
  #algorithm to decode the message of both bits
  print(decoded)
  #prints the decoded value
  mutex.release()
  #releases the mutex so it can be used in the next thread

def CANUpdate():
  #this function updates the CAN 
  mutex.acquire()
  #acquires the mutex for this thread
  CAN_message_1[1] = CAN_message_1[1]+10
  #increments the CAN message
  mutex.release()
  #releases the mutex so it cna be used for the other thread



th_CANDecode  = Thread(target=CANDecode)
th_CANUpdate  = Thread(target=CANUpdate)
#turns the functions into threads

th_CANDecode.start()
th_CANUpdate.start()
#starts the decode and update threads

