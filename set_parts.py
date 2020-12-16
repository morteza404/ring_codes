from swift.common.ring import RingBuilder
from collections import defaultdict
import math
import itertools

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

replica_plan = ring._build_replica_plan()

parts_by_tier = defaultdict(int)

sub_tiers = sorted(tier2children[('r1', 'z1', 's2')])

# print(sorted(sub_tiers, key=lambda t: replica_plan[t]['target']))


sub_tier_gen = itertools.cycle(sorted(sub_tiers, key=lambda t: replica_plan[t]['target']))

z = next(sub_tier_gen)

y = next(sub_tier_gen)

print(z)

print(y)

# sub_tier_gen = itertools.cycle()

# def place_parts(tier, parts):
#     parts_by_tier[tier] = parts
#     sub_tiers = sorted(tier2children[tier])
#     if not sub_tiers:
#         return
#     to_place = defaultdict(int)
#     for t in sub_tiers:
#         to_place[t] = min(parts, int(math.floor(
#             replica_plan[t]['target'] * ring.parts)))
#         parts -= to_place[t]

#     sub_tier_gen = itertools.cycle(sorted(
#         sub_tiers, key=lambda t: replica_plan[t]['target']))
#     while parts > 0:
#         t = next(sub_tier_gen)
#         to_place[t] += 1
#         parts -= 1

#     for t, p in to_place.items():
#         place_parts(t, p)

# total_parts = int(ring.replicas * ring.parts)

# place_parts((), total_parts)
