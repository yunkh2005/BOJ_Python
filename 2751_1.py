N = int(input())
A = []

for i in range(N):
    A.append(int(input()))

def QuickSort(A, start, end):
    if start >= end: 
        return

    pivot = start 
    left = start + 1
    right = end

    while(left <= right):
        while(left <= end and A[left] <= A[pivot]):
            left += 1

        while(right > start and A[right] >= A[pivot]):
            right -= 1

        if(left > right): 
            A[right], A[pivot] = A[pivot], A[right]
        else: 
            A[left], A[right] = A[right], A[left]

    QuickSort(A, start, right - 1)
    QuickSort(A, right + 1, end)

QuickSort(A, 0, N-1)
for i in A:
    print(i)