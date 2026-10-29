# geometric_lib

Небольшая библиотека для вычисления площади и периметра круга, прямоугольника, квадрата и треугольника.

## Состав приложения

| Модуль | Функции |
| --- | --- |
| `circle.py` | `area(r)`, `perimeter(r)` |
| `rectangle.py` | `area(a, b)`, `perimeter(a, b)` |
| `square.py` | `area(a)`, `perimeter(a)` |
| `triangle.py` | `area(a, h)`, `perimeter(a, b, c)` |

Функции принимают числа `int` или `float`. Проверка корректности геометрических размеров не выполняется.

## Круг

### `area(r)`

Возвращает площадь круга по формуле `S = πr²`.

- `r` — радиус круга.

```python
from app.circle import area

area(5)  # 78.53981633974483
```

### `perimeter(r)`

Возвращает длину окружности по формуле `P = 2πr`.

- `r` — радиус круга.

```python
from app.circle import perimeter

perimeter(5)  # 31.41592653589793
```

## Прямоугольник

### `area(a, b)`

Возвращает площадь прямоугольника по формуле `S = ab`.

- `a`, `b` — длины сторон.

```python
from app.rectangle import area

area(3, 4)  # 12
```

### `perimeter(a, b)`

Возвращает периметр прямоугольника по формуле `P = 2(a + b)`.

- `a`, `b` — длины сторон.

```python
from app.rectangle import perimeter

perimeter(3, 4)  # 14
```

## Квадрат

### `area(a)`

Возвращает площадь квадрата по формуле `S = a²`.

- `a` — длина стороны.

```python
from app.square import area

area(5)  # 25
```

### `perimeter(a)`

Возвращает периметр квадрата по формуле `P = 4a`.

- `a` — длина стороны.

```python
from app.square import perimeter

perimeter(5)  # 20
```

## Треугольник

### `area(a, h)`

Возвращает площадь треугольника по формуле `S = ah / 2`.

- `a` — длина основания;
- `h` — высота к основанию.

```python
from app.triangle import area

area(4, 3)  # 6.0
```

### `perimeter(a, b, c)`

Возвращает периметр треугольника по формуле `P = a + b + c`.

- `a`, `b`, `c` — длины сторон.

```python
from app.triangle import perimeter

perimeter(3, 4, 5)  # 12
```

## Запуск тестов

Из корня репозитория:

```bash
python -m unittest discover -s tests -v
```
