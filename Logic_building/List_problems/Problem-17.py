"""
Return unique no of pairs from the sorted list
"""

def Pairs(arr):
    if not arr:
        return []
    else:
        pairs = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                pairs.append((arr[i],arr[j]))

        return pairs


x = list(map(int,input().split()))

print(Pairs(x))
                

