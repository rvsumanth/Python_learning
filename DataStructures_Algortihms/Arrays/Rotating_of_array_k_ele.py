'''
Rotate Array by K Positions
Problem: Rotate an array of size $N$ to the right by K steps.
Key Intuition (Reversal Algorithm):Normalize K = K % N.
Reverse the entire array.
Reverse the first K elements.
Reverse the remaining N-K elements.
Time / Space: O(N) time, O(1) auxiliary space.
'''

def rotate_array_by_k_ele(arr: list[int], k):
    n = len(arr)
    k = k%n

    def reverse(left, right):
        while left<right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    # Step 1: Reverse the whole array
    reverse(0, n-1)
    # Step 2: Reverse the first k elements
    reverse(0, k-1)
    # Step 3: Reverse the remaining elements 
    reverse(k, n-1)
    return arr


arr = [1,2,3,4,5,6]
k = 2

x = rotate_array_by_k_ele(arr, k)
print(x)