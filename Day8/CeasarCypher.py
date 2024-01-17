print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")


alphabet_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def encode(message, shiftNumber):
    encoded_alphabet_array = []
    for i in range(shiftNumber, len(alphabet_array) -1):
        encoded_alphabet_array.append(alphabet_array[i])
        i += 1
    for i in range(0, shiftNumber):
        encoded_alphabet_array.append(alphabet_array[i])
    encodedMessage = ""
    for i in message:
        encodedMessage += encoded_alphabet_array[alphabet_array.index(i)]
    return encodedMessage

def decode(message, shiftNumber):
    encoded_alphabet_array = []
    for i in range(-shiftNumber, 0):
        encoded_alphabet_array.append(alphabet_array[i])
    for i in range(0, 26 - shiftNumber):
        encoded_alphabet_array.append(alphabet_array[i])
    encodedMessage = ""
    for i in message:
        encodedMessage += encoded_alphabet_array[alphabet_array.index(i)]
    return encodedMessage
    

