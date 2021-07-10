
# Bubble sort implementation
# Bubble Sort Implementation

# n =5 
# for i in range(n):
#     print("loop 1: i- \n----------", i )
#     for j in range(n-i-1):
#         print("j-%d" % j)

# ---------------------------------------Small to Large------------------------------------------

def bubble_sort(data_list):
    n = len(data_list)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if data_list[j] > data_list[j+1]:
                # swap
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp

if __name__ == "__main__":
    data_list = [90, 30, 2, 40, 1, 50]
    bubble_sort(data_list)
    print("Bubble sort list:  " , data_list)


# ------------------------------------------Large to Small--------------------------------------

def bubble_sort(data_list):
    n = len(data_list)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if data_list[j] < data_list[j+1]:
                 # sawp
                 temp = data_list[j]
                 data_list[j] = data_list[j+1]
                 data_list[j+1] = temp

if __name__ == "__main__":
    data_list = [10, 30, 20, 5, 15, 25, 40]
    bubble_sort(data_list)
    print("Bubble sort list: " , data_list)

