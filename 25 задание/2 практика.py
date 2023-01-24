# task_!
# for i in range(123450708, 123459798 + 1):
#     if str(i)[:5] == "12345" and str(i)[6] == "7" \
#             and str(i)[-1] == "8" and i % 23 == 0:
#         print(i, i // 23)

# task_2
# Назовём маской числа последовательность цифр, в которой также могут встречаться
# следующие символы:
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины; в том
# числе «*» может задавать и пустую последовательность.
# Например, маске 123*4?5 соответствуют числа 123405 и 12300425. Среди натуральных
# чисел, не превышающих 10**9, найдите все числа, соответствующие маске 123*567? и
# делящиеся на 169 без остатка. В ответе запишите в первом столбце таблицы все
# найденные числа в порядке возрастания, а во втором столбце — соответствующие им
# частные от деления на 169
# 1 000 000 000 vs 1 239 995 679
# def f():
#     for i in range(12325677, 10**9 + 1, 169):
#         if str(i)[:3] == '123' and str(i)[-4:-1] == '567' and i % 169 == 0:
#             print(i)
#
#
# f()
# answer = 12325677
# 12385672
# 123165679
# 123225674
# 123515678
# 123575673
# 123865677
# 123925672

# task_3
#  1?34567?9
# for i in range(113456759, 10**9 + 1, 17):
#     if str(i)[0] == '1' and str(i)[2:7] == '34567' and str(i)[-1] == '9' and i % 17 == 0:
#         print(i, i // 17)

# task_4
def f(n):
    result = []
    for i in range(2, int(n ** 0.5)):
        result.append(i)
        result.append(n // i)

    return sum(result)

for i in range(1021394, 10**10 + 1):
    r = str(f(i))
    if r[:len(r) // 2] == r[len(r): len(r) // 2: -1]:
        print(r)