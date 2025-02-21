#from numpy.ma.core import indices, count
#from pandas.conftest import indices_dict

indexes = []


def find_pair_combinations(k, target):
    count: int = 0
    for i in range(len(k)):
        for j in range(len(k)):
            if i == j and k[i] == target:
                indexes.append((i, j))
                count += 1
                continue
            if k[j] == target:
                indexes.append((i, j))
                count += 1
                continue
            if (k[i] + k[j]) == target:
                indexes.append((i, j))
                count += 1
    print(f'Count ; {count} List indexes ; {indexes}')
    return count, indexes


input_params: str = input("Enter the input list\n")
print(f'input parameter string : {input_params}')
input_params = list(input_params.strip())
input_params = [ele for ele in input_params if ele != ' ']
input_params_list = list(map(int, input_params))
print(f'input list {input_params_list}')
target = input("Enter the target value:\n")
target = int(target)
noofoccurances, index_list = find_pair_combinations(input_params_list, target)

print(f'input list  = {input_params_list}')
print(f'target number  = {target}')

print(f'number of occurances = {noofoccurances}')
print(f'List indices = {index_list}')

