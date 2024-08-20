import numpy as np
import sys
def simplex_method(c, A, b,num_vars):
    m, n = len(A), len(A[0])
    if len(c) != n or len(b) != m:
        with open('primary_table.txt', 'w', encoding='utf-8') as file:
         f.write("Неправильные размерности матриц")
         print("Неправильные размерности матриц")
         sys.exit()

    c += [0] * m
    A = [row + [1 if i == j else 0 for j in range(m)] for i, row in enumerate(A)]
    basis = list(range(n, n + m))
    
    c1 = c
    num_tables = 0
    F_values = [0]
    result = 0

    while True:
        num_tables += 1
        c2 = c
      
        entering_variable = c.index(max(c))

        if c[entering_variable] <= 0:
            break

        if napr == 'max':
           if tr == 'Yes':
            ratios = [b[i] / A[i][entering_variable] if A[i][entering_variable] > 0 else float('inf') for i in range(m)]
            if all(ratio == float('inf') for ratio in ratios):
                   with open('primary_table.txt', 'a', encoding='utf-8') as file:
                    file.write(f"Функция не ограничена. Оптимальное решение отсутствует.")
                   print("Функция не ограничена. Оптимальное решение отсутствует.")
                   sys.exit()
            theta = min([ratios[i] for i in range(m) if A[i][entering_variable] > 0])
    
            table = [['C'] + c1 + [0.0]] + [['Б'] + ['x{}'.format(i+1) for i in range(m)] + ['x{}'.format(i+1) for i in range(m, m+num_vars)]  + ['b']]
            for i, row in enumerate(A):
                ratios = [b[i] / A[i][entering_variable] if A[i][entering_variable] > 0 else float('inf') for i in range(m)]
                leaving_variable = ratios.index(min(ratios))
                theta = b[leaving_variable] / A[leaving_variable][entering_variable]
                if i != leaving_variable:
                    table.append(['x{}'.format(basis[i]+1) if i < len(basis) else 'x{}'.format(i-len(basis)+1+m)] + [float("{:.1f}".format(col)) if col % 1 != 0 else int(col) for col in row] + [float("{:.1f}".format(b[i])) if b[i] % 1 != 0 else int(b[i])] + [float("{:.1f}".format(ratios[i])) if ratios[i] != float('inf') else '-'] + [float("{:.1f}".format(theta)) if i == leaving_variable else ''])
                else:
                    table.append(['x{}'.format(basis[i]+1) if i < len(basis) else 'x{}'.format(i-len(basis)+1+m)] + [float("{:.1f}".format(col)) if col % 1 != 0 else int(col) for col in row] + [float("{:.1f}".format(b[i])) if b[i] % 1 != 0 else int(b[i])] + [float("{:.1f}".format(ratios[i])) if ratios[i] != float('inf') else '-'] + [''])
    
            c2_neg = [-1 * round(float("{:.1f}".format(col)), 1) for col in c2]
            table.append(['F(x)'] + c2_neg + F_values)
            with open('primary_table.txt', 'a', encoding='utf-8') as file:
                file.write(f"\nИтерация {num_tables}:\n")
                for row in table:
                    file.write(''.join(['{:<10}'.format(str(elem)) for elem in row]) + '\n')
           if tr == 'No':
             ratios = [b[i] / A[i][entering_variable] if A[i][entering_variable] > 0 else float('inf') for i in range(m)]
             leaving_variable = ratios.index(min(ratios))
        if napr == 'min':
           if tr == 'Yes':
            ratios = [b[i] / A[i][entering_variable] if A[i][entering_variable] > 0 else float('inf') for i in range(m)]
            if all(ratio == float('inf') for ratio in ratios):
                   with open('primary_table.txt', 'a', encoding='utf-8') as file:
                    file.write(f"Функция не ограничена. Оптимальное решение отсутствует.")
                   print("Функция не ограничена. Оптимальное решение отсутствует.")
                   sys.exit()
            theta = min([ratios[i] for i in range(m) if A[i][entering_variable] > 0])
    
            table = [['C'] + c1 + [0.0]] + [['Б'] + ['x{}'.format(i+1) for i in range(m)] + ['x{}'.format(i+1) for i in range(m, m+num_vars+1)] +  ['b']]
            for i, row in enumerate(A):
                ratios = [b[i] / A[i][entering_variable] if A[i][entering_variable] > 0 else float('inf') for i in range(m)]
                leaving_variable = ratios.index(min(ratios))
                theta = b[leaving_variable] / A[leaving_variable][entering_variable]
                if i != leaving_variable:
                    table.append(['x{}'.format(basis[i]+1) if i < len(basis) else 'x{}'.format(i-len(basis)+1+m)] + [float("{:.1f}".format(col)) if col % 1 != 0 else int(col) for col in row] + [float("{:.1f}".format(b[i])) if b[i] % 1 != 0 else int(b[i])] + [float("{:.1f}".format(ratios[i])) if ratios[i] != float('inf') else '-'] + [float("{:.1f}".format(theta)) if i == leaving_variable else ''])
                else:
                    table.append(['x{}'.format(basis[i]+1) if i < len(basis) else 'x{}'.format(i-len(basis)+1+m)] + [float("{:.1f}".format(col)) if col % 1 != 0 else int(col) for col in row] + [float("{:.1f}".format(b[i])) if b[i] % 1 != 0 else int(b[i])] + [float("{:.1f}".format(ratios[i])) if ratios[i] != float('inf') else '-'] + [''])
 
            c2_neg = [-1 * round(float("{:.1f}".format(col)), 1) for col in c2]
            table.append(['F(x)'] + c2_neg + F_values)
            with open('primary_table.txt', 'a', encoding='utf-8') as file:
                file.write(f"\nИтерация {num_tables}:\n")
                for row in table:
                    file.write(''.join(['{:<10}'.format(str(elem)) for elem in row]) + '\n')
           if tr == 'No':
            ratios = [b[i] / A[i][entering_variable] if A[i][entering_variable] > 0 else float('inf') for i in range(m)]
            leaving_variable = ratios.index(min(ratios))

        basis[leaving_variable] = entering_variable

        pivot = A[leaving_variable][entering_variable]
        A[leaving_variable] = [x / pivot for x in A[leaving_variable]]
        b[leaving_variable] /= pivot

        for i in range(m):
            if i != leaving_variable:
                factor = A[i][entering_variable]
                A[i] = [A[i][j] - factor * A[leaving_variable][j] for j in range(n + m)]
                b[i] -= factor * b[leaving_variable]
  
        c = [c[j] - c[entering_variable] * A[leaving_variable][j] for j in range(n + m)]

        result = [0] * n
        for i in range(m):
            if basis[i] < n:
                result[basis[i]] = b[i]

        F_values[0] = (round(sum(c1[i]*result[i] for i in range(len(result))), 1))
        
        if b[i] < 0:
              with open('primary_table.txt', 'a', encoding='utf-8') as file:
                 file.write(f"\nЗадача не имеет решения\n")
                 sys.exit()
        
    if napr == "max":
       if tr == 'Yes':
         table = [['C'] + c1 + [0.0]] + [['Б'] + ['x{}'.format(i+1) for i in range(m)] + ['x{}'.format(i+1) for i in range(m, m+num_vars)] + ['b']]
         for i, row in enumerate(A):
             ratios = [b[i] / A[i][entering_variable] if A[i][entering_variable] > 0 else float('inf') for i in range(m)]
             leaving_variable = ratios.index(min(ratios))
             theta = b[leaving_variable] / A[leaving_variable][entering_variable]
             if i != leaving_variable:
                  table.append(['x{}'.format(basis[i]+1) if i < len(basis) else 'x{}'.format(i-len(basis)+1+m)] + [float("{:.1f}".format(col)) if col % 1 != 0 else int(col) for col in row] + [float("{:.1f}".format(b[i])) if b[i] % 1 != 0 else int(b[i])] + [float("{:.1f}".format(ratios[i])) if ratios[i] != float('inf') else '-'] + [float("{:.1f}".format(theta)) if i == leaving_variable else ''])
             else:
                  table.append(['x{}'.format(basis[i]+1) if i < len(basis) else 'x{}'.format(i-len(basis)+1+m)] + [float("{:.1f}".format(col)) if col % 1 != 0 else int(col) for col in row] + [float("{:.1f}".format(b[i])) if b[i] % 1 != 0 else int(b[i])] + [float("{:.1f}".format(ratios[i])) if ratios[i] != float('inf') else '-'] + [''])
         c2_neg = [-1 * round(float("{:.1f}".format(col)), 1) for col in c2]
         table.append(['F(x)'] + c2_neg + F_values)
         with open('primary_table.txt', 'a', encoding='utf-8') as file:
             file.write(f"\nФинальная:\n")
             for row in table:
                 file.write(''.join(['{:<10}'.format(str(elem)) for elem in row]) + '\n')
         if b[i] < 0:
             print(f"Задача не имеет решения")
             with open('primary_table.txt', 'a', encoding='utf-8') as file:
                file.write(f"\nЗадача не имеет решения\n")
                sys.exit()
       if tr == 'No':
          pass
    if napr == 'min':
       if tr == 'Yes':
            ratios = [b[i] / A[i][entering_variable] if A[i][entering_variable] > 0 else float('inf') for i in range(m)]
            theta = min([ratios[i] for i in range(m) if A[i][entering_variable] > 0])
    
            table = [['C'] + c1 + [0.0]] + [['Б'] + ['x{}'.format(i+1) for i in range(m)] + ['x{}'.format(i+1) for i in range(m, m+num_vars+1)] +  ['b']]
            for i, row in enumerate(A):
                ratios = [b[i] / A[i][entering_variable] if A[i][entering_variable] > 0 else float('inf') for i in range(m)]
                leaving_variable = ratios.index(min(ratios))
                theta = b[leaving_variable] / A[leaving_variable][entering_variable]
                if i != leaving_variable:
                    table.append(['x{}'.format(basis[i]+1) if i < len(basis) else 'x{}'.format(i-len(basis)+1+m)] + [float("{:.1f}".format(col)) if col % 1 != 0 else int(col) for col in row] + [float("{:.1f}".format(b[i])) if b[i] % 1 != 0 else int(b[i])] + [float("{:.1f}".format(ratios[i])) if ratios[i] != float('inf') else '-'] + [float("{:.1f}".format(theta)) if i == leaving_variable else ''])
                else:
                    table.append(['x{}'.format(basis[i]+1) if i < len(basis) else 'x{}'.format(i-len(basis)+1+m)] + [float("{:.1f}".format(col)) if col % 1 != 0 else int(col) for col in row] + [float("{:.1f}".format(b[i])) if b[i] % 1 != 0 else int(b[i])] + [float("{:.1f}".format(ratios[i])) if ratios[i] != float('inf') else '-'] + [''])
 
            c2_neg = [-1 * round(float("{:.1f}".format(col)), 1) for col in c2]
            table.append(['F(x)'] + c2_neg + F_values)
            with open('primary_table.txt', 'a', encoding='utf-8') as file:
                file.write(f"\nФинальная:\n")
                for row in table:
                    file.write(''.join(['{:<10}'.format(str(elem)) for elem in row]) + '\n')
            if b[i] < 0:
             print(f"Задача не имеет решения")
             with open('primary_table.txt', 'a', encoding='utf-8') as file:
                file.write(f"\nЗадача не имеет решения\n")
                sys.exit()
       if tr == 'No':
          pass
   
    return result

