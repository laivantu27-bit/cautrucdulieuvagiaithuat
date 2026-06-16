print("DSU 1")
def make_set(vertices):
    """
    Khởi tạo DSU: mỗi đỉnh là một nhóm riêng, parent[v] = v.
    """
    parent = {}
    for v in vertices:
        parent[v] = v
    return parent

def find(parent, v):
    """
    Tìm root (trưởng nhóm) của v, leo lên tới khi parent[v] == v.
    """
    while parent[v] != v:
        v = parent[v]
    return v

def union(parent, a, b):
    """
    Gộp nhóm chứa a và nhóm chứa b.
    """
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a  # Cho root_b nhập hội root_a

def demo_dsu_basic():
    vertices = ['A', 'B', 'C', 'D', 'E']
    parent = make_set(vertices)

    ops = [
        ("union", 'A', 'B'),
        ("union", 'C', 'D'),
        ("find", 'B'),
        ("union", 'B', 'C'),
        ("find", 'D'),
        ("find", 'E'),
    ]

    for op in ops:
        if op[0] == "union":
            _, x, y = op
            print(f"Thực hiện union({x}, {y})")
            union(parent, x, y)
        else:
            _, x = op
            root = find(parent, x)
            print(f"find({x}) = {root}")

    print("parent hiện tại:", parent)

if __name__ == "__main__":
    demo_dsu_basic()

print("DSU 2")
import time

# --- Basic DSU ---
def make_set_basic(vertices):
    return {v: v for v in vertices}

def find_basic(parent, v):
    steps = 0
    while parent[v] != v:
        v = parent[v]
        steps += 1
    return v, steps

def union_basic(parent, a, b):
    root_a, _ = find_basic(parent, a)
    root_b, _ = find_basic(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a

# --- Optimized DSU ---
def make_set_optimized(vertices):
    parent = {v: v for v in vertices}
    size = {v: 1 for v in vertices}
    return parent, size

def find_optimized(parent, v, steps=0):
    if parent[v] != v:
        # Ghi nhận bước nén đường đi
        root, s = find_optimized(parent, parent[v], steps + 1)
        parent[v] = root
        return root, s
    return v, steps

def union_optimized(parent, size, a, b):
    root_a, _ = find_optimized(parent, a)
    root_b, _ = find_optimized(parent, b)
    if root_a != root_b:
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        size[root_a] += size[root_b]

# --- Bài tập So sánh ---
def compare_dsu(n=1000):
    # Tạo chuỗi dài union(0,1), union(1,2)...
    print(f"--- So sánh với n = {n} đỉnh ---")
    
    # Test Basic
    parent_b = make_set_basic(range(n))
    for i in range(n - 1):
        union_basic(parent_b, i, i + 1)
        
    # Test Optimized
    parent_o, size_o = make_set_optimized(range(n))
    for i in range(n - 1):
        union_optimized(parent_o, size_o, i, i + 1)

    # Đo số bước find(0) sau khi đã tạo chuỗi
    _, steps_basic = find_basic(parent_b, 0)
    _, steps_opt = find_optimized(parent_o, 0)

    print(f"Số bước find(0) (Basic): {steps_basic}")
    print(f"Số bước find(0) (Optimized): {steps_opt}")

if __name__ == "__main__":
    compare_dsu(1000)