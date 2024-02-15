x = int(input())

for _ in range(x):
    n = int(input())
    s = input()

    ans = 0
    runningSum = 0
    mymap = {0: 1}

    for i in range(n):
        runningSum += int(s[i])
        ans += mymap.get(runningSum - (i + 1), 0)
        mymap[runningSum - (i + 1)] = mymap.get(runningSum - (i + 1), 0) + 1

    print(ans)