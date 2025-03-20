# with open('5-exam.txt', 'w') as file:
#     file.write('Write your exam questions here. !!!!!!!!!!!!!!!11')



with open('5-exam.txt', 'r') as file:
    content = file.read()
    print(content)