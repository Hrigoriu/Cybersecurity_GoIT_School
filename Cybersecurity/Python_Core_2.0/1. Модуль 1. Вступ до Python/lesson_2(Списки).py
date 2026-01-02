my_list = list()
empty_list = []
#==============================================================
my_list = [1, "Hello", 3.14]
#==============================================================
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[0]
middle_one = some_iterable[1]
last_letter = some_iterable[2]

#==============================================================
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[-3]
middle_one = some_iterable[-2]
last_letter = some_iterable[-1]

#==============================================================
some_iterable[1] = -2

#==============================================================
chars = ['a', 'b', 'c']
last = chars.pop(1)

#==============================================================
chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)

#==============================================================
chars = ["a", "c"]
chars.insert(1, "b")

#==============================================================
chars = ['a', 'b']
chars.clear()  # []

#==============================================================
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c')

#==============================================================
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

#==============================================================
my_list = [1, 2, 3, 4, 5]
print(len(my_list))

#==============================================================
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

#==============================================================
nums.sort(reverse=True)
print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]

#==============================================================
words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']

#==============================================================
nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]
print(nums)  # Оригінальний список залишається незмінним

#==============================================================
sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)  # Виведе [9, 5, 4, 3, 2, 1, 1]

#==============================================================
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']

#==============================================================
chars = ['a', 'b']
chars_copy = chars.copy()
print(chars_copy)  # Виведе ['a', 'b']
#==============================================================
chars = ["banana", "apple", "cherry"]
chars.reverse()
print(chars)  # Виведе ['cherry', 'apple', 'banana']
