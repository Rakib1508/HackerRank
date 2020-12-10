from datetime import datetime as std

clone = '%a %d %b %Y %H:%M:%S %z'

cycle = int(input())

for i in range(cycle):
    initial_time = std.strptime(input(), clone)
    later_time = std.strptime(input(), clone)
    diff = later_time - initial_time
    seconds = int(abs(diff.total_seconds()))
    print(seconds)
