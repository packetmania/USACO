# USACO 2024 January Contest, Bronze: P3. Balancing Bacteria

def solve():
    # Solution with simulation approach algorithm:
    #   For each a[i], if it is not 0, apply the operation to make it 0,
    #   and update all a[j] (j>i) accordingly. Count the number of operations.
    #
    # Time complexity O(n^2)
    N = int(input())
    a = [int(x) for x in input().split()]
    num = 0

    for i in range(0, N):
        if a[i] != 0:
            for j in range(i+1, N):
                a[j] += -a[i] * (j - i + 1)
            num += abs(a[i])  ## Remember to use abs() here!

    return num


def solve():
    # Solution with simulation approach algorithm:
    #   For each a[i], if it is not 0, apply the operation to make it 0,
    #   and update all a[j] (j>i) accordingly. Count the number of operations.
    #
    # Time complexity O(n^2)
    N = int(input())
    a = [int(x) for x in input().split()]
    num = 0

    for i in range(0, N):
        if a[i] != 0:
            for j in range(i + 1, N):
                a[j] += -a[i] * (j - i + 1)
            num += abs(a[i])  ## Remember to use abs() here!

    return num

if __name__ == "__main__":
    print(solve())
