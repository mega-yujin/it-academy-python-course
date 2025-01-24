"""
Пусть P(m,n) будет количеством различных элементов в таблице умножения m×n.
Например, таблица умножения 3×4, В ней 8 различных элементов {1,2,3,4,6,8,9,12}, поэтому P(3,4) = 8.
Известно, что:
P(64,64) = 1263,
P(12,345) = 1998
P(32,1015) = 13826382602124302

Найдите P(64,1016)
"""
def count_unique_elements(m, n):
    unique_elements = set()

    for i in range(1, m+1):
        for j in range(1, n+1):
            unique_elements.add(i*j)

    return len(unique_elements)

known_values = {
    (64, 64): 1263,
    (12, 345): 1998,
    (32, 1015): 13826382602124302
}

result = count_unique_elements(64, 1016)

print(f"P(64, 1016) = {result}")