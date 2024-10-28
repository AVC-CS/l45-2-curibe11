

def main():  
    import random 
    numbers = []
    total = 0 
    for i in range(5):
        numbers.append(random.randint(0,100))
        print(numbers[i], end = ' ')
        total += numbers[i] 
    total -= numbers[-1]
    print (total)

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
