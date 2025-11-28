# USACO 2023 Dec Bronze - P3: Farmer John Actually Farms

def ceiling(a, b):
    return (a + b - 1) // b

def solve():
    N = int(input())
    h = [int(x) for x in input().split()]  # Initial heights
    a = [int(x) for x in input().split()]  # Growth rates
    t = [int(x) for x in input().split()]  # Comparison conditions

    # Generate an order list mapped from t list.
    # E.g. index:  0  1  2  3  4
    #         t = [4, 0, 3, 1, 2]
    #  => order = [1, 3, 4, 2, 0]
    order = list(range(N))
    for i in range(N):
        order[t[i]] = i

    days = 0

    for idx in range(N - 1):
        i = order[idx]
        j = order[idx + 1]
        # For each adjacent pair in order, compute minimal days so that
        # h[i] > h[j] if initially h[i] < h[j] and a[i] > a[j].
        # Use ceiling division to get the smallest integer day count.
        # Keep the maximum of these lower bounds for all such pairs.
        if h[i] < h[j] and a[i] > a[j]:
            days = max(days, ceiling(h[j] - h[i] + 1, a[i] - a[j]))

    # The 'days' computed above is the maximum lower bound for pairs where
    # h[i] < h[j] and a[i] > a[j]. But some other pairs with h[i] > h[j]
    # initially but a[i] < a[j], there is an upper bound: after enough days
    # h[i] may become <= h[j]. Verify that the chosen 'days' satisfy all
    # adjacent pairs in order.
    for i in range(N):
        h[i] += a[i] * days

    for idx in range(N - 1):
        i = order[idx]
        j = order[idx + 1]
        if h[i] <= h[j]:
            return -1

    return days


if __name__ == "__main__":
    num_cases = int(input())
    for _ in range(num_cases):
        print(solve())
