
'''
this can be used to convert list of scancodes into data packet sent by usb keyboard
(not currently used in the project)
Uses usb_packets from /files for RP zero
'''

from usb_packets import scancode_to_packet, modifier_keys
NULL_CHR = chr(0)
def set_bit(byte:chr, bit_index:int) -> chr:
    byte = ord(byte)
    mask = 1 << bit_index
    result = byte | mask
    return chr(result)

def convert_scancodes_to_packets(scancodes : list[int]):
    
    initial_packet = [NULL_CHR]*8

    for scancode in scancodes:
        if scancode in scancode_to_packet:
            for idx, character in enumerate(initial_packet[2:]):
                if character == chr(0):
                    initial_packet[idx+2] = chr(scancode_to_packet[scancode])
                    
                    break
                if initial_packet[-1]!=NULL_CHR:
                    initial_packet[2:] = map(lambda *_: chr(1) , initial_packet[2:])
        elif scancode in modifier_keys:
            initial_packet[0] = set_bit(initial_packet[0],modifier_keys[scancode])
        else:
            print("scancode doesn't exist")
        

    return "".join(initial_packet)




