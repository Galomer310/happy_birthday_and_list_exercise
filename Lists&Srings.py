# Challenge 1
multiplication_list = []
number = int(input("choose a number"))
multiplication_list.append(number)
multiplier = input("choose a multiplier")
multiplier = int(multiplier)
list_size = int(len(multiplication_list))
for num in multiplication_list:
    if list_size == multiplier:
        print("end of the list")
    elif list_size < multiplier:
        action = multiplication_list[-1] * 2
        multiplication_list.append(action)
        list_size += 1
        print(multiplication_list)
    else:
        break

# Challenge 2
seen = set()
result = []
input_string = input("enter a String \n")
print(f"input string: {input_string}")
for char in input_string:
    if char not in seen:
        seen.add(char)
        result.append(char)
output_string = ''.join(result)
print(f"output string: {output_string}")



