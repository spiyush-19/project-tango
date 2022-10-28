# Returns true if there exists a subsequence of `A[0…n]` with the given sum
def subsetSum(A, n, k):
 
    # return true if the sum becomes 0 (subset found)
    if k == 0:
        return True
 
    # base case: no items left, or sum becomes negative
    if n < 0 or k < 0:
        return False
 
    # Case 1. Include the current item `A[n]` in the subset and recur
    # for the remaining items `n-1` with the remaining total `k-A[n]`
    include = subsetSum(A, n - 1, k - A[n])
 
    # Case 2. Exclude the current item `A[n]` from the subset and recur for
    # the remaining items `n-1`
    exclude = subsetSum(A, n - 1, k)
 
    # return true if we can get subset by including or excluding the
    # current item
    return include or exclude
 
 
# Subset Sum Problem
if __name__ == '__main__':
 
    # Input: a set of items and a sum
    A = [7, 3, 2, 5, 8]
    k = 14
 
    if subsetSum(A, len(A) - 1, k):
        print('Subsequence with the given sum exists')
    else:
        print('Subsequence with the given sum does not exist')
 
