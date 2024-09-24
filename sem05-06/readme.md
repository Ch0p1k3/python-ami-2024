# "Функции, рекурсии" и "Collections + itertools, регулярные выражения"

[Тетрадка с лекцией "Функции, рекурсии"](https://colab.research.google.com/github/Palladain/Python_1_HSE_2024/blob/main/Lectures/Lecture_04.ipynb)
[Тетрадка с лекцией "Collections + itertools, регулярные выражения"](https://colab.research.google.com/github/Palladain/Python_1_HSE_2024/blob/main/Lectures/Lecture_05.ipynb)

Несколько слов о конструкции:
```python
def main():
    ...


if __name__ == '__main__':
    main()
```
- `def main()` - объявление [функции](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) `main`. Дальше идет блок с кодом, который эта функция выполняет при ее вызове;
- `main()` - вызов функции;
- `if __name__ == '__main__`:
  - `__name__` - аттрибут, в котором следующее значение:
    - когда скрипт запускается напрямую, `__name__` устанавливается в `'__main__'`;
    - когда [модуль](https://docs.python.org/3/tutorial/modules.html) импортируется, `__name__` устанавливается в имя этого модуля;
  - То есть, выражение `if __name__ == '__main__` выполнится только, тогда, когда мы напрямую начнем исполнять файл.
- Плюс этой конструкции:
  - при импорте данного файла, никакой код не запустится, из-за `if __name__ == '__main__`;
  - А функция нужна для того, что бы все объявленные переменные попали в локальную [область видимости](https://www.yuripetrov.ru/edu/python/ch_05_01.html#id27) функции `main`. У `if` нет своей локальной области видимости, в отличие от других языков, например `C++`.
