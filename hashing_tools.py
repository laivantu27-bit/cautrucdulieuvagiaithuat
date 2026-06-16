from collections import defaultdict

# --- 2.1. Hash table dùng cho tra cứu đơn hàng ---
class OrderHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        
    def _hash(self, key):
        return hash(key) % self.capacity
        
    def insert(self, order_id, order_data):
        idx = self._hash(order_id)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == order_id:
                self.table[idx][i] = (order_id, order_data)
                return
        self.table[idx].append((order_id, order_data))
        
    def get(self, order_id):
        idx = self._hash(order_id)
        for k, v in self.table[idx]:
            if k == order_id: return v
        return None
        
    def remove(self, order_id):
        idx = self._hash(order_id)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == order_id:
                del self.table[idx][i]
                return True
        return False

def demo_order_hash_table():
    print("--- Demo Order Hash Table ---")
    ht = OrderHashTable()
    ht.insert("ORD001", {"item": "Laptop", "price": 1000})
    ht.insert("ORD002", {"item": "Mouse", "price": 50})
    print("Get ORD001:", ht.get("ORD001"))
    ht.remove("ORD001")
    print("Get ORD001 sau khi xóa:", ht.get("ORD001"))
    print()

# --- 2.2. Group anagrams ---
def group_coupon_anagrams(codes):
    groups = defaultdict(list)
    for code in codes:
        key = tuple(sorted(code))
        groups[key].append(code)
    return list(groups.values())

def demo_group_anagrams():
    codes = ["SAVE10", "AVES10", "10SAVE", "PROMO", "MOROP"]
    print("--- Demo Group Anagrams ---")
    groups = group_coupon_anagrams(codes)
    for g in groups: print(f"Nhóm: {g}")
    print("Ứng dụng: Phát hiện mã khác tên nhưng giống cấu trúc.\n")

# --- 2.3. Longest consecutive ---
def longest_consecutive_days(days):
    day_set = set(days)
    longest_streak = 0
    for day in day_set:
        if day - 1 not in day_set:
            current_day = day
            current_streak = 1
            while current_day + 1 in day_set:
                current_day += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak

def demo_longest_consecutive():
    days = [100, 4, 200, 1, 3, 2, 5]
    print("--- Demo Longest Consecutive Days ---")
    print(f"Chuỗi ngày liên tiếp dài nhất: {longest_consecutive_days(days)}\n")

# --- 2.4. Subarray sum = k ---
def count_revenue_windows(revenues, k):
    prefix_sums = {0: 1}
    current_sum = 0
    count = 0
    for rev in revenues:
        current_sum += rev
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
    return count

def demo_subarray_sum():
    revenues = [10, 20, 10, 5, 15, -5, 20]
    k = 30
    print("--- Demo Subarray Sum = k ---")
    print(f"Số đoạn con có tổng = {k}: {count_revenue_windows(revenues, k)}\n")

# --- 2.5. Rolling hash (Rabin-Karp) ---
def rolling_hash_search(text, pattern):
    if not pattern or not text or len(pattern) > len(text): return []
    d = 256
    q = 101 # Số nguyên tố
    m = len(pattern)
    n = len(text)
    p_hash = 0
    t_hash = 0
    h = 1
    res = []
    
    for i in range(m - 1): h = (h * d) % q
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
        
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i+m] == pattern: res.append(i)
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0: t_hash += q
    return res

def demo_rolling_coupon_search():
    text = "LOG: User applied SAVE10. LOG: Invalid code. LOG: SAVE10 success."
    pattern = "SAVE10"
    print("--- Demo Rolling Hash Search ---")
    print(f"Tìm thấy '{pattern}' tại các index: {rolling_hash_search(text, pattern)}\n")