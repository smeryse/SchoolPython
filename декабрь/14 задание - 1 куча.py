# universal function code
def to_new_system(num, base, type_data='integer'):
    result_func = []

    if type_data == 'integer':
        while num > 0:
            result_func.append(num % base)
            num //= base

    elif type_data == 'string':
        while num > 0:
            result_func.append(str(num % base))
            num //= base

    return result_func[::-1]


# task_6
# num = 1*3**37+2*3**23+3*3**20+4*3**4+5*3**3+4+5
# print(to_new_system(num, 9).count(0))
# answer = 14

# task_7
# num = (64**25+4**10)-(16**20+32**3)
# print(to_new_system(num, base=4)[::-1].index(2) + 1)
# answer = 8

# task_8
# num = (5**300 * 15**100) - (25**50 + 125**100)
# result = to_new_system(num, base=5)
# answer = sum(result) - result.count(4) * 4
# print(answer)
# answer = 83

# task_9
# num = (7**160 * 7**90) - (14**150+2**13)
# result = to_new_system(num, base=7)
# answer = sum(result) - result.count(6) * 6
# print(answer)
# answer = 145

# task_10
# num = 5 * 216**1256 - 5 * 36**1146 + 4 * 6**1053 - 1087
# print(sum(to_new_system(num, 6)))
# answer = 12642

# homework
# task_1
# count = 9 ** 81 + 27 ** 729 - 4
# result = to_new_system(count, 9, type_data='string')  # take out nums in 'count'
# max_num = max(to_new_system(count, 9, type_data='integer'))  # take maximum num in our list
#
# result_str = ''.join(result)
# result_str = result_str.replace('0', str(max_num))  # replace all zeros with the max_num
# print(result_str.count(str(max_num)))
# answer = 8744

# task_2
# count = 12 * 7 ** 135 + 11 * 7 ** 92 - 63 * 7 ** 22 + 17 * 7 ** 11 + 157
# result = to_new_system(count, 7)
# answer = len(set(result))
# answer = 6

# task_3
# count = 5 * 216 ** 1256 - 5 * 36 ** 1146 + 4 * 6 ** 1053 - 1087
# result = to_new_system(count, 6)
# answer = sum(result)
# answer = 12642

# task_4
# count = 0
# min_hex = 16**7
# max_hex = 16**8 - 1
# min_oct = 8**10
# last_int = 5
#
#
# #min_hex < min_oct < max_hex
#
# print(((max_hex - min_oct) / 2) // 5)