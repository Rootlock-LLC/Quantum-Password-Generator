def listToString(s):                # Converts list of bits into string 
    str1 = ""    
    for element in s: 
        str1 += element      
    return str1 

def decode_binary_string(s):        # decodes binary string into ASCII
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

qfile = open("bits.txt", "r")       # bits.txt is the generate file from Q# output
bits = qfile.readline() 
sbits = str(bits)
bitarray = []

for bit in sbits:                   # Filter our string to only include numbers  
    try:
        int(bit)                    # Check if character is numeric
        bitarray.append(bit)        # Add bit to array 
    except:
        pass
qfile.close
sraw_bits = listToString(bitarray)
ascii_text = decode_binary_string(sraw_bits)
char_array = []

for character in ascii_text:        # Loops through original ascii conversion and shortens ascii range to common ascii characters
    dec = ord(character)            # Converts ascii character to decimal
    mods = dec % 93                 # Mods decimal 93 in corrilation to range of common characters in Ascii table
    ascii_dec = mods + 33           # Adds 33 to set minimal numer in range to ascii character 33
    char_array.append(chr(ascii_dec)) 

moded_ascii = listToString(char_array)
print('\n[!] Raw Bits:', sraw_bits, '\n[!] Randomly generate string:', moded_ascii, '\n[!] Number of Characters Generated:', len(ascii_text))

