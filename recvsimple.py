import random
import time

import can

from modbuscrc import crc

bus = can.interface.Bus(channel = 'can0', bustype='socketcan')

received = 0
mismatched = 0
match_hypothesis = 0

def recvthread():
    
    global received
    global mismatched
    global match_hypothesis

    while True:
        msg = bus.recv()
        data = msg.data[2:]
        val = int.from_bytes(data, 'little')

        crccalc = crc(data)
        crcpkt = msg.data[0] + (msg.data[1] << 8)
    
        received += 1
        if crcpkt != crccalc:
            mismatched += 1

            # hypothesis: corrupted bytes are packet id, shifted a bit
            predict_last = ((msg.arbitration_id & 0x7) << 13) + (msg.arbitration_id >> 3)
            last = int.from_bytes(data[4:], "little")

            if predict_last == last:
                match_hypothesis += 1
            else:
                print(msg)
        else:
            good = val


def main():
    import threading
    threading.Thread(target=recvthread, daemon=True).start()
    while True:
        time.sleep(1)
        print(received, mismatched, match_hypothesis)


if __name__ == '__main__':
    main()
