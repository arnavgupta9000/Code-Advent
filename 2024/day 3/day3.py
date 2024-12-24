def read_file(file):
    arr = []
    with open(file, 'r') as f:
        for i in f:
            arr.append(i.strip())

    return arr

def part1():
    string = "".join(map(str, read_file("2024/day 3/input.txt")))
    valid = 'mul('
    j=0
    total = 0
    a= 0
    while True:
        
        index = string.find(valid,j) # index value is where its found
        if index == -1:
            break
        j = index
        # start reading from index j
        # now find the comma
        comma = string.find(',', j)
        num1 = string[index+4:comma]
        try:
            num1 = int(num1)
            j=comma
            # find the end bracket
            bracket = string.find(')', j)
            k=j # save j
            j=bracket

            num2 = string[comma+1:bracket]
            
            try:
                num2 = int(num2)
                if string[j] == ')':
                    print(f"mul({num1},{num2})")
                    a+=1
                    total += num1 * num2
                else:
                    print(string[j], j)
            except:
                j=k # restore j # this was the problem, it would skip to much ie mul(7,8]mul(3,4)<- before it would go straight to that bracket skipping one of the muls

                j+=1
                # pass
        except:
            j+=1



    print(total)
    print(a, sep = '\n')
    
        

part1()

def part2():
    string = "".join(map(str, read_file("2024/day 3/input.txt")))
    valid = 'mul('
    j=0
    k=0
    total = 0
    do = True
    infinite = None
    while True:
        
        index = string.find(valid,j) # index value is where its found
        if infinite == True:
            pass
        if infinite == False:
            # done exit
            return
        else:
            while True:
                # if index is between the last do and the next dont we are good, if its between a dont and a do we are not good
                # assume we have currently do-don't and its not infinite
                # find the next don't()
                if do:
                    find_do = string.find("don't()", k)
                    if find_do == -1:
                        infinite = True
                    if do <= index <= find_do:
                        break # we are good to go
                    else:
                        # we set do = False
                        do = False
                        k = find_do
                else:
                    pass
                


        
        if index == -1:
            break
        j = index
        # start reading from index j
        # now find the comma
        comma = string.find(',', j)
        num1 = string[index+4:comma]
        try:
            num1 = int(num1)
            j=comma
            # find the end bracket
            bracket = string.find(')', j)
            k=j # save j
            j=bracket

            num2 = string[comma+1:bracket]
            
            try:
                num2 = int(num2)
                if string[j] == ')':
                    print(f"mul({num1},{num2})")
                    a+=1
                    if do:
                        total += num1 * num2
                else:
                    print(string[j], j)
            except:
                j=k # restore j # this was the problem, it would skip to much ie mul(7,8]mul(3,4)<- before it would go straight to that bracket skipping one of the muls

                j+=1
                # pass
        except:
            j+=1

part2()