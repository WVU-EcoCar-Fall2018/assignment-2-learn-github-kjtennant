from threading import Thread, Lock

mutex = Lock()
CAN_message_1= [0x01, 0x40, 0x00, 0x00, 0x00]

def CANDecode():
  mutex.acquire()
  CAN_message_1[0]=CAN_message_1[0] & 0x3f
  decoded = (CAN_message_1[0] << 3) + (CAN_message_1[1] >> 5)
  print(decoded)
  mutex.release()

def CANUpdate():
  mutex.acquire()
  CAN_message_1[1] = CAN_message_1[1]+10
  mutex.release()



th_CANDecode  = Thread(target=CANDecode)
th_CANUpdate  = Thread(target=CANUpdate)

th_CANDecode.start()
th_CANUpdate.start()


