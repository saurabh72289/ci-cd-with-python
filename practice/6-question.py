# Write a function that reads a file and prints its contents. If the file doesn’t exist, print an error message instead of crashing.

# # 


try:
    with open('5-exam----.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Error: File not found   \n\n\n', FileNotFoundError)



# In the above code, the open() function is used to open a file in read mode ('r'). 
# If the file doesn't exist, a FileNotFoundError is raised. We use a try-except block to catch this error and print an error message instead of crashing the program.