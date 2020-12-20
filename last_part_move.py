from swift.common.ring import RingBuilder 

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(10, 3.0, 24)

ring._update_last_part_moves()

print(ring._last_part_moves)

print(ring._last_part_moves_epoch)