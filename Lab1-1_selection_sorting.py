#selection sorting(최솟값 중심 정리)

def selection_sort(list):
    
    for i in range(len(list)):
        min_idx = i
        
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                min_idx = j
                list[i] , list[min_idx] = list[min_idx] , list[i]
        
    return list
        
list = [64, 25, 12, 22, 11]
print("original list : %s" %list)

print("sorted list : %s" %selection_sort(list))
