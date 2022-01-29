def get_Titles():
    temp = []
    with open('bin\\books\\book-info.txt') as f:
                        for line in f:
                            line = line.strip().split('-')
                            temp.append(line[1])
    return temp
li = get_Titles()
print(li)