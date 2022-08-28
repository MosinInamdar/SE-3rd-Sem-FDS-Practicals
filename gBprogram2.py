'''
    Write a python program to store roll numbers of student array who attended training program in sorted
    order.Write function for searching whether particular student attended training program or not, 
    using Binary search and Fibonacci search.
'''
l=[]
def get():
    n=int(input("Enter the number of students in the class : "))
    for i in range(n):
        k=int(input("Enter roll no. : "))
        l.append(k)

def dis():
    for i in l:
        print(i,end=" ")

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

def fibMonaccianSearch(arr, x, n):
  
    # Initialize fibonacci numbers
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
  
    # fibM is going to store the smallest
    # Fibonacci Number greater than or equal to n
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
  
    # Marks the eliminated range from front
    offset = -1
  
    # while there are elements to be inspected.
    # Note that we compare arr[fibMm2] with x.
    # When fibM becomes 1, fibMm2 becomes 0
    while (fibM > 1):
  
        # Check if fibMm2 is a valid location
        i = min(offset+fibMMm2, n-1)
  
        # If x is greater than the value at
        # index fibMm2, cut the subarray array
        # from offset to i
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
  
        # If x is less than the value at
        # index fibMm2, cut the subarray
        # after i+1
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
  
        # element found. return index
        else:
            return i
  
    # comparing the last element with x */
    if(fibMMm1 and arr[n-1] == x):
        return n-1
  
    # element not found. return -1
    return -1


if __name__=='__main__':
    get()
    dis()

    print("\n1.Binary Search")
    print("2.Fibonacci Search")
    ch=int(input("Enter your choice : "))
    if(ch==1):
        x=int(input("Enter Roll for searching whether perticular "
                    "student attended training program or not "))
        result = binary_search(l, 0, len(l)-1, x)
        if result != -1:
            print("Roll no. found at ", int(result)," location")
        else:
            print("Roll no. is absent")
    elif(ch==2):
        n = len(l)
        x = l[-1]
        ind = fibMonaccianSearch(l, x, n)
        if ind>=0:
            print("Found at index:",ind)
        else:
            print(x,"isn't present in the array");    
    else:
        print("Wrong Input!!")
