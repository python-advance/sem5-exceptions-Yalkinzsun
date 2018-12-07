import json

def FromJsonToTable(filename):
  try:
    file = open(filename,'rb')
  except IOError:
    print('Файл отсутствует!')
    exit(0)
  else:
    data = json.load(file)
    file.close()

  #использование менеджера контекста
  with open(filename,'r') as data_file:    
     data = json.load(data_file)

  name, surname, sex, birth, nationality = [],[],[],[],[]
  for i in range(len(data["fields"])):
    name.append(data["fields"][i]["name"])
    surname.append(data["fields"][i]["surname"])
    sex.append(data["fields"][i]["sex"])
    birth.append(data["fields"][i]["date of birth"])
    nationality.append(data["fields"][i]["nationality"])

  titles = ['name', 'surname', 'sex', 'birth', 'nationality']
  dt = [titles] + list(zip(name, surname, sex, birth, nationality))
  try:
    iter(dt)
  except TypeError:
    print(" Не итеребл")

  for i, d in enumerate(dt):
      line = ' '.join(str(x).ljust(14) for x in d)
      print(line)
      if i == 0:
          print('-' * len(line))
  return len(data["fields"]) 

if __name__ == "__main__":
  FromJsonToTable('json.json')
  