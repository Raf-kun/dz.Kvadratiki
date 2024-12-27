num = int(input("Введите четырехзначное число: "))

hundreds = num // 100 % 10
thousands = num // 1000

print(f"Число {num}, содержит вот столько то сотен - {hundreds}, содержит вот столько то тысяч - {thousands}")