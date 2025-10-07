#1. Екі санның минимумын табу
a = int(input("Бірінші санды енгіз: "))
b = int(input("Екінші санды енгіз: "))

if a < b:
    print("Кіші сан:", a)
else:
    print("Кіші сан:", b)

#2. Жұп немесе тақ
n = int(input("Санды енгіз: "))

if n % 2 == 0:
    print("Сан жұп")
else:
    print("Сан тақ")

#3. 1-ден N-ге дейінгі сандардың қосындысы
N = int(input("N санын енгіз: "))
total = 0

for i in range(1, N + 1):
    total += i

print("Қосынды:", total)

#4. Көбейту кестесі
N = int(input("Санды енгіз: "))

for i in range(1, 11):
    print(f"{N} x {i} = {N * i}")

#5. Факториалды табу
N = int(input("N санын енгіз: "))
fact = 1

for i in range(1, N + 1):
    fact *= i

print("Факториал:", fact)

#6. Дауысты әріптердің саны
text = input("Жол енгіз: ")
vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Дауысты әріптер саны:", count)

#7. Жолды кері шығару
text = input("Жол енгіз: ")
print("Кері жол:", text[::-1])

#8. Массивтегі максимумды табу
arr = list(map(int, input("Массив элементтерін енгіз: ").split()))
print("Максимум:", max(arr))

#9. Массив элементтерінің қосындысы
arr = list(map(int, input("Массив элементтерін енгіз : ").split()))
print("Қосынды:", sum(arr))

#10. Массивтен элемент іздеу
arr = list(map(int, input("Массив элементтерін енгіз: ").split()))
x = int(input("Іздейтін элементті енгіз: "))

if x in arr:
    print("Элемент бар")
else:
    print("Элемент жоқ")