import time
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid
import busio
import storage

uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

buffer = ""
currently_pressed = set()
kbd = Keyboard(usb_hid.devices)




def exec_from_buffer():
    global buffer
    global currently_pressed
    keycodes_to_exec = []
    while "\n" in buffer:
        end_point_index = buffer.find("\n")
        keycodes_to_exec = [int(i) for i in buffer[:end_point_index].split(",") if i.isdigit()]
        for keycode in keycodes_to_exec:
            if keycode == 0:
                kbd.release_all()
                currently_pressed = set()
                continue
            
            print(keycode)
            try:
                kbd.press(int(keycode))
                currently_pressed.add(int(keycode))
            except OverflowError:
    
        
                print("overflow")
        
        buffer = buffer[end_point_index+1:]
    
        for key_to_unpress in {i for i in currently_pressed if i not in keycodes_to_exec}:
        
        
            kbd.release(int(key_to_unpress))
        
            currently_pressed.remove(key_to_unpress)
        
while True:
    if uart.in_waiting > 0:
        
        received_bytes = uart.read(uart.in_waiting)
        try:
            strings = received_bytes.decode("utf-8")
        except UnicodeError:
            continue
        buffer += strings
        exec_from_buffer()  
        