from swift.common.ring import RingBuilder

devs = [{'region':'r1', 'zone':'z1', 'ip':'s1', 'port':6200, 'device':'sda', 'weight':100.0, 'id':0, "parts":0, "parts_wanted":None}, 
        {'region':'r1', 'zone':'z1', 'ip':'s2', 'port':6200, 'device':'sdb', 'weight':200.0, 'id':1, "parts":0, "parts_wanted":None},
        {'region':'r1', 'zone':'z1', 'ip':'s2', 'port':6200, 'device':'sdc', 'weight':300.0, 'id':2, "parts":0, "parts_wanted":None},
        {'region':'r1', 'zone':'z2', 'ip':'s3', 'port':6200, 'device':'sdd', 'weight':500.0, 'id':3, "parts":0, "parts_wanted":None}        
       ]

ring = RingBuilder(10,3.0,24)

ring.devs = devs

for dev in devs:
    dev['sort_key'] = ring._sort_key_for(dev)

print(devs[0])