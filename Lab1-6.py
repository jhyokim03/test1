#insertion sorting 내림차순 정리

def insertion_sort(lst):
    
    for i in range(1, len(lst)):
        key = lst[i]
        j = i -1
        
        while j >= 0 and key > lst[j]:
            lst[j+1] = lst[j]
            j-= 1
            
        lst[j +1] = key 

lst = [12, 11, 13 ,5, 6]
print("original list = %s" %lst)
insertion_sort(lst)
print("sorted list by insertion method = %s" %lst)