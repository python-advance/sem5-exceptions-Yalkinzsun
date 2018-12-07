import csv
from prettytable import PrettyTable 
from contextlib import contextmanager
 
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
 
def csv_reader(file_obj):
    """
    Read a csv file
    """
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
    #print(" ".join(row))

if __name__ == "__main__":
  with open_file('titanic.csv') as f_obj:
        csv_reader(f_obj)
