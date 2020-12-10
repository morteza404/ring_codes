import pickle

with open("/home/shahbazi/Desktop/rings/object.builder","rb") as pkl_file:
    data = pickle.load(pkl_file)

# del data["_last_part_moves"], data["_replica2part2dev"], data["_dispersion_graph"], data["devs"], data["_remove_devs"]

print(data)
