import numpy as np


sequence1 = "AGTCGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"
sequence2 = "TACGTACGTACGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC"


arr1 = np.array(list(sequence1))
arr2 = np.array(list(sequence2))


length1 = len(arr1)
length2 = len(arr2)


matches = np.sum(arr1 == arr2)


similarity_percentage = (matches / min(length1, length2)) * 100

print(f"Sequence 1: {sequence1}")
print(f"Sequence 2: {sequence2}")
print(f"Sequence Lengths: {length1}, {length2}")
print(f"Matching Positions: {matches}")
print(f"Similarity Percentage: {similarity_percentage:.2f}%")
