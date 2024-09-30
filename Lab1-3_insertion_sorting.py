#insertion sorting

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i] #일시적으로 key값 할당
        j = i - 1
        
        while j >= 0 and key < lst[j]: 
            lst[j+1] = lst[j] #오른쪽으로 이동
            j -= 1  #j가 -1이면 멈춤
            
        lst[j+1] = key #j=0이 되면 최솟값으로 내려온다
        
lst = [12, 11, 13 ,5, 6]
print("original list = %s" %lst)
insertion_sort(lst)
print("sorted list by insertion method = %s" %lst)