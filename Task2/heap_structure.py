# Heap

class MaxHeap:
   def __init__(self, items=[]): 
    self.data = list(items)
    if len(self.data) > 0:
        self.build_heap()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

   def sift_down(self, i):
    n = len(self.data) 
    
    while True:
        largest = i
        l = self.left(i)   
        r = self.right(i)  

        if l < n and self.data[l] > self.data[largest]:
            largest = l
            
        if r < n and self.data[r] > self.data[largest]:
            largest = r

        if largest == i:
            break

        self.swap(i, largest)
        i = largest
 
    def sift_up(self, i):
       
        while i > 0:
            p = self.parent(i)
            if self.data[i] <= self.data[p]:
                break
            self.swap(i, p)
            i = p

    # Build a max heap
    def build_heap(self):
      
        n = len(self.data)
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(i)

    # Insert a new value
    def push(self, value):
        
        self.data.append(value)
        self.sift_up(len(self.data) - 1)

    # Return the maximum value 
    def peek(self):
        
        if self.is_empty():
            return None
        return self.data[0]

    # Remove and return the maximum value 
    def pop(self):
        
        if self.is_empty():
            return None

        max_value = self.data[0]
        last = self.data.pop()
        if not self.is_empty():
            self.data[0] = last
            self.sift_down(0)
        return max_value

    # Return the sorted list 
    def sort_list(self):
        
        copied = MaxHeap(self.data)
        result = []
        while not copied.is_empty():
            result.append(copied.pop())
        result.reverse()
        return result

    def __str__(self):
        return f"MaxHeap({self.data})"


if __name__ == "__main__":
    nums = [7, 1, 9, 3, 2, 8]
    print("Original data:", nums)

    heap = MaxHeap(nums)
    print("After building heap:", heap)
    print("Current maximum (peek):", heap.peek())

    heap.push(10)
    print("After pushing 10:", heap)

    print("Popping all elements:", end=" ")
    while not heap.is_empty():
        print(heap.pop(), end=" ")
    print()
