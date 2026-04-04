input_str = input("Nhập X, Y: ")
# Tách chuỗi nhập vào thành danh sách các số nguyên
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
# Tạo mảng 2 chiều chứa toàn số 0
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# Gán giá trị cho từng phần tử bằng tích của chỉ số hàng và cột
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print (multilist)