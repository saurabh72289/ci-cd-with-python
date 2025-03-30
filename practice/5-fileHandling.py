with open('5-exam.txt', 'w') as file:
    file.write('Write your exam questions here. !!!!!!!!!!!!!!!11')



with open('5-exam.txt', 'a') as file:
    file.write('\n\n new line added !!!!!!11')



with open('5-exam.txt', 'r') as file:
    content = file.read()
    print(content)