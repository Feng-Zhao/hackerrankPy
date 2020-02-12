
if __name__ == '__main__':
    n = int(input())
    dic = {}
    for i in range(0, n):
        key, value = input().rstrip().split()
        dic[key] = value
    try:
        while True:
            query = input()
            if query in dic:
                print("{}={}".format(query, dic[query]))
            else:
                print("Not found")
    except EOFError:
        pass
