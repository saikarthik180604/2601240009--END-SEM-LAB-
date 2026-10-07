# Merge Sort – Product Price Sorting

##  Project Description

This project implements the **Merge Sort algorithm** using the **Divide and Conquer** technique.

An e-commerce company maintains the prices of `N` products in an unsorted array. The program sorts these product prices using Merge Sort and displays:

- Sorted product prices
- Number of comparisons performed
- Time complexity of the algorithm

The program can be easily modified to sort the prices in either **ascending** or **descending** order.

---

##  Objectives

1. Implement Merge Sort using Divide and Conquer.
2. Divide the array recursively into smaller subarrays.
3. Sort and merge the subarrays.
4. Display the sorted product prices.
5. Count the number of comparisons.
6. Analyze the time complexity.

---

## Algorithm Used

### Merge Sort

Merge Sort follows the **Divide and Conquer** approach.

### Steps

1. Divide the array into two halves.
2. Recursively divide each half until individual elements remain.
3. Compare elements from the two sorted halves.
4. Merge them into a single sorted array.
5. Continue until the complete array is sorted.

---

##  Divide and Conquer

For an array:

```text
[5, 2, 8, 1, 9, 3]
```

The array is divided as:

```text
              [5 2 8 1 9 3]
                 /      \
             [5 2 8]   [1 9 3]
              /  \       /  \
           [5] [2 8]  [1] [9 3]
```

After sorting and merging:

```text
[1 2 3 5 8 9]
```

---

##  Program

```python
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
```

---

##  Ascending Order

To sort the product prices in **ascending order**, change:

```python
if arr[i] >= arr[j]:
```

to:

```python
if arr[i] <= arr[j]:
```

Then the output will be from the smallest price to the largest price.

Example:

```text
Input:
50 20 40 10 30

Output:
10 20 30 40 50
```

---

##  Descending Order

The current program sorts the product prices in **descending order** using:

```python
if arr[i] >= arr[j]:
```

Example:

```text
Input:
50 20 40 10 30

Output:
50 40 30 20 10
```

---

##  Sample Input

For 50 products:

```text
Enter number of products: 50
```

Example product prices:

```text
1
2
3
4
5
10
9
8
7
6
11
12
13
14
15
20
19
18
17
16
21
22
23
24
25
30
29
28
27
26
31
32
33
34
35
40
39
38
37
36
41
42
43
44
45
50
49
48
47
46
```

---

##  Sample Output

```text
Sorted product prices in descending order:

50 49 48 47 46 45 44 43 42 41
40 39 38 37 36 35 34 33 32 31
30 29 28 27 26 25 24 23 22 21
20 19 18 17 16 15 14 13 12 11
10 9 8 7 6 5 4 3 2 1

Number of comparisons: ...

Time Complexity: O(n log n)
```

---

##  Time Complexity

| Case | Time Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

### Space Complexity

```text
O(n)
```

Merge Sort requires additional temporary space for merging the subarrays.

---

##  Comparison Counting

The program counts every comparison made while merging two sorted subarrays.

The following statement increments the comparison count:

```python
comparisons += 1
```

Therefore, the program displays the total number of element comparisons after sorting.

---


##  Conclusion

The Merge Sort algorithm successfully sorts product prices using the **Divide and Conquer** technique.

It efficiently handles large numbers of products with a time complexity of:

```text
O(n log n)
```

The program also counts the number of comparisons performed during the sorting process.

## VIVA-VOICE 
What is Merge Sort?
→ Merge Sort is a Divide-and-Conquer sorting algorithm that divides the array into smaller parts, sorts them, and then merges them.

Why is Merge Sort called Divide-and-Conquer?
→ Because it divides the array recursively, conquers by sorting the smaller arrays, and combines them by merging.

What is the time complexity of Merge Sort?
→ Best, average, and worst cases are O(N log N).

How are two sorted arrays merged?
→ We compare the first elements of both arrays, select the smaller element, and continue until all elements are merged.

What is the space complexity of Merge Sort?
→ O(N) because temporary arrays are used during the merging process.