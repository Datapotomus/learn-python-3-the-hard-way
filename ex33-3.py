def counting(count_var, num_incr=1):
    i=0
    numbers=[]

    while i < count_var:
        print(f"At the top i is {i}")
        numbers.append(i)

        i=i+num_incr
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

counting(100, 8)