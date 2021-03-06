import serial

all_white = bytearray([
    0x80,  # header
    0x83,  # 28 bytes refresh
    0xFF,  # address
    0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, # 28 bytes data
    0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F,
    0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F,
    0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 
    0x8F # EOT
])

with serial.Serial("/dev/ttyUSB0", 57600) as srl:
    srl.write(all_white)
    