# Запрос данных у пользователя
with open('data.txt') as f:
    next(f)  # пропустить 1 строку
    tr = f.readline().strip()
    next(f)  # пропустить 3 строку
    Napr2 = f.readline().strip()
    next(f)  # пропустить 5 строку
    num_vars = int(f.readline()) #кол-во переменных
    next(f)  # пропустить 7 строку
    num_constraints = int(f.readline()) #кол-во ограничений
    next(f)  # пропустить 8 строку
    c2 = f.readline().split() #целевая функция
    next(f)  # пропустить 10 строку
    h = f.readline().split() #значения для ограничений
    next(f)  # пропустить 12 строку
    b2 = f.readline().split() #значения для ограничений после знака
    next(f)  # пропустить 14 строку
    Zn2 = f.readline().split() #Знаки
    
    napr = Napr2
    c = [float(x) for x in c2] # целевая функция в виде одномерного массива
    b = [float(x) for x in b2]# значения для ограничений после знака в виде одномерного массива
    Zn = [str(x) for x in Zn2]
    A = [[0]*num_vars for _ in range(num_constraints)]
    for i in range(num_constraints):
        for j in range(num_vars):
            try:
                value = float(h[i*num_vars+j])
                A[i][j] = value
            except ValueError:
                print("Ошибка")
                break

