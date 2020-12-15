replica, partition = (3,10)

r2p2d = [[1 for j in range(partition)] for i in range(replica)]

print("r2p2d initialized")
print(r2p2d)

r2p2d[0][8] = 0
r2p2d[1][8] = 4
r2p2d[2][8] = 1

r2p2d[0][3] = 2
r2p2d[1][3] = 1
r2p2d[2][3] = 3

r2p2d[0][0] = 3
r2p2d[1][0] = 2
r2p2d[2][0] = 0

r2p2d[0][5] = 4
r2p2d[1][5] = 1
r2p2d[2][5] = 2

print("r2p2d")
print(r2p2d)

N = 5

devs = [i for i in range(N)]

print("devs")
print(devs)

devices = [devs[part2dev_id[5]] for part2dev_id in r2p2d]

print("devices")
print(devices)
