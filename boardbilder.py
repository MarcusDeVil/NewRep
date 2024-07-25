def printboard():
    print("Нарисуем доску!")
    l = int(input("Введите длину: "))
    w = int(input("Введите ширину: "))
    outline = int(input("Введите отступ: "))
    lgth = l+1
    h = w//2-5
    p = l//2-1
    p1 = p-1
    p2 = int(p1)-outline
    print("#"*lgth)
    for i in range(h):
        print("!"+" "*p +"." + " "*p +"!")
    for i in range(5):
        print("!"+" "*outline+ "["+" "*p2 +"." + " "*p2 +"]"+" "*outline+ "!")
    for i in range(h):
        print("!"+" "*p +"." + " "*p +"!")
    print("#"*lgth)
printboard()