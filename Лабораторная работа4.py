if name == "__main__":
    class _SONG:
        def __init__(self, name_of_song: str, performer_of_song: str, duration_of_song: float):
            """
            Иницилизация полей класса
            :param name_of_song: Название песни
            :param performer_of_song: Исполнитель песни
            :param duration_of_song: Длительность песни
            Примеры:
            >>>  Lovewholovesyouback = _SONG('Love who loves you back', 'Tokio Hotel', 3.40) # инициализация экземпляра класса
             """
            self.name_of_song = name_of_song  # защищенный атрибут, название песни
            self.performer_of_song = performer_of_song  # защищенный атрибут, исполнитель песни
            self.duration_of_song = duration_of_song  # защищенный атрибут, длительность песни

        def __str__(self) -> str:
            return f'Песня "{self.name_of_song}". Жанр: {self.performer_of_song}'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(name_of_song = {self.name_of_song!r}, genre_of_song = {self.performer_of_song})'

        def check_duration_of_song(self, place_of_song: float) -> float:
            """
            С помощью этой функций совршается проверка длительности песни.
            :param place_of_song: Какое время песни уже проиграно
            Примеры:
            >>> time = _SONG('Love who loves you back', 'Tokio Hotel', 3.40)
            >>> time.place_of_song(3.40)
            """
            if place_of_song <= self.duration_of_song:
                raise ValueError('Песня еще играет')
            return place_of_song = duration_of_song


    class ROCKSONG(_SONG):
        def __init__(self, name_of_song: str, performer_of_song: str, duration_of_song: float, genre_of_song: str):
            """
            Создание и подготовка к работе объекта "Pop Song"
            :param name_of_song: Название песни
            :param performer_of_song: Исполнитель песни
            :param duration_of_song: Длительность песни
            :param genre_of_song: Жанр песни
            Примеры:
            >>> CountingStars = ROCKSONG('Counting stars', 'One republic', 4.17, 'Rock') # инициализация экземпляра класса
             """
            super().__init__(name_of_song, performer_of_song, duration_of_song)
            self.genre_of_Song = genre_of_song  # защищенный атрибут, жанр песни

        def __str__(self) -> str:
            return f'Песня "{self.name_of_song}". Исполнитель: {self.performer_of_song}. Длительность песни {self.duration_of_song}. Жанр песни {self.genre_of_Song} '

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(name_of_song = {self.name_of_song!r}, performer_of_song = {self.performer_of_song}, duration_of_song = {self.duration_of_song}, genre_of_song = {self.genre_of_song})'


    class VINTAGESONG(_SONG):
        def __init__(self, name_of_song: str, performer_of_song: str, duration_of_song: float, year_of_song: int):
            """
            Создание и подготовка к работе объекта "ArcadeGame"
           :param name_of_song: Название песни
            :param performer_of_song: Исполнитель песни
            :param duration_of_song: Длительность песни
            :param year_of_song: Год выпуска песни
            Примеры:
            >>> Alexandra = VINTAGESONG('Alexandra', 'Tatyana Nikitina', 3.39, 1) # инициализация экземпляра класса
             """
            super().__init__(name_of_song, performer_of_song, duration_of_song)
            self.year_of_song = year_of_song  # защищенный атрибут, год выпуска песни

        def __str__(self) -> str:
            return f'Песня "{self.name_of_song}". Исполнитель: {self.performer_of_song}. Длительность песни {self.duration_of_song}. Год выпуска песни: {self.year_of_song}.'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(name_of_song = {self.name_of_song!r}, performer_of_song = {self.performer_of_song}, duration_of_song = {self.duration_of_song},year_of_song = {self.year_of_song}'
