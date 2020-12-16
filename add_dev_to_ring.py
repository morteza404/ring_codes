from swift.common.ring import RingBuilder

devs = [{"device":"sda1", "region":"r1", "zone":"z1", "ip":"192.168.1.10", "port":6200, "weight":100.0, "id":0},
        {"device":"sda2", "region":"r1", "zone":"z1", "ip":"192.168.1.10", "port":6200, "weight":200.0, "id":1}]

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(10, 3.0, 24)

#print (ring)
#print (ring.get_ring())
#print (ring.get_ring().to_dict())

#print ("----")

for dev in devs:
    ring.add_dev(dev)

print(ring.get_ring().to_dict())
