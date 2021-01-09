from swift.common.ring import RingBuilder

ring = RingBuilder(2,3.0,24)

devs = [{'region':'r1', 'zone':'z1', 'ip':'s1', 'port':6200, 'device':'sda', 'weight':100.0, 'id':0}, 
        {'region':'r1', 'zone':'z1', 'ip':'s2', 'port':6200, 'device':'sdb', 'weight':200.0, 'id':1},
        {'region':'r1', 'zone':'z1', 'ip':'s2', 'port':6200, 'device':'sdc', 'weight':50.0, 'id':2},
        {'region':'r1', 'zone':'z2', 'ip':'s3', 'port':6200, 'device':'sdd', 'weight':500.0, 'id':3}        
       ]

for dev in devs:
    ring.add_dev(dev)

ring._replica2part2dev = [[0,1,2,3],[3,2,1,0],[2,0,3,1]]

changed_parts = ring._build_dispersion_graph()

# print(changed_parts)

print(ring._dispersion_graph)

# print(ring.devs)