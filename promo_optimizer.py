# --- 3.1. Ôn lại DP nhẹ: stairs & fibonacci ---
def fib_memo(n, memo=None):
    if memo is None: memo = {}
    if n <= 1: return n
    if n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def climb_stairs(n):
    if n <= 2: return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def demo_dp_basics():
    print("--- Demo DP Basics ---")
    n = 10
    print(f"Fibonacci thứ {n}: {fib_memo(n)}")
    print(f"Số cách leo {n} bậc thang: {climb_stairs(n)}\n")

# --- 3.2. Khuyến mãi combo (knapsack 0/1) 2D ---
def build_combo_dp_table(prices, scores, B):
    n = len(prices)
    dp = [[0] * (B + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for b in range(B + 1):
            if prices[i-1] <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b - prices[i-1]] + scores[i-1])
            else:
                dp[i][b] = dp[i-1][b]
    return dp

def trace_combo_from_dp(dp, prices, scores, B):
    n = len(prices)
    selected = []
    b = B
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i-1][b]:
            selected.append(i-1) # Lưu index
            b -= prices[i-1]
    selected.reverse()
    return selected

def demo_combo_knapsack_2d():
    prices = [10, 20, 30, 40]
    scores = [30, 50, 40, 70]
    B = 50
    dp = build_combo_dp_table(prices, scores, B)
    selected = trace_combo_from_dp(dp, prices, scores, B)
    print("--- Demo Combo Knapsack (2D) ---")
    print(f"Max score: {dp[-1][-1]}")
    print(f"Sản phẩm được chọn (index): {selected}\n")

# --- 3.3. Tối ưu memory: knapsack 1D ---
def combo_knapsack_1d(prices, scores, B):
    dp = [0] * (B + 1)
    for i in range(len(prices)):
        for b in range(B, prices[i] - 1, -1):
            dp[b] = max(dp[b], dp[b - prices[i]] + scores[i])
    return dp[B]

def demo_combo_knapsack_1d():
    prices = [10, 20, 30, 40]
    scores = [30, 50, 40, 70]
    B = 50
    print("--- Demo Combo Knapsack (1D) ---")
    print(f"Max score (1D): {combo_knapsack_1d(prices, scores, B)}")
    print("Nhận xét: Kết quả giống bản 2D nhưng tiết kiệm không gian bộ nhớ.\n")