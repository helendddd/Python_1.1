# Программа переводит градусы в Фарингейты
# или Фарингейты в градусы Цельсия

t = int(input("Введите температуру: ")) #Ввод температуры
sms = input("Перевести в Цельсия/Фарингейта : (True/False) ") # Программа уточняет

if sms == "True":
    ans = (t - 32) / 1.8
    ans = int(ans)
    print (ans)
elif sms == "False":
    ans = t * 1.8 + 32
    ans = int(ans)
    print (ans)
else:
    print ("Неверные данные")

