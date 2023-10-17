number_array = [
    [54, 76, 12],
    [98, 14, 51],
    [21, 82, 46]]

# Рахуємо колонки у матриці
columns_count = len(number_array[0])
# Створюємо новий пустий Array
column_arrays = [[] for _ in range(columns_count)]

# Беремо кожен рядок з матриці чисел
for row in number_array:
    # Беремо кожну колонку і заповнюємо масив column_arrays
    for i in range(columns_count):
        column_arrays[i].append(row[i])

#  Підраховуємо сумму кожної колонки
for column in column_arrays:
    column_sum = sum(column)
    print(column, "sum = ", column_sum)

column_sums = [sum(column) for column in column_arrays]

# Сортуємо індекси колонок за їх сумами
indexes_sorted_columns = sorted(range(columns_count), key=lambda i: column_sums[i])

# Створюємо новий відсортований масив
sorted_colons_array = [
    [number_array[row_i][col_i] for col_i in indexes_sorted_columns]
    for row_i in range(len(number_array))
]

print("\nНовий масив:")
for row in sorted_colons_array:
    print(row)
