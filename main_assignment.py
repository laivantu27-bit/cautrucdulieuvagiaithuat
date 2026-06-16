import routing
import hashing_tools
import promo_optimizer

def main():
    while True:
        print("====== HỆ THỐNG HẬU CẦN POLY-SHIP ======")
        print("1. Demo routing - shortest path giữa 2 kho")
        print("2. Demo MST - mạng kho tối thiểu")
        print("3. Demo hash table đơn hàng")
        print("4. Demo hashing: group anagrams, ngày liên tiếp, subarray sum = k")
        print("5. Demo rolling hash tìm pattern trong log")
        print("6. Demo DP cơ bản (fibonacci, climbing stairs)")
        print("7. Demo combo khuyến mãi (knapsack 0/1 - 2D, 1D)")
        print("8. Thoát")
        
        choice = input("Nhập lựa chọn của bạn (1-8): ")
        print()
        
        if choice == '1':
            routing.demo_routing_shortest_path()
        elif choice == '2':
            routing.demo_mst_network()
        elif choice == '3':
            hashing_tools.demo_order_hash_table()
        elif choice == '4':
            hashing_tools.demo_group_anagrams()
            hashing_tools.demo_longest_consecutive()
            hashing_tools.demo_subarray_sum()
        elif choice == '5':
            hashing_tools.demo_rolling_coupon_search()
        elif choice == '6':
            promo_optimizer.demo_dp_basics()
        elif choice == '7':
            promo_optimizer.demo_combo_knapsack_2d()
            promo_optimizer.demo_combo_knapsack_1d()
        elif choice == '8':
            print("Đã thoát hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại!\n")

if __name__ == "__main__":
    main()