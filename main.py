import random


def main():
    total = 0
    numbers = []
    for i in range(5):
       numbers.append(random.randint(0,100))
    print(numbers[i], end = ' ')
    total += numbers[i] 
    print (total)

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
