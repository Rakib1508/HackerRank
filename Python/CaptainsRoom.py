family = int(input())
room_numbers = list(map(int, input().split()))
rooms = {}
for i in room_numbers:
    if i in rooms:
        rooms[i] += 1
    else:
        rooms[i] = 1

for k, v in rooms.items():
    if v == 1:
        print(k)
