def cetakarr(arr, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end="  ")
        print()
    print()

stop = False
while(stop == False):
    print("\n-----PROGRAM ARRAY SEGITIGA-----\n")
    n = int(input(f'Masukan Ukuran Array (Integer): '))
    a = [[0 for i in range(n)] for i in range(n)]
    b = [[0 for i in range(n-1)] for i in range(n-1)]
    c = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j] = input(f'- Masukkan Elemen A[{i+1},{j+1}]: ')
                c[i][j] = a[i][j]

    print("\nHasil Array A (Upper Tringular):")
    cetakarr(a, n)

    for i in range(n-1):
        for j in range(n-1):
            if j <= i:
                b[i][j] = input((f'- Masukkan Elemen B[{i+1},{j+1}]: '))
                c[i+1][j] = b[i][j]

    print("\nHasil Array B (Lower Tringular):")
    cetakarr(b, n-1)

    input("Tekan Enter Untuk Melihat Hasil!\n")
    print("----------- H A S I L -----------")

    print("\nHasil Array A (Upper Tringular):")
    cetakarr(a, n)

    print("Hasil Array B (Lower Tringular):")
    cetakarr(b, n-1)

    print("Hasil Akhir:")
    cetakarr(c, n)

    ask = True
    while(ask == True):
        repeat = input("Apakah Anda Ingin Mengulang? (Y/N): ").lower()
        if repeat == "n":
            stop = True
            ask = False
        elif repeat == "y":
            stop = False
            ask = False
        else:
            ask = True

print("\nTerima Kasih!\n")
