from swift.common.ring import utils
from swift.common.ring import RingBuilder

devs = [{'region':'r1', 'zone':'z1', 'ip':'s1', 'port':6200, 'device':'sda', 'weight':100.0, 'id':0, 'parts_wanted':682}, 
        {'region':'r1', 'zone':'z1', 'ip':'s2', 'port':6200, 'device':'sdb', 'weight':200.0, 'id':1, 'parts_wanted':1024},
        {'region':'r1', 'zone':'z1', 'ip':'s2', 'port':6200, 'device':'sdc', 'weight':300.0, 'id':2, 'parts_wanted':341},
        {'region':'r1', 'zone':'z2', 'ip':'s3', 'port':6200, 'device':'sdd', 'weight':500.0, 'id':3, 'parts_wanted':1025}        
        ]

ring = RingBuilder(2,3.0,24)

for dev in devs:
    ring.add_dev(dev)

for dev in ring._iter_devs():
    dev['tiers'] = utils.tiers_for_dev(dev)

print(devs)

# for tier in dev['tiers']:
#     print(tier)