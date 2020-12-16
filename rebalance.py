from swift.common.ring import RingBuilder

devs = []

infos = [{"region":"r1", "zone":"z1", "ip":"s1", "weight":100.0, "id":0, "parts":1024}, 
         {"region":"r1", "zone":"z1", "ip":"s2", "weight":200.0, "id":1, "parts":1024},
         {"region":"r1", "zone":"z1", "ip":"s2", "weight":50.0, "id":2, "parts":1024},
         {"region":"r1", "zone":"z2", "ip":"s3", "weight":500.0, "id":3, "parts":1024}]

for info in infos:
    devs.append(info)

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(10, 3.0, 24)

ring.devs = devs

print(ring.rebalance())