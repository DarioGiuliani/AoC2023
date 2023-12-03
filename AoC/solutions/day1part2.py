from utils.file_reader import FileReader
from word2number import w2n

input = FileReader.readfile("day1part2input.txt")
tokens = ["0","1","2","3","4","5","6","7","8","9","zero","one","two","three","four","five","six","seven","eight","nine"]
total = 0

for element in input:
    occurences = []
    for token in tokens:
        first_index = element.find(token)
        occurences.append((first_index, token))
        last_index = element.rfind(token)
        occurences.append((last_index, token))
        
    filtered_occurences = list(filter(lambda occurence: occurence[0] != -1, occurences))
    first_number = min(filtered_occurences, key = lambda occurence: occurence[0])
    second_number = max(filtered_occurences, key = lambda occurence: occurence[0])

    if(str(first_number[1]).isalpha()):
        first_number = (first_number[0], w2n.word_to_num(first_number[1]))

    if(str(second_number[1]).isalpha()):
        second_number = (second_number[0], w2n.word_to_num(second_number[1]))

    total += int(str(first_number[1])+str(second_number[1]))

print(total)