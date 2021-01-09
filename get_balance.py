from swift.common.ring import RingBuilder

devs = []

infos = [{"region":"r1", "zone":"z1", "ip":"s1", "weight":100.0, "id":"d0", "parts":1}, 
         {"region":"r1", "zone":"z1", "ip":"s2", "weight":200.0, "id":"d1", "parts":0},
         {"region":"r1", "zone":"z1", "ip":"s2", "weight":50.0, "id":"d2", "parts":-1},
         {"region":"r1", "zone":"z2", "ip":"s3", "weight":500.0, "id":"d3", "parts":0}]

for info in infos:
    devs.append(info)

ring = RingBuilder(10, 3.0, 24)

ring.devs = devs

balance = ring.get_balance()

print(balance)
