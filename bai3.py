a = float(input("Input number a: "))
b = float(input("Input number b: "))
c = float(input("Input number c: "))

def classify_triangle(a, b, c):
    # Kiểm tra điều kiện của bất đẳng thức tam giác
    if not (a + b > c and a + c > b and b + c > a):
        return 0
    
    # Sắp xếp các cạnh theo thứ tự tăng dần
    slides = sorted([a, b, c])
    a, b,c = slides[0], slides[1], slides[2]

    # Kiểm tra loại tam giác dựa vào bình phương của các cạnh
    if a**2 + b**2 > c**2:
        return 1  # Tam giác nhọn
    elif a**2 + b**2 == c**2:
        return 2  # Tam giác vuông
    else:
        return 3  # Tam giác tù
    
result = classify_triangle(a, b, c)
print(result)