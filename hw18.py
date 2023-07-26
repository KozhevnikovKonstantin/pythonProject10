num = int(input("Введите количество билетов"))
age = []
for i in range(num):
    age.append(int(input("Введите возраст посетителя № " + str(i+1))))
count_child = 0
count_stud = 0
count_adult = 0
for i in age:
    if 0<i<18:
        count_child += 1
    elif 18<=i<25:
        count_stud += 1
    else:
        count_adult += 1
cost = count_stud*990 + count_adult*1390
if num>3:
    print("Общая стоимость заказа: " + str(cost*0.9))
else:
    print("Общая стоимость заказа: " + str(cost))