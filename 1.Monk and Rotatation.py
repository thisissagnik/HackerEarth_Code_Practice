def Rotate_Right(N,K,arr):
    M=K%N
    temp = arr[N-M:] + arr [:N-M]

    return " ".join(str(x) for x in temp)


def main():
    T= input()

    for i in range(int(T)) :
        N,K= map(int,input().split())

        arr= list(map(int,input().split())) [:N]

        print(Rotate_Right(N,K,arr))
        #Rotate_Right(N,K,arr)

main()


