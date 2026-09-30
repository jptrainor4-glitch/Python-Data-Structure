def insertion_sort(my_list):
  for i in range(1, len(my_list)):            #Outer Loop, Iterate through the list starting at index [1]
    for j in range(i, 0, -1):                 #Inner Loop, Iterate backward until the iteration of the outer loop
      if my_list[j] < my_list[j - 1]:         #If [inner loop iteration] index value is large than preceeding index
        temp = my_list[j]                     #Swap two indicies
        my_list[j] = my_list[j - 1]
        my_list[j - 1] = temp
      else:
        break                                #If inner loop has served its purpose, break early
  return my_list                             #Return List

print(insertion_sort([4,2,6,5,1,3]))
