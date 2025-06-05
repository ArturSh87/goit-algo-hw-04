from pathlib import Path

file_name = Path.home() /'PythonProjects' / 'HomeWork' / 'goit-algo-hw-04' / 'get_cats_info' / 'cats.txt'
def get_cats_info(path):  
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats =[]
            for line in file:
                parts = line.strip().split(',')
                cat_dict = {'id': parts[0], 'name': parts[1], 'age':parts[2]}
                cats.append(cat_dict)
            return cats 
    except FileNotFoundError:
        print("File not found")
print(file_name)        
cats_info = get_cats_info(file_name)
print(cats_info)


