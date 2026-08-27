# Проект FitLife - MVP версия 1.0

# Минимальный допустимый возраст
MIN_AGE = 18
# Максимальный допустимый возраст
MAX_AGE = 100

# Минимальный допустимый вес
MIN_WEIGHT = 30
# Максимальный допустимый вес
MAX_WEIGHT = 200

# Минимальный допустимый рост
MIN_HEIGHT = 1.4
# Максимальный допустимый рост
MAX_HEIGHT = 2.2

# Норма воды в миллилитрах
WATER_PER_KG = 30
# Количество милиллитров в литре
ML_IN_LITER = 1000


def get_valid_name(prompt):
    """
    Запрашивает у пользователя имя, пока не будет
    введено непустое значение.

    Args:
        prompt (str): текст вопроса.

    Returns:
        str: корректное имя, которое ввёл пользователь.
    """
    while True:
        name = input(prompt)
        if len(name.strip()) != 0:
            return name
        else:
            print('Имя не может быть пустым или состоять только из пробелов.')


def get_valid_age(prompt, min_age, max_age):
    """
    Запрашивает у пользователя возраст, пока он не станет
    корректным числом в заданном диапазоне.

    Args:
        prompt (str): текст вопроса.
        min_age (int): минимальный допустимый возраст.
        max_age (int): максимальный допустимый возраст.

    Returns:
        int: корректный возраст.
    """
    while True:
        user_input = input(prompt)
        try:
            age = int(user_input)
        except ValueError:
            print(f'Введите целое число от {min_age} до {max_age}.')
            continue
        if min_age <= age <= max_age:
            return age
        else:
            print(
                f'Возраст должен быть в диапазоне'
                f'от {min_age} до {max_age}.'
            )


def get_valid_weight(prompt, min_weight, max_weight):
    """
    Запрашивает у пользователя вес, пока он не станет
    корректным числом в заданном диапазоне.

    Args:
        prompt (str): Текст вопроса.
        min_weight (float): минимальный допустимый вес.
        max_weight (float): максимальный допустимый вес.

    Returns:
        float: корректный вес.
    """
    while True:
        user_input = input(prompt)
        try:
            weight = float(user_input)
        except ValueError:
            print(
                f'Введите чисдо от '
                f'{min_weight} до {max_weight} (например 70.5).'
            )
            continue
        if min_weight <= weight <= max_weight:
            return weight
        else:
            print(
                f'Вес должен быть в диапазоне '
                f'от {min_weight} до {max_weight} (например 70.5).'
            )


def get_valid_height(prompt, min_height, max_height):
    """
    Запрашивает у пользователя рост, пока он не станет
    корректным числом в заданном диапазоне.

    Args:
        prompt (str): Текст вопроса.
        min_height (float): минимальный допустимый рост.
        max_height (float): максимальный допустимый рост.

    Returns:
        float: корректный рост.
    """
    while True:
        user_input = input(prompt)
        try:
            height = float(user_input)
        except ValueError:
            print(
                f'Введите чисдо '
                f'от {min_height} до {max_height} (например 1.75).'
            )
            continue
        if min_height <= height <= max_height:
            return height
        else:
            print(
                f'Рост должен быть в диапазоне '
                f'от {min_height} до {max_height} (например 1.75).')


def get_age_suffix(user_age):
    """
    Определяет правильную форму слова "год" для заданного возраста.

    Args:
        user_age (int): возраст пользователя.

    Returns:
        str: правильная форма слова "год".
    """
    if 11 <= user_age % 100 <= 14:
        return 'лет'
    elif user_age % 10 == 1:
        return 'год'
    elif 2 <= user_age % 10 <= 4:
        return 'года'
    else:
        return 'лет'


def get_bmi_category(bmi):
    """
    Возвращает категорию состояния массы тела по значению ИМТ.

    Args:
        bmi (float): индекс массы тела.

    Returns:
        str: текстовая категория.
    """
    if bmi < 16:
        return 'Выраженный дефицит массы тела.'
    elif 16 <= bmi < 18.5:
        return 'Недостаточная (дефицит) масса тела.'
    elif 18.5 <= bmi < 25:
        return 'Норма.'
    elif 25 <= bmi < 30:
        return 'Избыточная масса тела (предожирение).'
    elif 30 <= bmi < 35:
        return 'Ожирение 1 степени.'
    elif 35 <= bmi < 40:
        return 'Ожирение 2 степени.'
    elif bmi >= 40:
        return 'Ожирение 3 степени.'


# Шаг 1. Знакомство с пользователем
print('Привет! Я фитнес-бот FitLife. Давайте познакомимся!')

user_name = get_valid_name('Как вас зовут? ')
user_age = get_valid_age('Сколько вам лет? ', MIN_AGE, MAX_AGE)

# Шаг 2. Сбор параметров и расчёты
user_weight = get_valid_weight('Ваш вес в кг? ', MIN_WEIGHT, MAX_WEIGHT)
user_height = get_valid_height('Ваш рост в метрах? ', MIN_HEIGHT, MAX_HEIGHT)

# Расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# Расчёт нормы воды в литрах
water_l = round((user_weight * WATER_PER_KG) / ML_IN_LITER, 1)

# Правильная форма слова "год"
age_suffix = get_age_suffix(user_age)


# Шаг 3. Вывод результата
print('\n' + '=' * 40)
print(f'Отчёт для пользователя: {user_name} ({user_age} {age_suffix}).')
print(f'Вес: {user_weight} кг. | Рост: {user_height} м.')
print(f'Индекс массы тела (ИМТ): {bmi}. {get_bmi_category(bmi)}')
print(f'Рекомендуемая норма воды: {water_l} л. в день.')
print('=' * 40)
print('Расчёт окончен. Будьте здоровы!')
