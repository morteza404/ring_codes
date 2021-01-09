from swift.common.ring import RingBuilder

devs = []

infos = [{'weight': 100.0, 'ip': 's1', 'meta': '', 'device': 'sda', 'port': 6200, 'tiers': (('r1',), ('r1', 'z1'), ('r1', 'z1', 's1'), ('r1', 'z1', 's1', 0)), 'zone': 'z1', 'region': 'r1', 'id': 0, 'parts': 0, 'parts_wanted': 682}, 
         {'weight': 200.0, 'ip': 's2', 'meta': '', 'device': 'sdb', 'port': 6200, 'tiers': (('r1',), ('r1', 'z1'), ('r1', 'z1', 's2'), ('r1', 'z1', 's2', 1)), 'zone': 'z1', 'region': 'r1', 'id': 1, 'parts': 0, 'parts_wanted': 1024}, 
         {'weight': 300.0, 'ip': 's2', 'meta': '', 'device': 'sdc', 'port': 6200, 'tiers': (('r1',), ('r1', 'z1'), ('r1', 'z1', 's2'), ('r1', 'z1', 's2', 2)), 'zone': 'z1', 'region': 'r1', 'id': 2, 'parts': 0, 'parts_wanted': 341}, 
         {'weight': 500.0, 'ip': 's3', 'meta': '', 'device': 'sdd', 'port': 6200, 'tiers': (('r1',), ('r1', 'z2'), ('r1', 'z2', 's3'), ('r1', 'z2', 's3', 3)), 'zone': 'z2', 'region': 'r1', 'id': 3, 'parts': 0, 'parts_wanted': 1025}]

for info in infos:
    devs.append(info)

ring = RingBuilder(2, 3.0, 24)

ring.devs = devs

ring._replica2part2dev = [[0,1,2,3],[3,2,1,0],[2,0,3,1]]

replica_plan = ring._build_replica_plan()

assign_parts_list = [(0, [0]), (1, [0, 2]), (2, [1]), (3, [1, 2])]

ring._reassign_parts(assign_parts_list, replica_plan)

print(ring.devs)