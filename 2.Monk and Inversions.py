def cnt_inversion(n, arr):
    count = 0
    index_com = []
    for i in range(n):
        for j in range(n):
            index_com.append((i, j))

    for x, y in index_com:
        for p, q in index_com:
            if x <= p and y <= q:
                if arr[x][y] > arr[p][q]:
                    count += 1

    return count


# Driver Program
def main():
    t = input()

    for _ in range(int(t)):
        n = int(input())

        arr = []

        for _ in range(n):
            arr.append(list(map(int, input().strip().split())))

        print(cnt_inversion(n, arr))


main()
