"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():
    while True:
        input = raw_input()
        tokens = input.split(" ")
        #loop through list to identify digits using the range function
    
        for index in range(len(tokens)): #range helps us get at the indices of a list.
            if tokens[index].isdigit() == True: #checks if the string at specific index is a digit
                tokens[index] = int(tokens[index]) #turns item at index into an integer

        if tokens[0] == "q":
            break
        elif tokens[0] == "+":
            Output = arithmetic.add(tokens[1], tokens[2])
            print Output
        elif tokens[0] == "-":
            Output = arithmetic.subtract(tokens[1], tokens[2])
            print Output
        elif tokens[0] == "*":
            Output = arithmetic.multiply(tokens[1], tokens[2])
            print Output
        elif tokens[0] == "/":
            Output = arithmetic.divide(tokens[1], tokens[2])
            print Output
        elif tokens[0] == "square":
            Output = arithmetic.square(tokens[1])
            print Output
        elif tokens[0] == "cube":
            Output = arithmetic.cube(tokens[1])
            print Output
        elif tokens[0] == "mod":
            Output = arithmetic.mod(tokens[1], tokens[2])
            print Output
        else:
            print "Please use prefix style format."
            continue



    
if __name__ == '__main__':
    main()
