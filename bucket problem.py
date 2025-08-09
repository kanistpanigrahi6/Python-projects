n = int(input())
for i in range(n):
    w, x, y, z = map(int, input().split())
    initial = w + y * z
    if initial > x:
        print("Overflow")
    elif initial < x:
        print("Unflled")
    else:
        print("Filled")

