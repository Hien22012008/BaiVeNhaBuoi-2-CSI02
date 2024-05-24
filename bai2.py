n = int(input("Input number: "))

def is_prime(num):
     # Kiểm tra xem số num có phải là số nguyên tố hay không
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_superprime(num):
        # Kiểm tra xem số num có phải là số siêu nguyên tố hay không
    if not is_prime(num):
        return False
    num_str = str(num)
    for i in range(1, len(num_str)):
        truncated_num = int(num_str[:-i])
        if not is_prime(truncated_num):
            return False
    return True

result = is_superprime(n)

print("True" if result else "False")