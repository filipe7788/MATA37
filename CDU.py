u = input()
u = int(u)
hundred = int(u / 100)
rest = u % 100
decimal = int(rest / 10)
rest = rest % 10
unit = int(rest)
total = (unit.__str__() + " " + decimal.__str__() + " " + hundred.__str__())
print(total)
