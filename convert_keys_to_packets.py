from usb_packets import scancode_to_packet, modifier_keys
NULL_CHR = chr(0)
def set_bit(byte:chr, bit_index:int) -> chr:
    byte = ord(byte)
    mask = 1 << bit_index
    result = byte | mask
    return chr(result)

def convert_scancodes_to_packets(scancodes : list[int]):
    
    initial_packet = [NULL_CHR]*8

    for keyname in scancodes:
        if keyname in scancode_to_packet:
            for idx, character in enumerate(initial_packet[2:]):
                if character == chr(0):
                    initial_packet[idx+2] = chr(scancode_to_packet[keyname])
                    break
                if initial_packet[-1]!=NULL_CHR:
                    initial_packet[2:] = map(lambda *_: chr(1) , initial_packet[2:])
        if keyname in modifier_keys:
            initial_packet[0] = set_bit(initial_packet[0],modifier_keys[keyname])

        

    return "".join(initial_packet)




