#selection sorting(최댓값 중심 정리)

def selection_sort(list):
    
    for i in range(len(list)-1, 0, -1):
        max_idx = i         
        for j in range(i-1, -1, -1): 
            if list[i] < list[j]:
                max_idx = j
                list[i] , list[max_idx] = list[max_idx] , list[i]
    
    return list


list = [64, 25, 12, 22, 11]
print("original list : %s" %list)
print("sorted list : %s" %selection_sort(list))
