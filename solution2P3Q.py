# A Python function that, given a non-negative integer N, 
# returns the value A[N] in a generated set S that consist of 
# numbers of the form 2^P*3^Q, where P and Q are non-negative integers.

# N is the number of elements generated
def solution2P3Q(N):
    list2p3q = []
    p = 0
    while p < N:
        v2p = 2 ** p
        q = 0
        while q < N:
            v3q = 3 ** q
            v2p3q = v2p * v3q
            # store the calculated value
            list2p3q.append(v2p3q)
            q+= 1
        p+= 1
    # sorting the values
    list2p3q.sort()
    # return the element in N'th index
    return list2p3q[N]

print(solution2P3Q(8))