def sort_ascii(str):
    return ''.join(sorted(str))

if __name__ == "__main__":
    s = input().strip()
    print(sort_ascii(s))