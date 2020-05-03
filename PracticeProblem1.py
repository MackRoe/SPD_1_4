def check_for_dupes(num_list):
    current_n = num_list[0]
    for i in range(1, (len(num_list) - 1)):
        next_n = num_list[i]
        if next_n > current_n:
            greatest_n = next_n
            print('Greatest number is :', greatest_n)
            print('at iteration ', i)
            next_n = num_list[i + 1]
        else:
            greatest_n = current_n
            next_n = num_list[i + 1]
    return greatest_n


List1 = [9, 8, 12, 90, 8]
List2 = [2, 4, 6, 12, 20]

print(check_for_dupes(List2))
