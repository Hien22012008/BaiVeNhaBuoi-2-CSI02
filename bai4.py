def min_switches_to_unify_lights(lights):
    # Đếm số bóng đèn mở và tắt
    count_open = sum(lights)
    count_closed = len(lights) - count_open
    
    # Số lần ấn công tắc ít nhất là số bóng đèn ít hơn cần thay đổi
    return min(count_open, count_closed)


n = int(input("Input number of the lights: "))
arr = [True, True, False]
result = min_switches_to_unify_lights(arr)
print(result) 