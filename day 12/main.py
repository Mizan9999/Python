def is_prime(num):
    break_code = "True"

    for i in range(2,num):
        if num % i == 0:
            print(i)
            break_code = False
            break
    
    return break_code


print(is_prime(5))