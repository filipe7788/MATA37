time = input()

numberOfHours = time // 3600
numberOfMinutes = (time % 3600) // 60
numberOfSeconds = (time % 3600) % 60

print(numberOfHours.__str__()+"h "+numberOfMinutes.__str__()+"m "+numberOfSeconds.__str__()+"s")