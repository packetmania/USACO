# USACO 2024 January Contest, Bronze: P3. Balancing Bacteria

def solve():
    # Solution with simulation approach:
    #   For each a[i], if it is not 0, apply the operation to make it 0,
    #   and update all a[j] (j>i) accordingly. Count the number of operations.
    #
    # Time complexity O(n^2)
    N = int(input())
    a = [int(x) for x in input().split()]
    num = 0

    for i in range(N):
        if a[i] != 0:
            for j in range(i+1, N):
                a[j] += -a[i] * (j - i + 1)
            num += abs(a[i])  ## Remember to use abs() here!

    return num


def solve_fast():
    # Solution with prefix-sum like algorithm:
    #
    # Time complexity O(n)
    N = int(input())
    a = [int(x) for x in input().split()]

    num = 0      # total number of operations
    effects = 0  # total effect on current position from all previous operations
    sum_ops = 0  # algebraic sum of operations (+1 for add, -1 for remove)

    for i in range(N):
        effects += sum_ops  # update effects from all previous operations
        a[i] += effects     # apply effects to a[i]

        cur_ops = -a[i]      # number of operations needed make a[i] become 0
        num += abs(cur_ops)  # update total number of operations

        sum_ops += cur_ops   # # update the global operation algebraic sum

        # these new operations also affect the current position immediately
        effects += cur_ops

    return num

if __name__ == "__main__":
    print(solve_fast())