if napr == 'max':
   
   # Преобразование уравнений с знаком равенства на два уравнения с знаком меньше
   new_A = []
   new_b = []
   new_Zn = []
   for i in range(num_constraints):
    if Zn[i] == "=":
        eq_parts = Zn[i].split('=')
        new_A.append(A[i])
        new_b.append(b[i])
        new_Zn.append('<=')
        new_A.append([-x for x in A[i]])
        new_b.append(-b[i])
        new_Zn.append('<=')
        if '>=' in eq_parts:
            new_A[-1] = [-x for x in new_A[-1]]
            new_b[-1] = -new_b[-1]
    elif Zn[i] == '>=':
        new_A.append([-x for x in A[i]])
        new_b.append(-b[i])
        new_Zn.append('<=')
    else:
        new_A.append(A[i])
        new_b.append(b[i])
        new_Zn.append(Zn[i])
   
   A = new_A
   b = new_b
   Zn = new_Zn

   # Вывод содержимого массивов
   # целевая
   expression = ""
   for i in range(len(c)):
       expression += f"{c[i]}*x{i+1}+"
   expression = expression.rstrip("+") # Удаляем последний плюс
   print(f"{napr} {expression}")
   #ограничения
   for j, row in enumerate(A):
    left_side = ' + '.join([f'{coeff:.0f}*x{i+1}' for i, coeff in enumerate(row)])
    print(f'{left_side} {Zn[j]} {b[j]:.0f}')
    
   #Запись уравнения в текстовик 
    with open('primary_table.txt', 'w') as f:
     expression = ""
     for i in range(len(c)):
         expression += f"{c[i]}*x{i+1}+"
     expression = expression.rstrip("+") # Удаляем последний плюс
     f.write(f"{napr} {expression}\n")
     for j, row in enumerate(A):
         left_side = ' + '.join([f'{coeff:.0f}*x{i+1}' for i, coeff in enumerate(row)])
         f.write(f'{left_side} {Zn[j]} {b[j]:.0f}\n')
   
   # Решение задачи
   result = simplex_method(c, A, b, num_vars)

   #Запись данных в текстовик
   with open('primary_table.txt', 'a', encoding='utf-8') as f:
        f.write("\nРешение:\n")
        for i in range(len(result)):
            f.write(f"x{i+1} = {result[i]}\n")
        f.write(f"Целевая функция: {sum(c[i]*result[i] for i in range(len(result)))}\n")     

   # Вывод результатов в консоль
   print("Решение:")
   for i in range(len(result)):
    print(f"x{i+1} = {result[i]}")
   print(f"Значение целевой функции: {sum(c[i]*result[i] for i in range(len(result)))}")
   
