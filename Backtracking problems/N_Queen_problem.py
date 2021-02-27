# printing all solution of N queen problem
from itertools import permutations

n = 4
sol = 0
col = range(n)

for combo in permutations(col):
    if n == len(set(combo[i] + i for i in col)) == len(set(combo[i] - i for i in col)):
        sol += 1
        print(f'Solution {sol} : {combo}')
        print('\n'.join(' 0 ' * i + ' 1 ' + ' 0 ' * (n-i-1) for i in combo)+ '\n\n\n\n')
