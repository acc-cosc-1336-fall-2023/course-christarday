def get_p_distance(list1, list2):
    count = 0
    if len(list1) != len(list2):
        raise ValueError("DNA strings are not of equal length")
    else:
        for x in range(len(list1)):
            if list1[x] != list2[x]:
                count += 1
        return round((count / len(list1)), 5)


def get_p_distance_matrix_for(nested_list):
    k = len(nested_list)
    matrix = []

    for i in range(k):
        row = []
        for j in range(k):
            x = get_p_distance(nested_list[i], nested_list[j])
            row.append(x)
        matrix.append(row)

    return matrix

def get_p_distance_matrix_while(long_list):
    k = len(long_list)
    matrix = []
    i = 0
    while i < k:
        row = [0.0] * k
        j = 0
        
        while j < k:
            row[j] = (get_p_distance(long_list[i], long_list[j]))
            j += 1
        
        matrix.append(row)

        i += 1

    return matrix
    



