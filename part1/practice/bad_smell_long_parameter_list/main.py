# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)
# ----------------------------------------------------------------------


class Unit:

    def __init__(self, move_type: str, speed: int):

        self._pos_x = 0
        self._pos_y = 0
        self._move_type = move_type
        self._speed = self._get_speed(speed)

    def _get_speed(self, speed: int):

        if self._move_type == "FLY":
            return speed * 1.2

        elif self._move_type == "CRAWL":
            return speed * 0.5

        else:
            raise ValueError("Unknown move type")

    def move(self, direction):

        if direction == 'UP':
            self._pos_y += self._speed

        elif direction == 'DOWN':
            self._pos_y -= self._speed

        elif direction == 'LEFT':
            self._pos_x -= self._speed

        elif direction == 'RIGHT':
            self._pos_x += self._speed

        else:
            raise ValueError("Unknown direction")

#     ...
