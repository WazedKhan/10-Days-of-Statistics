def mean(arr):
    print(sum(arr)/10)


def median(arr):
    if len(arr) % 2 != 0:
        print(round(len(arr)/2)+1)
    else:
        mid = arr[(int(len(arr)/2)-1)] + arr[(int(len(arr)/2))]
        print(mid/2)


arr = sorted(list(map(
    int, '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'.split(' '))))


mean(arr)
median(arr)
