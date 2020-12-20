from swift.common.ring import RingBuilder
from collections import defaultdict

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(10, 2.25, 24)

assign_parts = defaultdict(list)

ring._adjust_replica2part2dev_size(assign_parts)

replica = len(ring._replica2part2dev)

partition = [len(ring._replica2part2dev[i]) for i in range(replica)]

print(replica)

print(partition)