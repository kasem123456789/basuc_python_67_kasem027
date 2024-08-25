odd_numbers = [] #เลขคี่
even_numbers = [] #เลขคู่

for numbers in range(21, 41):# วนลูปตั้งแต่ 21 ถึง 40
    if numbers % 2 == 0: #ถ้าหาร 2 ลงตัว แสดงว่าเป็นเลขคู่
        even_numbers.append(numbers)
    else: #ถ้าไม่ลงตัว แสดงว่าเป็นเลขคี่
        odd_numbers.append(numbers)

print("เลขคี่:", odd_numbers)
print("เลขคู่:", even_numbers)

#นายเกษม เกษมสุข 6749010027