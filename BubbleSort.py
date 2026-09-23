def bubble_sort(my_list):                           #Define function
    for i in range(len(my_list) - 1, 0, -1):        #Start outter loop iteratting backward, this ensures inner loop index stays in range
        print('i:', i)                              #Developer feedback, shows each itteration incase of error.
        for j in range(i):                          #Inner loop, itterating forward through the length of the current outter loop iteration
            if my_list[j] > my_list[j + 1]:         #If statement, searching for bigger vlue between two corrisponding numbers in list
                temp = my_list[j + 1]               #If above True, holds value of next index before it is changed
                my_list[j + 1] = my_list[j]         #Replace value of next index with value of current index.
                my_list[j] = temp                   #Replace value of current index with held value temp.
    return my_list                                  #Function output of list thats been altered inplace.


print(bubble_sort([4,2,6,5,1,3]))