def podziel(napis):
    end = []
    start = 0
    for i in range(len(napis) - 1):
        if napis[i] == " ":
            start = i + 1
        elif napis[i] != " " and napis[i + 1] == " ":
            end.append(napis[start:i + 1])
    return end


sa = " Ala ma kota "
print(podziel(sa))
