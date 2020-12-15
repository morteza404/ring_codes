from swift.common.ring import RingBuilder
from swift.common.ring import utils
from collections import defaultdict

devs = []

infos = [{"region":"r1", "zone":"z1", "ip":"s1", "weight":100.0, "id":"d0"}, 
         {"region":"r1", "zone":"z1", "ip":"s2", "weight":200.0, "id":"d1"},
         {"region":"r1", "zone":"z1", "ip":"s2", "weight":50.0, "id":"d2"},
         {"region":"r1", "zone":"z2", "ip":"s3", "weight":500.0, "id":"d3"}]

for info in infos:
    devs.append(info)

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(10, 3.0, 24)

ring.devs = devs

num_devices = defaultdict(int)

for d in ring._iter_devs():
    if d['weight'] <= 0:
        continue
    for t in (d.get('tiers') or utils.tiers_for_dev(d)):
        num_devices[t] += 1
    num_devices[()] += 1

print(num_devices)
