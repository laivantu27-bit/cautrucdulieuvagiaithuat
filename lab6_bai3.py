print("Kruskal dùng DSU ")
# Giả định các hàm DSU đã được định nghĩa từ bài trước
def make_set(vertices):
    return {v: v for v in vertices}

def find(parent, v):
    while parent[v] != v:
        v = parent[v]
    return v

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a

def kruskal_mst_basic(vertices, edges):
    """
    Kruskal MST dùng DSU basic.
    """
    # B1: Sort cạnh theo trọng số (e[0] là weight)
    edges_sorted = sorted(edges, key=lambda e: e[0])

    # B2: Khởi tạo DSU
    parent = make_set(vertices)

    mst = []
    total_weight = 0

    print("Cạnh sau khi sort (w, u, v):")
    for e in edges_sorted:
        print(" ", e)

    print("\nDuyệt từng cạnh:")
    for w, u, v in edges_sorted:
        root_u = find(parent, u)
        root_v = find(parent, v)
        print(f"Xét cạnh {u}-{v} (w={w}), root_u={root_u}, root_v={root_v}")

        if root_u != root_v:
            print(" → Khác nhóm → CHỌN cạnh này")
            mst.append((u, v, w))
            total_weight += w
            union(parent, u, v)
        else:
            print(" → Cùng nhóm → BỎ (tránh chu trình)")

        # Nếu đã đủ |V|-1 cạnh, có thể dừng luôn
        if len(mst) == len(vertices) - 1:
            break

    return mst, total_weight

# Dữ liệu test
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    (1, 'A', 'B'),
    (4, 'A', 'C'),
    (3, 'B', 'C'),
    (2, 'B', 'D'),
    (5, 'C', 'E'),
    (2, 'D', 'E'),
]

mst, total_weight = kruskal_mst_basic(vertices, edges)
print(f"\nMST cuối cùng: {mst}")
print(f"Tổng trọng số: {total_weight}")

print("Kruskal dùng DSU optimized")
# Giả định các hàm DSU tối ưu đã được định nghĩa từ bài lab trước:
# make_set_optimized, find_optimized, union_optimized

def kruskal_mst_optimized(vertices, edges):
    """
    Kruskal MST với DSU tối ưu: path compression + union by size.
    """
    # B1: Sắp xếp cạnh theo trọng số (e[0] là weight) [cite: 539]
    edges_sorted = sorted(edges, key=lambda e: e[0])
    
    # B2: Khởi tạo DSU tối ưu [cite: 418-419]
    parent, size = make_set_optimized(vertices)

    mst = []
    total_weight = 0

    # B3: Duyệt các cạnh đã sắp xếp
    for w, u, v in edges_sorted:
        # Sử dụng find_optimized với path compression [cite: 423-426]
        root_u = find_optimized(parent, u)
        root_v = find_optimized(parent, v)
        
        # Nếu khác nhóm, gộp nhóm bằng union_optimized 
        if root_u != root_v:
            mst.append((u, v, w))
            total_weight += w
            union_optimized(parent, size, u, v)
            
        # Nếu đã đủ số cạnh trong cây khung (V-1), dừng lại [cite: 545]
        if len(mst) == len(vertices) - 1:
            break

    return mst, total_weight

# --- Ví dụ sử dụng ---
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    (1, 'A', 'B'),
    (4, 'A', 'C'),
    (3, 'B', 'C'),
    (2, 'B', 'D'),
    (5, 'C', 'E'),
    (2, 'D', 'E'),
]

mst, total_weight = kruskal_mst_optimized(vertices, edges)
print(f"MST (Tối ưu): {mst}")
print(f"Tổng trọng số: {total_weight}")

print("Hàm test tổng hợp MST")
def test_kruskal():
    # Định nghĩa đỉnh và các cạnh (trọng số, đỉnh u, đỉnh v)
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        (1, 'A', 'B'),
        (4, 'A', 'C'),
        (3, 'B', 'C'),
        (2, 'B', 'D'),
        (5, 'C', 'E'),
        (2, 'D', 'E'),
    ]

    print("=== Kruskal với DSU basic ===")
    mst1, total1 = kruskal_mst_basic(vertices, edges)
    print("\nMST basic:")
    for u, v, w in mst1:
        print(f"  {u}-{v} (w={w})")
    print("Tổng trọng số:", total1)

    print("\n=== Kruskal với DSU optimized ===")
    mst2, total2 = kruskal_mst_optimized(vertices, edges)
    print("\nMST optimized:")
    for u, v, w in mst2:
        print(f"  {u}-{v} (w={w})")
    print("Tổng trọng số:", total2)

if __name__ == "__main__":
    test_kruskal()