# USACO 2023 Dec Brone - P2: Cowntact Tracing 2
# https://usaco.org/index.php?page=viewproblem2&cpid=1348

# Sample input:
# 6
# 011101

def solve():

    N = int(input().strip())
    cows = input().strip()

    if "1" not in cows:
        print(0)
        return

    # Generate a list of contiguous 1's (for infected cows).
    # Each group is indicated with 0-based index: [l, r] 
    segments = []

    l = 0
    while l < N:
        if cows[l] == '1':
            # Find a starting point of an infected cow group
            r = l
            while r < N and cows[r] == '1':
                r += 1
            # No more continuous 1's
            segments.append((l, r - 1))
            l = r
        else:
            # It is 0, move to the next.
            l += 1

    W_max = float('inf')

    # Segments would be [(1, 3), (5, 5)] now.

    # Scan each segment to calculate the max allowed Window size,
    # then find the minimum of the max size for W_max.

    for l, r in segments:
        I = r - l + 1  # I - length of this segment
        left_edge = (l == 0)
        right_edge = (r == N - 1)
        
        if left_edge or right_edge:
            # edge segment：W_allowed = 2 * I - 1, for segment (5, 5)
            allowed = 2 * I - 1
        else:
            # middle segment
            if I % 2 == 0:
                # even length：W_allowed = I - 1
                allowed = I - 1
            else:
                # Odd length：W_allowed = I, for segment (1, 3)
                allowed = I
        W_max = min(W_max, allowed)


    # W_max would be 1 for the sample input

    ans = 0
    for l, r in segments:
        I = r - l + 1
        ans += (I + W_max - 1) // W_max  # Same as math.ceil(I / W_max)

    print(ans)
        

if __name__ == "__main__":
    solve()
    
    
