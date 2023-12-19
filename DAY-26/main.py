from unittest import result


numbers = [1, 2, 3, 4, 5]
# list compression
print([n + 1 for n in numbers])
name = "JIBRIL"
letter = [n for n in name]
print(letter)
range_list = [n * 3 for n in range(1, 5)]
print(range_list)
names = ["jibril", "jemal", "abba jobir", "abbabora"]
short_names = [name.upper() for name in names if len(name) < 7]
long_names = [name for name in names if len(name) > 7]

print(short_names)
print(long_names)
sq = [2, 4, 1, 3, 5, 7, 9, 6, 8, 10, 12, 22, 44]
print([n**2 for n in sq])
print([n for n in sq if n % 2 == 0])
with open("/home/jibril/Documents/Python/DAY-26/file1.txt") as file1:
    file1_data = file1.readlines()
with open("/home/jibril/Documents/Python/DAY-26/file2.txt") as file2:
    file2_data = file2.readlines()
result = [int(num) for num in file1_data if num in file2_data]
print(result)
