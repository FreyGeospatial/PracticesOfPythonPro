from time import time
print(time())

from datetime import time
print(time())

# easier to just explicity import...
import time
import datetime

now = time.time()
midnight = datetime.time()

# you can also alias imports to avoid namespace collisions...
from mycoollibrary import datetime as cooldatetime
from datetime import datetime

cooldatetime()
datetime(2020, 1, 1)