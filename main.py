import os

KERNEL_PATHS = [r"C:\Windows\SysNative\ntoskrnl.exe",
                r"C:\Windows\System32\ntoskrnl.exe"]

def ChangeEndian(tmpArray):
    for i in range(int(len(tmpArray)/2)):
        tmp = tmpArray[i]
        tmpArray[i] = tmpArray[len(tmpArray)-i-1]
        tmpArray[len(tmpArray)-i-1] = tmp

    return tmpArray

for potential_path in KERNEL_PATHS:
    if os.path.isfile(potential_path):
        f = open(potential_path,'rb')
        count = 0
        while(1):
            data = f.read(16)
            GUID = ""
            if data[0] == 82 and data[1] == 83 and data[2] == 68 and data[3] == 83 :
                tmpArray = bytearray(data[4:8])
                GUID += ChangeEndian(tmpArray).hex()

                tmpArray = bytearray(data[8:10])
                GUID += ChangeEndian(tmpArray).hex()

                tmpArray = bytearray(data[10:12])
                GUID += ChangeEndian(tmpArray).hex()

                GUID += bytearray(data[12:16]).hex()

                data = f.read(16)
                GUID += bytearray(data[:4]).hex()

                GUID += hex(data[4])[2:]

                print(GUID)
                break