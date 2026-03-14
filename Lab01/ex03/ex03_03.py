# Tạo Tuple
def tao_tuple_tu_list(lst):
    return tuple(lst)

# Truy cập phần tử đầu và cuối
def truy_cap_phan_tu(tuple_data):
    return tuple_data[0], tuple_data[-1]

input_list = input("Nhập danh sách các số: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
first, last = truy_cap_phan_tu(my_tuple)
print("Tuple từ List:", my_tuple)
print(f"Phần tử đầu tiên: {first}, Cuối cùng: {last}")