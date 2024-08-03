import timeit


def insertion_sort(data):
    lst = data.copy()
    for i in range(1, len(lst)):
        key = lst[i]

        j = i-1

        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1

        lst[j+1] = key
    return lst


def merge_sort(data):
    arr = data.copy()
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def time_count(data, loops: int = 10000):
    mrg_time = 0
    ins_time = 0
    sorted_time = 0
    sort_time = 0

    print(f"\nAfter \033[93m{loops} loops\x1b[0m each algorithm tooks in \033[96maverage\x1b[0m:")
    print(f"{"Input data:":<13} {data}")

    for i in range(0, loops):

        t = timeit.timeit("merge_sort(data)", number=1, globals={"merge_sort": merge_sort, "data": data})
        mrg_time += t

        t = timeit.timeit("insertion_sort(data)", number=1, globals={"insertion_sort": insertion_sort, "data": data})
        ins_time += t

        t = timeit.timeit("sorted(data)", number=1, globals={"data": data})
        sorted_time += t

        t = timeit.timeit("data.sort()", number=1, globals={"data": data})
        sort_time += t

    mrg_time, ins_time = mrg_time/loops * 1000000, ins_time/loops * 1000000
    sorted_time, sort_time = sorted_time/loops * 1000000, sort_time/loops * 1000000

    print(f"{"Sorted data:":<13} {data}")
    print(f"\033[96m{"Merge sort:":<12} \033[93m{mrg_time:.10f}\x1b[0m μs")
    print(f"\033[96m{"Insertion:":<12} \033[93m{ins_time:.10f}\x1b[0m μs")
    print(f"\033[96m{"Sorted:":<12} \033[93m{sorted_time:.10f}\x1b[0m μs")
    print(f"\033[96m{"Sort method:":<12} \033[93m{sort_time:.10f}\x1b[0m μs")

    return mrg_time, ins_time, sorted_time, sort_time


def main():
    mrg_total = 0
    ins_total = 0
    sorted_total = 0
    sort_total = 0

    def time_sum(a, b, c, d):
        nonlocal mrg_total, ins_total, sorted_total, sort_total
        mrg_total += a
        ins_total += b
        sorted_total += c
        sort_total += d

    a, b, c, d = time_count([5, 3, 8, 4, 2])
    time_sum(a, b, c, d)

    a, b, c, d = time_count([58.99774, 3.823, 0.28364, 23.0472, 892.88723668])
    time_sum(a, b, c, d)

    a, b, c, d = time_count(["some", "few", "words", "in", "random", "order"])
    time_sum(a, b, c, d)

    print("\nIn total:")
    print(f"\033[96m{"Merge:":<12} \033[93m{mrg_total/3:.10f}\x1b[0m μs")
    print(f"\033[96m{"Insertion:":<12} \033[93m{ins_total/3:.10f}\x1b[0m μs")
    print(f"\033[96m{"Sorted:":<12} \033[93m{sorted_total/3:.10f}\x1b[0m μs")
    print(f"\033[96m{"Sort method:":<12} \033[93m{sort_total/3:.10f}\x1b[0m μs\n")
    

if __name__ == "__main__":
    main()