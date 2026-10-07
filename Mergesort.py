comparisons = 0

def merge(arr, left, mid, right):
    global comparisons

    i = left
    j = mid + 1
    temp = []

    while i <= mid and j <= right:
        comparisons += 1

        # For descending order
        if arr[i] >= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for i in range(len(temp)):
        arr[left + i] = temp[i]


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


n = int(input("Enter number of products: "))

arr = []

print("Enter product prices:")

for i in range(n):
    arr.append(int(input()))

merge_sort(arr, 0, n - 1)

print("\nSorted product prices in descending order:")
print(*arr)

print("\nNumber of comparisons:", comparisons)
print("Time Complexity: O(n log n)")