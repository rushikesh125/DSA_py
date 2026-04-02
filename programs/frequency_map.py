nums = [5,6,7,7,9,3,4,6,2,5,7,3,5,3,4,5,2,3,,6]

freq_map = {}
for i in nums:
    freq_map[i] = freq_map.get(i,0)+1

print(freq_map)