class StrArr:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        return self.array[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        self.array[index] = value

    def print_elem(self, index):
        print(self[index])

    def print_array(self):
        for i in range(self.size):
            print(self[i])

if __name__ == "__main__":
    
    # создание массива
    arr1 = StrArr(3)
    arr1[0] = "focus"
    arr1[1] = "school"
    arr1[2] = "house"

    # обращение к элементу массива
    print(arr1[1])

    print("\n\n") # для увеличения читабельности кода

    # выполнение операции поэлементного сцепления
    arr2 = StrArr(3)
    arr2[0] = "say"
    arr2[1] = "everyday"
    arr2[2] = "street"
    arr3 = StrArr(3)
    for i in range(3):
        arr3[i] = arr1[i] + arr2[i]
    arr3.print_array()

    print("\n\n")# для увеличения читабельности кода

    # выполнение операции слияния
    arr4 = StrArr(3)
    arr4[0] = "eggs"
    arr4[1] = "school"
    arr4[2] = "water"
    arr5 = StrArr(6)
    for i in range(3):
        arr5[i] = arr1[i]
    j = 3
    for i in range(3):
        if arr4[i] not in arr1.array:
            arr5[j] = arr4[i]
            j += 1
    print(arr5[2])
    print("\n") # для увеличения читабельности кода
    arr5.print_array()
