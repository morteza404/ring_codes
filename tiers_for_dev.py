from swift.common.ring import utils
from swift.common.ring import RingBuilder

devs = [{'region':'r1', 'zone':'z1', 'ip':'192.168.1.1', 'port':6200, 'device':'sda', 'weight':100.0, 'id':0}, 
        {'region':'r1', 'zone':'z2', 'ip':'192.168.1.2', 'port':6200, 'device':'sdb', 'weight':200.0, 'id':1},
        {'region':'r1', 'zone':'z2', 'ip':'192.168.1.3', 'port':6200, 'device':'sdc', 'weight':300.0, 'id':2},
        {'region':'r1', 'zone':'z3', 'ip':'192.168.1.4', 'port':6200, 'device':'sdd', 'weight':500.0, 'id':3},
        {'region':'r1', 'zone':'z3', 'ip':'192.168.1.5', 'port':6200, 'device':'sde', 'weight':100.0, 'id':4}
        ]

ring = RingBuilder(10,3.0,24)

for dev in devs:
    ring.add_dev(dev)

for dev in ring._iter_devs():
    dev['tiers'] = utils.tiers_for_dev(dev)

print(devs)