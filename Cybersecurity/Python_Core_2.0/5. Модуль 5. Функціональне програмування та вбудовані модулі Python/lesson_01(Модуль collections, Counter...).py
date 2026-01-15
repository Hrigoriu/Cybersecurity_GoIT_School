from collections import namedtuple

# Створення іменованого кортежу
Point = namedtuple('Point', ['x', 'y'])
# Створення екземпляра Point
p = Point(11, y=22)

# Доступ до елементів
print(p.x)  # 11
print(p.y)  # 22
#================================================================================================
import collections

# Створення іменованого кортежу Person
Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# Виведення різних атрибутів іменованого кортежу
print(person.first_name)       
print(person.post_index) 
print(person.age)        
print(person[3])         
#================================================================================================

import collections

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])
cat = Cat('Simon', 4, 'Krabat')
print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')
#================================================================================================
#================================================================================================
                #Counter
#================================================================================================
#================================================================================================
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)

#================================================================================================
import collections

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts)

#================================================================================================
import collections

student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)

print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

#================================================================================================
from collections import Counter

# Створення Counter з рядка
letter_count = Counter("banana")
print(letter_count)

#================================================================================================
from collections import Counter

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
word_count = Counter(words)
print(word_count)
# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")

#================================================================================================
from collections import defaultdict

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)

# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

#================================================================================================
from collections import defaultdict

d = defaultdict(int)

# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1

print(d)
#================================================================================================
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words)


#================================================================================================
from collections import defaultdict

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))