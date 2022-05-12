import random
import string
ad = 5
a = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(ad))
print(a)