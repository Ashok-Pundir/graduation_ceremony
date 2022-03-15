import copy

def generate_all_combinations(days, total_combinations):
    """
        Complexity: O((2^n)*(n))
    """
    arr = []
    miss_grad_ceremony = 0

    # Copy First combination
    temp = [0]*days
    arr.append(temp)
    total_combinations -= 1

    temp = copy.copy(arr[-1])

    while(total_combinations > 0):
        j = days - 1

        for k in range(j, -1, -1):
            if temp[k] == 0:
                temp[k] = 1
                break
            else:
                temp[k] = 0
                if temp[k-1] == 0:
                    temp[k-1] = 1
                    break
                else:
                    temp[k-1] = 1

        arr.append(temp)
        temp = copy.copy(arr[-1])

        total_combinations -= 1

    return arr

def count_consecutive_four_or_more_zero(arr):
    """
        Checking For each Combination
        Complexity: O((2^n)*(n))
    """
    var_count_consecutive_four_or_more_zero, miss_grad_ceremony = 0, 0
    for sub_arr in arr:
        count = 0
        invalid_combination = 0

        for elem in sub_arr:

            if elem&1 == 0:
                count += 1
            else:
                count = 0
            
            if count >= 4:
                var_count_consecutive_four_or_more_zero += 1
                invalid_combination = 1
                break

        if not invalid_combination and sub_arr[-1] == 0:
            miss_grad_ceremony += 1

    return var_count_consecutive_four_or_more_zero, miss_grad_ceremony


no_of_days = int(input('Enter Number of Days: '))
total_combinations = 1 << no_of_days

arr = generate_all_combinations(no_of_days, total_combinations)

combination_consecutive_count_zeros, miss_grad_ceremony = count_consecutive_four_or_more_zero(arr)

print("{}/{}".format(miss_grad_ceremony, total_combinations-combination_consecutive_count_zeros))