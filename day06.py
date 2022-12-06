def marker(s, size):
    for i, s in enumerate(a):
        if (len(set(a[i:i+size])) == size):
            return i+size

a = input()
print(marker(a, 4), marker(a, 14))