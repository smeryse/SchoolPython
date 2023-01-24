# получение стартовых данных
file = list(open('26-60.txt'))
K, N = map(lambda x: int(x), file[0][:-1].split())

# словарь id: count по специальностям
spec_codes = {id: int(count[:-1]) for id, count in enumerate(file[1: K + 1])}

# словарь студентов с ключом id (направления) и значениями - список баллов абитурентов
students = dict()
for data in file[K + 1:]:
    scores, id = map(lambda x: int(x), data.split())
    students.setdefault(id, []).append(scores)

# словарь со списком поступивших. Ключ - id
enrolled = dict()
for id, scores in students.items():
    scores = sorted(scores, reverse=True)
    # получаем из словаря номер направления и баллы на эту направленность
    # так как количество абитуриентов может быть меньше кол-ва мест, выбираем наименьшее из них
    # получаем из списка scores студентов получаем сначала с самыми высокими баллами, а затем по убыванию
    enrolled[id] = [scores[score] for score in range(min(spec_codes[id], len(scores)))]

# задача реализована, но почему она не верна?