from swift.common.ring import RingBuilder

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(2, 3.0, 24)

devs = [{"id":0, "device":"sda"},{"id":1, "device":"sdb"}, {"id":2, "device":"sdc"},{"id":3, "device":"sdd"}]

ring.devs = devs

ring._replica2part2dev = [[0,1,2,3],[3,2,1,0],[2,0,3,1]]

print(ring._replicas_for_part(2))