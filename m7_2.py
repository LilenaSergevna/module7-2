from pprint import pprint
import io
def custom_write(file_name, strings):
    x=0
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions={}
    for i in strings:
        x=x+1
        strings_positions[x,file.tell()]=i
        txt = file.write(str(i))
        txt = file.write('\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)