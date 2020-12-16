from swift.common.ring import RingBuilder

ring = "/home/shahbazi/Desktop/rings/object-real.builder"

print(RingBuilder.load(ring).to_dict())