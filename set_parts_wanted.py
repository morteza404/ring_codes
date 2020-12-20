from swift.common.ring import RingBuilder

devs = []

infos = [{"region":"r1", "zone":"z1", "ip":"s1", "weight":100.0, "id":"d0", "parts":0, "parts_wanted":None}, 
         {"region":"r1", "zone":"z1", "ip":"s2", "weight":200.0, "id":"d1", "parts":0, "parts_wanted":None},
         {"region":"r1", "zone":"z1", "ip":"s2", "weight":50.0, "id":"d2", "parts":0, "parts_wanted":None},
         {"region":"r1", "zone":"z2", "ip":"s3", "weight":500.0, "id":"d3", "parts":0, "parts_wanted":None}]

for info in infos:
    devs.append(info)

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(2, 3.0, 24)

ring.devs = devs

replica_plan = ring._build_replica_plan()

ring._set_parts_wanted(replica_plan)

print(devs)