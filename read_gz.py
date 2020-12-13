import os
from swift.common.ring import RingData

path = os.getenv(key="HOME") + "/Desktop/object.ring.gz"

data = RingData.load(path).to_dict()

print(data)
