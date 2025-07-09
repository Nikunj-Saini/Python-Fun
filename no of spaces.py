
input_string = input("enter a sentence:")
space_count = 0
for char in input_string:
    if char == ' ':
        space_count += 1
# Print the result
print(f"There are  {space_count}  spaces in the sentence")