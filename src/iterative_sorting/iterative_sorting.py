# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        current = i
        smallest = current
        for n in range(i+1, len(arr)):
           if arr[n]< arr[smallest]:
              smallest = n
        arr[current], arr[smallest] = arr[smallest], arr[current]
        
    return arr

tester = [5,12,23,56,11,22,4,7,3,2,1]
print(selection_sort(tester))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr