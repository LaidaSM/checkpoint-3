#Exercise 1
string_example = 'This sentence is a string'
number_example = 0.75
list_example = ['Item 1', 'Item 2', 'Item 3']
boolean_example = False

#Exercise 2
query_string = string_example[0:3]

#Exercise 3
query_list_first = list_example[0]

#Exercise 4
incremented_number = number_example + 10

#If we wanted the original variable incremented, and not a new variable, we could perform:
# number_example +=10

#Exercise 5
query_list_last = list_example[-1]

#Exercise 6
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)

#Exercise 7
string_word = string_example[:4]
string_word_upp = string_word.upper()
new_string = f'{string_word_upp}{string_example[4:]}'

#Exercise 8
new_sentence = f'The probability of precipitation today is {number_example}'

#We could also use format method:
# new_sentence_two = 'The probability of precipitation today is ' + str(number_example)

#Or we could do it without string interpolation, converting the number into a string
# new_sentence_three = 'The probability of precipitation today is {0}'.format(number_example)

#Exercise 9
print('hello world')

#But if the "" should also be included:
# print('\"hello world\"')