class Mylist:
    def __init__(self, numbers):
        self.numbers = numbers  
    def add_numbers(self, numbers):
        self.numbers.append(numbers)
    def find_indexes(self, target):
        indexes = []
        for i in range(len(self.numbers)):
            for j in range(i+1, len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == target:
                    indexes.append((i,j))
        return indexes if indexes else -1
my_list = Mylist([1, 2, 3, 4, 5])
target = 9
result = my_list.find_indexes(target)
print(result)