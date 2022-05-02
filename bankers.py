# start here
print('\nBANKER\'S ALGORITHM\n')
n = int(input('Enter the number of processes: '))
print('Enter total resources: ', end = '')
tot_resources = list(map(int,input().strip().split()))
allocation = list()
max_need = list()
rem_need = list()
tot_allocation = [0, 0, 0]
available = [0, 0 ,0]
for i in range(n):
    print('Allocated Resources for P%d :'%i, end = '')
    allo = list(map(int,input().strip().split()))
    allocation.append(allo)
    print('Maximum need for P%d :'%i, end = '')
    mneed = list(map(int,input().strip().split()))
    max_need.append(mneed)
    # to calcutate max - allo
    temp = list()
    for j in range(3):
        k = mneed[j] - allo[j]
        temp.append(k)
        tot_allocation[j] = tot_allocation[j] + allo[j]
    rem_need.append(temp)
for j in range(3):
    available[j] = tot_resources[j] - tot_allocation[j]
safe = list()
rem_process = list()
# starting algo
for i in range(n):
    if rem_need[i] <= available:
        # the process is executed
        # freeing up already allocated memory by p[i]
        for j in range(3):
            available[j] = available[j] + allocation[i][j]
        safe.append(i)
    else:
        rem_process.append(i)
for i in range(n):
    if i in rem_process:
        # process not executed yet
        if rem_need[i] <= available:
            # the process is executed
            # freeing up already allocated memory by p[i]
            for j in range(3):
                available[j] = available[j] + allocation[i][j]
            safe.append(i)
            rem_process.remove(i)
    else:
        continue
for i in range(n):
    if i in rem_process:
        # process not executed yet
        if rem_need[i] <= available:
            # the process is executed
            # freeing up already allocated memory by p[i]
            for j in range(3):
                available[j] = available[j] + allocation[i][j]
            safe.append(i)
            rem_process.remove(i)
    else:
        continue
if len(safe) != n:
    print('Safe sequence cannot be obtained.')
else:
    print('Safe sequence : ', safe)
