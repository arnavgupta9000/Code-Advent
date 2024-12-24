def open_file(file):
    a = []
    with open(file, 'r') as f:

        for i in f:
            a.append(i.strip().split())
    
    return a

def part1():

    arr = open_file("2024/day 2/input.txt")
    
    valid = 0

    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):

    for i, row in enumerate(arr):
        asc = True
        desc = True
        prev = []
        for j, v in enumerate(row):
            v = int(v)
            if prev:

                if v >= prev[-1]:
                    desc = False
                if v <= prev[-1]:
                    asc = False
                if not(abs(int(v) - int(prev[-1])) >= 1 and abs(int(v) - int(prev[-1])) <= 3):
                    asc = False
                    desc = False

            prev.append(int(v))
        

        if asc or desc:
            valid +=1
        
    # issue was i wasnt using int and it was comparing strings...


#part1()


def part2():
    arr = open_file("2024/day 2/input.txt")
    # plan call a helper function for every row without 1 element for every element. if one returns true it works if all returns false it doesnt work
    def helper(arr):
        #print(arr)
        asc = True
        desc = True
        prev = []

        for j, v in enumerate(arr):
            v = int(v)
            if prev:

                if v >= prev[-1]:
                    desc = False
                if v <= prev[-1]:
                    asc = False
                if not(abs(int(v) - int(prev[-1])) >= 1 and abs(int(v) - int(prev[-1])) <= 3):
                    asc = False
                    desc = False

            prev.append(int(v))
            

        if asc or desc:
            return True
        return False

    total = 0
    for i in range(len(arr)):
        valid = False
        for j in range(len(arr[i])):

                if not valid:
                    re = arr[i][0:j] + arr[i][j+1:]
                    valid = helper(re)
        
        if valid:
            total +=1
    
    print(total)


part2()