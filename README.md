## Исключения

**Инвариантная самостоятельная работа**

1.1. Разработать программу с реализацией функции для считывания json- данных из файла и вывод их в табличном виде на экран. Реализовать базовый синтаксис для обработки исключений (try .. except) 

Часть содержимого фала JSON:

```
{
	  "tablename": "Табличка",
	  "fields": [
	      {
	        "name": "Catherin",
	        "surname":"Geberg",
            "sex":"female",
            "date of birth":"13.04.1965",
            "nationality":"Australian"
	      },
	      {
	        "name": "Eustathies",
	        "surname":"Varfolomeyev",
            "sex":"male",
            "date of birth":"01.01.1992",
            "nationality":"Russian"
	      },
          ...
   ]
}
```

Для работы со данными JSON необходимо подключить одноимённую библиотеку: 

```python
import json
```
Функция принимает в качестве единственного аргумента имя файла:
```Python
def FromJsonToTable(filename):
  try:
    file = open(filename,'rb')
  except IOError:
    print('Файл отсутствует!')
    exit(0)
  else:
    data = json.load(file)
    file.close()
    ...
```
Конструкция **try .. except** обрабатывает исключиние, которое может возникнуть при попытки открытия файла (файла не существует). Если такое исключение поднимается, выводится сообщение об ошибке и программа завершается. Если открытие произошло успешно, в переменную *data* помещается JSON c помощью метода **.load()**

Для каждого элемента из списка, являющимся значением для ключа **"fields"** (количество этих элементов лего узнать с помощью функции `len()`), помещаем значения для нужных нам ключей этого элемента в дополнительные списки:

 ``` python
  name, surname, sex, birth, nationality = [],[],[],[],[]
  for i in range(len(data["fields"])):
    name.append(data["fields"][i]["name"])
    surname.append(data["fields"][i]["surname"])
    sex.append(data["fields"][i]["sex"])
    birth.append(data["fields"][i]["date of birth"])
    nationality.append(data["fields"][i]["nationality"])
 ```

Данные можно представить в табличном ввиде с  помощью встроенных функций языка и сторонних библиотек. Первый способ:
```python
titles = ['name', 'surname', 'sex', 'birth', 'nationality']
  dt = [titles] + list(zip(name, surname, sex, birth, nationality))
    
  for i, d in enumerate(dt):
      line = ' '.join(str(x).ljust(14) for x in d)
      print(line)
      if i == 0:
         print('-' * len(line))
```

Второй способ - использование библиотеки PrettyTable:

```Python 
from prettytable import PrettyTable
x = PrettyTable()
column_names = ['name', 'surname', 'sex', 'birth', 'nationality']
x.add_column(column_names[0], name)
x.add_column(column_names[1], surname)
x.add_column(column_names[2], sex)
x.add_column(column_names[3], birth)
x.add_column(column_names[4], nationality)
print(x)
```

Результат:

```
+------------+--------------+--------+------------+-------------+
|    name    |   surname    |  sex   |   birth    | nationality |
+------------+--------------+--------+------------+-------------+
|  Catherin  |    Geberg    | female | 13.04.1965 |  Australian |
| Eustathies | Varfolomeyev |  male  | 01.01.1992 |   Russian   |
|  Gertrude  |  Wolemasen   | female | 09.08.1998 |   Finnish   |
|  Kurpusha  |  Fedorovna   | female | 31.05.1968 |  Ukrainian  |
|   Huang    |     Gong     |  male  | 28.03.1974 |   Chinese   |
+------------+--------------+--------+------------+-------------+
```

1.2. Дополнение программы для считывания данных проверкой утверждений или высказываний (assert). Создание отдельного блока для такой проверки (с помощью __name__) и скрипта командной строки для запуска этих проверок. 

Для первого способа вывода таблицы можно использовать проверку итерабельности объекта:

```python
titles = ['name', 'surname', 'sex', 'birth', 'nationality']
dt = [titles] + list(zip(name, surname, sex, birth, nationality))
try:
  iter(dt)
except TypeError:
  print(" Не iterable-объект!")
```

Функция **iter()** попытается получить итератора из объекта **dt**, и если при этом поднимитьь исключение **TypeError**, то можно будет сделать вывод о неитерируемости объекта.

Для создания теста с использованием библиотеки **pytest** был создан отдельный файл со следующим содержимым:

```python
import pytest
import main

def testing_fun1():
    assert main.FromJsonToTable('json.json') == 5, '1'
```

Функция возвращает количество элементов из списка, являющимся значением для ключа **"fields"**. Для текущего JSON - файла их 5

Чтобы найти все тесты в папке и во вложенных папках и запустить их необходимо выполнить команду в консоли: 

```
python -m pytest
```

Найти и запустить тесты в указанном файле: 

```
python -m pytest -q main.py
```

(Важно) имя теста должно начинаться с test_* для поиска пакетов

1.3. Дополнение программы для считывания данных с использованием менеджера контекстов 

```python
#использование менеджера контекста
  with open(filename,'r') as data_file:    
data = json.load(data_file)
```
**Вариативная самостоятельная работа**

1.3. Создание программы для считывания данных формата CSV c использованием функционала модуля contextlib. 

Необходимо импортировать библиотеки *scv*, *contextlib* и *PrettyTable*

Главная функция, принимающая на вход scv-файл:

```python
def csv_reader(file_obj):
    x = PrettyTable()
    reader = csv.reader(file_obj)
    x.field_names = next(reader)

    for row in reader:
        a =[]
        for item in row:
          a.append(item)
        x.add_row(a)

    print(x)
    with open('table.txt', 'w') as f:
       f.write(x.get_string())
```

Для получения первой строчки *scv*-файла и отсутсвия её при следующей итерации используется функция `next()`, вызывающая метод `__next__()` указанного объекта для получения следующего элемента.

Создание менеджера контекста с помощью модуля *contextlib* (используется специальный декоратор *@contextmanager*):

```Python
@contextmanager 
def open_file(file):
    try:
        data = open(file, 'r')
        yield data
    except OSError:
        print("Ошибка при открытии файла")
        exit(0)
    else:
        print('Закрываем файл...')
        data.close()
```

Часть итоговой таблицы:

```python
+-------------+----------+--------+------------------------------------------------------------------------------------+--------+------+-------+-------+--------------------+----------+-----------------+----------+
| PassengerId | Survived | Pclass |                                        Name                                        |  Sex   | Age  | SibSp | Parch |       Ticket       |   Fare   |      Cabin      | Embarked |
+-------------+----------+--------+------------------------------------------------------------------------------------+--------+------+-------+-------+--------------------+----------+-----------------+----------+
|      1      |    0     |   3    |                              Braund, Mr. Owen Harris                               |  male  |  22  |   1   |   0   |     A/5 21171      |   7.25   |                 |    S     |
|      2      |    1     |   1    |                Cumings, Mrs. John Bradley (Florence Briggs Thayer)                 | female |  38  |   1   |   0   |      PC 17599      | 71.2833  |       C85       |    C     |
|      3      |    1     |   3    |                               Heikkinen, Miss. Laina                               | female |  26  |   0   |   0   |  STON/O2. 3101282  |  7.925   |                 |    S     |
|      4      |    1     |   1    |                    Futrelle, Mrs. Jacques Heath (Lily May Peel)                    | female |  35  |   1   |   0   |       113803       |   53.1   |       C123      |    S     |

```



