import copy


def load_data_to_list():
    fname = "data.txt"

    arrs = []

    with open(fname, "r") as infile:
        for line in infile:
            arrs.append([int(x) for x in line.split()])

    assert len(arrs[0]) == 1
    return arrs


arrs = load_data_to_list()

max_p_sum = arrs[0]

for arr in arrs[1:]:
    assert len(arr) == len(max_p_sum) + 1

    mps_new = copy.deepcopy(max_p_sum)

    # First element
    mps_new[0] += arr[0]

    # Middle elements
    for i in range(1, len(max_p_sum)):
        mps_new[i] = arr[i] + max(max_p_sum[i], max_p_sum[i-1])

    # Final (new) element
    mps_new.append(max_p_sum[-1] + arr[-1])
    
    max_p_sum = mps_new


print(max(max_p_sum))



