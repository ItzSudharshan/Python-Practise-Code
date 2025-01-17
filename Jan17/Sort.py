#Arranging the Elements in Ascending or Descending 
li = [10,5,3,20] #[3, 5, 10, 20]
li.sort()  #Original List is Getting Modified and getting Sorted in Ascending Order
print(li)

#Sorting in Descending Order
li.sort(reverse=True)    #[20, 10, 5, 3]
print(li)  #original List it is making chnages . List gets sorted and since condition is True it gets reversed and hence list is sorted in descending order

li2 = [100,30,500,10]
sorted_list2 = sorted(li2) #[10, 30, 100, 500]
print(sorted_list2)  #Hence the list is sorted in ascending 