elif napr == 'min':
   #вывод целевой
   expression = ""
   for i in range(len(c)):
       expression += f"{c[i]}*x{i+1}+"
   expression = expression.rstrip("+")
   print(f"{napr} {expression}")

   c = [-1.0 * x for x in c]
   c.append(-1.0)

   A = [row + [0.0] for row in A]
   
   # Преобразование уравнений(= - 2x<(+,-/ > - <)
   new_A = []
   new_b = []
   new_Zn = []
   for i in range(num_constraints):
    if '=' in Zn[i]:
        eq_parts = Zn[i].split('=')
        new_A.append(A[i])
        new_b.append(b[i])
        new_Zn.append('<')
        new_A.append([-x for x in A[i]])
        new_b.append(-b[i])
        new_Zn.append('<')
        if '>' in eq_parts:
            new_A[-1] = [-x for x in new_A[-1]]
            new_b[-1] = -new_b[-1]
    elif Zn[i] == '>':
        new_A.append([-x for x in A[i]])
        new_b.append(-b[i])
        new_Zn.append('<')
    else:
        new_A.append(A[i])
        new_b.append(b[i])
        new_Zn.append(Zn[i])
   
   A = new_A
   b = new_b
   Zn = new_Zn

   # Вывод ограничений
   for j, row in enumerate(A):
    left_side = ' + '.join([f'{coeff:.0f}*x{i+1}' for i, coeff in enumerate(row)])
    print(f'{left_side} {Zn[j]} {b[j]:.0f}')

    with open('primary_table.txt', 'w', encoding='utf-8') as f:
     expression = ""
     for i in range(len(c)):
         expression += f"{c[i]}*x{i+1}+"
     expression = expression.rstrip("+") # Удаляем последний плюс
     f.write(f"{'Задача будет решение через max, путем домножения целевой функции на -1 и добавление дополнительно переменной'}\n")
     f.write(f"{'max'} {expression}\n")
     for j, row in enumerate(A):
         left_side = ' + '.join([f'{coeff:.0f}*x{i+1}' for i, coeff in enumerate(row)])
         f.write(f'{left_side} {Zn[j]} {b[j]:.0f}\n')

    # Решение задачи
   result = simplex_method(c, A, b, num_vars)

   #Запись данных в текстовик
   with open('primary_table.txt', 'a', encoding='utf-8') as f:
     f.write("\nРешение:\n")
     for i in range(len(result)):
         f.write(f"x{i+1} = {result[i]}\n")
     f.write(f"Целевая функция: {-sum(c[i]*result[i] for i in range(len(result)))}\n")

   # Вывод результатов
   print("Решение:")
   for i in range(len(result)):
    print(f"x{i+1} = {result[i]}")
   print(f"Значение целевой функции: {-sum(c[i]*result[i] for i in range(len(result)))}")
else:
    with open('primary_table.txt', 'w', encoding='utf-8') as f:
     f.write("Неверный ввод. Введите 'max' или 'min'.")
    print("Неверный ввод. Введите 'max' или 'min'.")
