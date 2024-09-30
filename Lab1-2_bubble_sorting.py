def bubblesort(lst):
    n = len(lst)
    
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
    return lst
                
lst = [64, 34, 25, 12, 22 , 11, 90]
print("orignal list %s" %lst)
print("sorted list : %s" %bubblesort(lst))
                