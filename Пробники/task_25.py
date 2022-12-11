#task_25
#input: [174457, 174505]

result = []
for num in range(174457, 174506):
    devider = []
    for dev in range(2, num):
        if num % dev == 0:
            devider.append(dev)
    if len(devider) == 2:
        result.append(devider)

#nums output
for i in result:
    print(*i)