from swift.common.ring import RingBuilder

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

tier2children = ring._build_tier2children()

sub_tiers = sorted(tier2children[()])

print(sub_tiers)
