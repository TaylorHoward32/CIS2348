#TaylorHoward
#10-05-2020
#CIS2348-14654
#Zylab 6.22

def main():
    #inputs for Variables x,y,n
    x1 =int(input())
    y1 = int(input())
    n1 = int(input())

    x2 = int(input())
    y2 = int(input())
    n2 = int(input())

    #If it wasn't solution is not found

    solution_found=False

    #Integer coefficent range

    for x in range (-10,11):
        for y in range(-10,11):
            if x1 * x + y1 * y== n1 and x2 * x +y2 * y==n2:
                print(x,y)
                solution_found=True

    if not solution_found:
        print("No solution")

if __name__ == '__main__':
    main()

