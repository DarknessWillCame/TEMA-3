counter = 0
while counter != 10:
    counter += 1
    string = 'hello'
    memory = ' world'
    print(string + memory)
    memory = string
    print(string)
    string = memory
    

