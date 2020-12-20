from swift.common.ring import RingBuilder
from collections import defaultdict

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(2, 3.0, 24)

devs = [{'region':'r1', 'zone':'z1', 'ip':'s1', 'port':6200, 'device':'sda', 'weight':100.0, 'id':0, "parts":0, "parts_wanted":None}, 
        {'region':'r1', 'zone':'z1', 'ip':'s2', 'port':6200, 'device':'sdb', 'weight':200.0, 'id':1, "parts":0, "parts_wanted":None},
        {'region':'r1', 'zone':'z1', 'ip':'s2', 'port':6200, 'device':'sdc', 'weight':300.0, 'id':2, "parts":0, "parts_wanted":None},
        {'region':'r1', 'zone':'z2', 'ip':'s3', 'port':6200, 'device':'sdd', 'weight':500.0, 'id':3, "parts":0, "parts_wanted":None}        
       ]

ring.devs = devs

# ring._replica2part2dev = [[0,1,2,3],[3,2,1,0],[2,0,3,1]]

assign_parts = defaultdict(list)

replica_plan = ring._build_replica_plan()

ring._gather_parts_for_dispersion(assign_parts,replica_plan)

print(devs)