char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#type_operation = input("Encode or Decode: ").lower()
msg = input("message: ")

def encode(msg):
    result_list = []
    
    for letters in msg:
        
        for i in range(0,len(char)-1):
            if letters == char[i]:
                result_list.append(char[i+2])
                break
            else:
                result_list.append(letters)
    result = "".join(result_list)
    return result

print(encode(msg))

"""
def decode(msg):
    result_list = []
    result = "".join(result_list)
    for letters in msg:
        
        for i in range(0,len(char)-1):
            if letters == char[i]:
                result_list.append(char[i-2])
                break
            else:
                result_list.append(letters)
    return result

if type_operation == "encode":
    encode(msg)
elif type_operation == "decode":
    decode(msg)
"""