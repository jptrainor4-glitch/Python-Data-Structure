def insertion_sort(my_list):
  for i in range(1, len(my_list)):
    for j in range(i, 0, -1):
      if my_list[j] < my_list[j - 1]:
        temp = my_list[j]
        my_list[j] = my_list[j - 1]
        my_list[j - 1] = temp
      else:
        break
  return my_list

print(insertion_sort([4,2,6,5,1,3]))