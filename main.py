def MainFunc():
    x = 1 + 2
    a = 1
    b = 2
    for i in range(5):
        if i == a or i == b:
            print("YES")
        else:
            print("NO")
    return x


if __name__ == "__main__":
    MainFunc()
