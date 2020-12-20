from swift.common.ring import RingBuilder
from swift.common.ring import utils
from collections import defaultdict

# ring parameters : p R m (partition power, replicas, min_part_hours)
ring = RingBuilder(2, 3.0, 24)

devs = [{'region':'r1', 'zone':'z1', 'ip':'192.168.1.1', 'port':6200, 'device':'sda', 'weight':100.0, 'id':0}, 
        {'region':'r1', 'zone':'z2', 'ip':'192.168.1.2', 'port':6200, 'device':'sdb', 'weight':200.0, 'id':1},
        {'region':'r1', 'zone':'z2', 'ip':'192.168.1.3', 'port':6200, 'device':'sdc', 'weight':300.0, 'id':2},
        {'region':'r1', 'zone':'z3', 'ip':'192.168.1.4', 'port':6200, 'device':'sdd', 'weight':500.0, 'id':3},
        {'region':'r1', 'zone':'z3', 'ip':'192.168.1.5', 'port':6200, 'device':'sde', 'weight':100.0, 'id':4}
        ]

ring.devs = devs

ring._replica2part2dev = [[0,1,2,3],[3,2,1,0],[2,0,3,1]]

print(ring._devs_for_part(1))

