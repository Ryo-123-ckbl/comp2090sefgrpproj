# Heap sort

def heapify(arr, n, i):

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# sort in ascending order
def heap_sort(arr):

    n = len(arr)
    if n <= 1:
        return

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)


if __name__ == "__main__":
    
    data1 = [9, 4, 1, 6, 7, 3]
    print("Before sorting data1:", data1)
    heap_sort(data1)
    print("After sorting data1:", data1)

    data2 = [5, 5, 2, 10, -1, 0]
    print("Before sorting data2:", data2)
    heap_sort(data2)
    print("After sorting data2:", data2)
