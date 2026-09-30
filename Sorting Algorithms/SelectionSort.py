def selection_sort(my_list):                            #Define function

    for i in range(len(my_list) - 1):                   #Outter loop, no use iterating final index of list
        min_index = i                                   #Minimum index defined

        for j in range(i, len(my_list)):                #Inner loop, starting at i index through to end of list
            if my_list[min_index] > my_list[j]:         #If statement checking min value
                min_index = j                           #If true, redefine

        temp = my_list[min_index]                       #Temp pointer at index value
        my_list[min_index] = my_list[i]                 #Alter list inplace at min values index
        my_list[i] = temp                               #Alter List inplace at begining index of the inner loop

    return my_list                                      #Return altered list


print(selection_sort([4,2,6,5,1,3]))
