# (x ∧ ¬y) ∨ (y ≡ z ) ∨ w.

# task_1
# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 f = (x and (not(y))) or (y == z) or w
#                 if f == 0:
#                     print(x, y, z, w)

# task_2
# (¬x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w.
#
# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 f = ((not(x)) and (not(y)) or (y == z) or (not(w)))
#                 if f == 0:
#                     print(x, y, z, w)

# task_3
# #((x → y) ≡ (y → z)) ∧ (y ∨ w).
#
# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 f = (((x <= y) == (y <= z)) and (y or w))
#                 if f == 1:
#                     print(x, y, z, w)

# task_4
# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 f = ((not(x) == z) <= (y == (w or x)))
#                 if f == 0:
#                     print(x, y, z, w)

# task_5
# #((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y)
# lst = [0, 1]
# print('x y z w')
# for x in lst:
#     for y in lst:
#         for z in lst:
#             for w in lst:
#                 f = ((x and w) or (w and x)) == ((z <= y) and (y <= x))
#                 if f == 1:
#                     print(x, y, z, w)
#
