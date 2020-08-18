'''
Starting with a 1-indexed array of zeros and a list of operations, for each operation 
add a value to each of the array element between two given indices, inclusive. Once 
all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros . Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of k between the indices  and  inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is 10 after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Constraints

Output Format

Return the integer maximum value in the finished array.
''' 

def arrayManipulation(n, queries):
    arr = [0 for _ in range(n+1)] ## Note that array is of n+1 length 
    for start, end, val in queries:
        arr[start-1] += val 
        arr[end] -= val ##since array is 1 index longer we can afford this
    result = 0
    s = 0
    print(arr)
    for val in arr:
        s += val
        result = max(s, result)
    return result

q = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

assert arrayManipulation(10, q) == 10

'''
This solution has O(n) complexity compareg to simplest O(n^2) option.
(also O(n^2) does not pass tests)'''