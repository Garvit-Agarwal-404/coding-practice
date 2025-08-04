def average(lst):    
    sum_of_list=sum(lst)
    average=sum_of_list/len(lst)
    return average
lst=[1,2,3,4,37]
Average=average(lst)
print("Average of the list is ",round(Average,3))