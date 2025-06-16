char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run_code = True
while run_code:

    type_operation = input("Encode or Decode: ").lower()
    def encode(msg):
        result_list = []
        n = len(char)  # Calculate once outside loop
        
        for letter in msg:
            found = False
            for i in range(n):
                if letter == char[i]:
                    new_index = i + 2
                    if new_index >= n:
                        new_index -= n  # Wrap around
                    result_list.append(char[new_index])
                    found = True
                    break
            if not found:
                result_list.append(letter)
        return "".join(result_list)
    
    decode_char = list(reversed(char))

    def decode(msg):
        result_list = []
        n = len(decode_char)
        
        for letter in msg:
            found = False
            for i in range(n):
                if letter == decode_char[i]:
                    new_index = i + 2  # Shift forward in reversed list
                    if new_index >= n:
                        new_index -= n
                    result_list.append(decode_char[new_index])
                    found = True
                    break
            if not found:
                result_list.append(letter)
        return "".join(result_list)



    if type_operation == "encode":
        msg = input("message: ")
        print(encode(msg))
    elif type_operation == "decode":
        msg = input("message: ")
        print(decode(msg))
    elif type_operation =="break":
        run_code = False

    else:
        print("wrong input")
        
