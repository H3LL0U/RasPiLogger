import usb.core as usb
import keyboard 

#name of the key : byte representation.
usb_main_packets = {
'a': 0x04,
'b': 0x05,
'c': 0x06,
'd': 0x07,
'e': 0x08,
'f': 0x09,
'g': 0x0A,
'h': 0x0B,
'i': 0x0C,
'j': 0x0D,
'k': 0x0E,
'l': 0x0F,
'm': 0x10,
'n': 0x11,
'o': 0x12,
'p': 0x13,
'q': 0x14,
'r': 0x15,
's': 0x16,
't': 0x17,
'u': 0x18,
'v': 0x19,
'w': 0x1A,
'x': 0x1B,
'y': 0x1C,
'z': 0x1D,
'1': 0x1E,
'2': 0x1F,
'3': 0x20,
'4': 0x21,
'5': 0x22,
'6': 0x23,
'7': 0x24,
'8': 0x25,
'9': 0x26,
'0': 0x27,
'enter': 0x28,
'esc': 0x29,
'backspace': 0x2A,
'tab': 0x2B,
'space': 0x2C,
'-': 0x2D,
'=': 0x2E,
'[': 0x2F,
']': 0x30,
'\\': 0x31,
';': 0x33,
'\'': 0x34,
'`': 0x35,
',': 0x36,
'.': 0x37,
'/': 0x38,
'capslock': 0x39,
'f1': 0x3A,
'f2': 0x3B,
'f3': 0x3C,
'f4': 0x3D,
'f5': 0x3E,
'f6': 0x3F,
'f7': 0x40,
'f8': 0x41,
'f9': 0x42,
'f10': 0x43,
'f11': 0x44,
'f12': 0x45,
'print screen': 0x46,
'scroll lock': 0x47,
'pause': 0x48,
'insert': 0x49,
'home': 0x4A,
'pageup': 0x4B,
'delete': 0x4C,
'end': 0x4D,
'page down': 0x4E,
'right': 0x4F,
'left': 0x50,
'down': 0x51,
'up': 0x52,
'numlock': 0x53,
'kp/': 0x54,
'kp*': 0x55,
'kp-': 0x56,
'kp+': 0x57,
'kpenter': 0x58,
'kp1': 0x59,
'kp2': 0x5A,
'kp3': 0x5B,
'kp4': 0x5C,
'kp5': 0x5D,
'kp6': 0x5E,
'kp7': 0x5F,
'kp8': 0x60,
'kp9': 0x61,
'kp0': 0x62,
'kp.': 0x63,
'app': 0x65,
'power': 0x66,
'kp=': 0x67,
'f13': 0x68,
'f14': 0x69,
'f15': 0x6A,
'f16': 0x6B,
'f17': 0x6C,
'f18': 0x6D,
'f19': 0x6E,
'f20': 0x6F,
'f21': 0x70,
'f22': 0x71,
'f23': 0x72,
'f24': 0x73,
'execute': 0x74,
'help': 0x75,
'menu': 0x76,
'select': 0x77,
'stop': 0x78,
'again': 0x79,
'undo': 0x7A,
'cut': 0x7B,
'copy': 0x7C,
'paste': 0x7D,
'find': 0x7E,
'mute': 0x7F,
'volumeup': 0x80,
'volumedown': 0x81,
'lockingcapslock': 0x82,
'lockingnumlock': 0x83,
'lockingscrolllock': 0x84,
'kp,': 0x85,
'kpequal': 0x86,
'international1': 0x87,
'international2': 0x88,
'international3': 0x89,
'international4': 0x8A,
'international5': 0x8B,
'international6': 0x8C,
'international7': 0x8D,
'international8': 0x8E,
'international9': 0x8F,
'lang1': 0x90,
'lang2': 0x91,
'lang3': 0x92,
'lang4': 0x93,
'lang5': 0x94,
'lang6': 0x95,
'lang7': 0x96,
'lang8': 0x97,
'lang9': 0x98,
'alternateerase': 0x99,
'sysreq': 0x9A,
'cancel': 0x9B,
'clear': 0xA2,
'prior': 0x9D,
'return': 0x9E,
'separator': 0x9F,
'out': 0xA0,
'oper': 0xA1,
'crsel': 0xA3,
'exsel': 0xA4,
'reserved': 0xA6,
#'left control': 0xE0,
#'left shift': 0xE1,
#'left alt': 0xE2,
#'left gui': 0xE3,
#'right control': 0xE4,
#'right shift': 0xE5,
#'right alt': 0xE6,
#'right gui': 0xE7,
}


scancode_to_packet = {
83:0x4C,
30:0x4,
48:0x5,
46:0x6,
32:0x7,
18:0x8,
33:0x9,
34:0xa,
35:0xb,
23:0xc,
36:0xd,
37:0xe,
38:0xf,
50:0x10,
49:0x11,
24:0x12,
25:0x13,
16:0x14,
19:0x15,
31:0x16,
20:0x17,
22:0x18,
47:0x19,
17:0x1a,
45:0x1b,
21:0x1c,
44:0x1d,
2:0x1e,
3:0x1f,
4:0x20,
5:0x21,
6:0x22,
7:0x23,
8:0x24,
9:0x25,
10:0x26,
11:0x27,
28:0x28,
1:0x29,
14:0x2a,
15:0x2b,
57:0x2c,
12:0x2d,
13:0x2e,
26:0x2f,
27:0x30,
43:0x31,
39:0x33,
40:0x34,
41:0x35,
51:0x36,
52:0x37,
53:0x38,
58:0x39,
59:0x3a,
60:0x3b,
61:0x3c,
62:0x3d,
63:0x3e,
64:0x3f,
65:0x40,
66:0x41,
67:0x42,
68:0x43,
87:0x44,
88:0x45,
55:0x55,
70:0x47,
119:0x48,
110:0x71,
102:0x6a,
104:0x6b,
111:0x72,
107:0x6e,
109:0x70,
106:0x6d,
105:0x6c,
108:0x6f,
103:0x67,
69:0x53,
98:0x62,
74:0x56,
78:0x57,
96:0x60,
89:0x59,
90:0x5a,
91:0x5b,
92:0x5c,
93:0x65,
94:0x5e,
95:0x5f,
97:0x61,
99:0x63,
116:0x74,
100:0x68,
101:0x69,
112:0x73,
138:0x89,
139:0x8a,
137:0x88,
121:0x79,
122:0x7a,
120:0x7b,
124:0x7c,
125:0x7d,
126:0x7e,
127:0x7f,
128:0x80,
129:0x81,
130:0x82,
131:0x83,
132:0x84,
133:0x85,
135:0x86,
136:0x87,
140:0x8b,
141:0x8c,
142:0x8d,
143:0x8e,
144:0x8f,
145:0x90,
146:0x91,
147:0x92,
148:0x93,
149:0x94,
150:0x95,
151:0x96,
152:0x97,
153:0x98,
155:0x9b,
154:0x9a,
156:0xa2,
157:0x9d,
158:0x9e,
159:0x9f,
160:0xa0,
161:0xa1,
162:0xa3,
163:0xa4,
165:0xa6,
#arrows
73: 0x4B,
81: 0x4E, #pgdn
77: 0x4F,
75: 0x50,
80: 0x51,
72: 0x52,

76: 0xA2,
71: 0x4A,
79: 0x4D,
82:0x49
}


#Name of the key : bit placement if active

modifier_keys = {

29 : 0, #ctrl
42: 1, #Shift
56: 2, #alt
91 : 3, #left windows
#"right ctrl": 4,
54 :5, #right shift
541: 6,
#"right windows": 7
}



        
        