def printboard():
    print("Нарисуем доску!")
    l = int(input("Введите длину: "))
    w = int(input("Введите ширину: "))
    lgth = l+1
    h = w//2-3
    p = l//2-1
    p1 = p-1
    print("#"*lgth)
    for i in range(h):
        print("!"+" "*p +"." + " "*p +"!")
    for i in range(5):
        print("!["+" "*p1 +"." + " "*p1 +"]!")
    for i in range(h):
        print("!"+" "*p +"." + " "*p +"!")
    print("#"*lgth)
printboard()