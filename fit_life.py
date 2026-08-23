# Проект FitLife - MVP версия 1.0

# Норма воды в миллилитрах
WATER_PER_KG = 30

# Количество милиллитров в литре
ML_IN_LITER = 1000

# Шаг 1. Знакомство с пользователем
print('Привет! Я фитнес-бот FitLife. Давайте познакомимся!')
user_name = input('Как вас зовут? ').strip().title()

user_age = int(input('Сколько вам лет? ').strip())

# Шаг 2. Сбор параметров и расчёты
user_weight = float(input('Ваш вес (в кг) (например 70.5): ').strip())

user_height = float(input('Ваш рост в метрах (например 1.75): ').strip())

# Расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Расчёт нормы воды в литрах
water_l = round((user_weight * WATER_PER_KG) / ML_IN_LITER, 1)

# Определяем правильную форму слова "год" для заданного возраста
if 11 <= user_age % 100 <= 14:
    year = 'лет'
elif user_age % 10 == 1:
    year = 'год'
elif 2 <= user_age % 10 <= 4:
    year = 'года'
else:
    year = 'лет'

# Шаг 3. Вывод результата
print('\n' + '=' * 40)
print(f'Отчёт для пользователя: {user_name} ({user_age} {year})')
print(f'Вес: {user_weight} кг | Рост: {user_height} м')
print(f'Индекс массы тела (ИМТ): {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print('=' * 40)
print('Расчёт окончен. Будьте здоровы!')
