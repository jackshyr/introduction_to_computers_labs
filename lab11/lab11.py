import json

def select(a):
    if a>0:
        a -=1
        select(a)
    if a == 0:
        return b

def BF(input):
    N = len(input)
    # complete the code
    # print(N)

    return assignment, cost

# main
with open('input.json', 'r') as inputFile:
    a = 0
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input

        # show input data and number of the Tasks
        print("Question: "+str(a))
        print("Assignment: "+str(input))
        a += 1

        # Brute Force Algorithm
      #  assignment, cost = BF(input)

       # print('Question: ' + str(key))
       # print('Assignment:', assignment)
       # print('Cost:', cost)
       # print()
