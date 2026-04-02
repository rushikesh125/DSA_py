def merge_sorted_arr(arr1,arr2):
    i,j=0,0
    result = []
    
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    
    while i<len(arr1):
        result.append(arr1[i])
        i+=1
    
    while j<len(arr2):
        result.append(arr2[j])
        j+=1
    
    return result


print(merge_sorted_arr([1,4,7,8],[2,3,5,9,10]))