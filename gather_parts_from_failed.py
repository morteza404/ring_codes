from swift.common.ring import RingBuilder
from collections import defaultdict

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(2, 3.0, 24)

devs = [{"id":0, "parts":-1},{"id":1, "parts":-1}, {"id":2, "parts":-1},{"id":3, "parts":-1}]

ring.devs = devs

ring._remove_devs = [{"id":0, "parts":-1},{"id":1, "parts":-1}]

ring._replica2part2dev = [[0,1,2,3],[3,2,1,0],[2,0,3,1]]

ring._part_moved_bitmap = bytearray(max(2 ** (ring.part_power - 3), 1))

assign_parts = defaultdict(list)

removed_devs = ring._gather_parts_from_failed_devices(assign_parts)

print(removed_devs)

print(devs)