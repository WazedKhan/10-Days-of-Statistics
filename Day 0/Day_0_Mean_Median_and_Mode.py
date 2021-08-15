def mean(arr, N):
    print(sum(arr)/N)


def median(arr, N):
    if N % 2 != 0:
        print(round(N/2)+1)
    else:
        mid = arr[(int(N/2)-1)] + arr[(int(N/2))]
        print(mid/2)


def mode(arr):
    output = {}
    fre = []
    for item in arr:
        if item not in output:
            output[item] = 0
        output[item] += 1
    for _, count in output.items():
        fre.append(count)
    if max(fre) == min(fre):
        print(arr[0])
    else:
        print(max(fre))


N = 10
arr = sorted(list(map(
    int, '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'.split(' '))))


mean(arr, N)
median(arr, N)
# there is a problem its only checks max and min number is repeted or not but it does not check between max and min
mode(arr)
