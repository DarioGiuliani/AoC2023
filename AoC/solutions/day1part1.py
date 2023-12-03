from utils.file_reader import FileReader
import string

input = FileReader.readfile("day1part1input.txt")
table = str.maketrans(string.ascii_letters, '*'*len(string.ascii_letters))
total = 0

for element in input:
    onlyNumbers = element.translate(table).replace('*', '').strip()
    total += int(onlyNumbers[0]+onlyNumbers[-1])

print(total)