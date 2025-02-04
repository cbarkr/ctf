ace = "aaa"
jack = "aaa"
queen = "aaa"
king = "aaa"

ace0 = chr(ord(ace[0]) + 4)
ace1 = chr(ord(ace[0]) + 19)
ace2 = chr(ord(ace[0]) + 18)

jack0 = chr(ord(jack[0]) + 7)
jack1 = chr(ord(jack[0]) + 0)
jack2 = chr(ord(jack[0]) + 1)

queen0 = chr(ord(queen[0]) + 0)
queen1 = chr(ord(queen[0]) + 11)
queen2 = chr(ord(queen[0]) + 15)

king0 = chr(ord(king[0]) + 14)
king1 = chr(ord(king[0]) + 20)
king2 = chr(ord(king[0]) + 15)

ace = ace0 + ace1 + ace2
jack = jack0 + jack1 + jack2
queen = queen0 + queen1 + queen2
king = king0 + king1 + king2

res = queen + jack + ace + king
print(res)
