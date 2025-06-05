from pathlib import Path

file_name = Path.home() / 'PythonProjects' / 'HomeWork' / 'goit-algo-hw-04' / 'total_salary' / 'salaries.txt'
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
            average = int(total / count) if count else 0
            return total, average
    except FileNotFoundError:
        print('File no found')
        return 0, 0
total, average = total_salary(file_name)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")        