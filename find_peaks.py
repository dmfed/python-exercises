'''
Find peaks in array  of ints. Report position and
value of peaks.'''

def pick_peaks(array):
    peaks = []
    indices = []
    prevmin = prevmax = 0
    for i in range(len(array)):
        if array[i] < array[prevmax] and array[prevmin] < array[prevmax]:
            peaks.append(array[prevmax])
            indices.append(prevmax)
            prevmin = prevmax = i
        if array[i] > array[prevmax]:
            prevmin, prevmax = prevmax, i
        if array[i] <= array[prevmin]:
            prevmin = prevmax = i
    return {"pos": indices, "peaks": peaks}


print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))

assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) == {"pos": [3, 7, 10], "peaks": [6, 3, 2]}
assert pick_peaks([1,2,3,6,4,1,2,3,2,1]) == {"pos":[3,7], "peaks":[6,3]}
assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]) == {"pos":[3,7], "peaks":[6,3]}
assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) == {"pos":[3,7,10], "peaks":[6,3,2]}
assert pick_peaks([2,1,3,1,2,2,2,2,1]) == {"pos":[2,4], "peaks":[3,2]}
assert pick_peaks([2,1,3,1,2,2,2,2]) == {"pos":[2], "peaks":[3]}
assert pick_peaks([2,1,3,2,2,2,2,5,6]) == {"pos":[2], "peaks":[3]}
assert pick_peaks([2,1,3,2,2,2,2,1]) == {"pos":[2], "peaks":[3]}
assert pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]) == {"pos":[2,7,14,20], "peaks":[5,6,5,5]}
assert pick_peaks([]) == {"pos":[],"peaks":[]}
assert pick_peaks([1,1,1,1]) == {"pos":[],"peaks":[]}
