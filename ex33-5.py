def counting(count_var, num_incr=1):
    i=0
    numbers=[]

    for i in range(0, count_var, num_incr):
        print(f"At the top i is {i}")
        numbers.append(i)

        # The incrementor is no longer needed there, because it increments with for on it's own.
        # i=i+num_incr
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

counting(100, 8)