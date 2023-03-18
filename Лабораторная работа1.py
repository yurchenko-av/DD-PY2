class Mouse:
    def __init__(self, color: str, number_of_ears, model_type: str):
        if not isinstance(color, str):
            raise TypeError('Название цвета str')
        self.color = color
        if number_of_ears < 0:
            raise TypeError('Количество ушек не может быть отрицательным числом.')
        self.number_of_ears = number_of_ears
        if not isinstance(model_type, str):
            raise TypeError('Модель str')
        self.model_type = model_type
    def broken(self):
        print('Это не лабораторная мышь')
        self.health = 0

class Research:
    def __init__(self, aim: str, number_of_repeat: int, result: str):
        if not isinstance(aim, str):
            raise TypeError('Цель эксперимента должна быть типа str')
        self.aim = aim
        if not number_of_repeat > 3:
            raise ValueError('Для достоверности эксперимента количество повторов должно быть не меньше 3')
        self.number_of_repeat = number_of_repeat
        if not isinstance(result, str):
            raise ValueError('Результат должны быть записан в виде str')
        self.result = result

class Thesis:
    def __init__(self, number_of_words: int, heading: str):
        if not isinstance(number_of_words, int):
            raise TypeError('Количество слов должно быть числом')
        if number_of_words > 500:
            raise ValueError('Количество слов не должно превышать 500')
        self.number_of_words = number_of_words
        if not isinstance(heading, str):
            raise TypeError('Название str')
        self.heading = heading

if __name__ == "__main__":
    CVS_mouse_model = Mouse('Белая', 2, 'Chronic variable stress')
    In_vitro_transcription = Research('Проверить функциональность T7 полимеразы', 10, 'РНК получена, полимераза работает')
    IVT_conditions = Thesis(488, 'Проверка условий IVT')
    import doctest
    doctest.testmod()
    pass