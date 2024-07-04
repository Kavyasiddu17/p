with open('output.txt','r')as f:
    print("File content line by line:")
    for line in f:
        print(line.strip())
