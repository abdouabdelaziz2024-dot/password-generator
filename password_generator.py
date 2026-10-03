import random
import time
import string

x = random.randint(1, 1000000000000000000000)

z = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(16))

y = time.strftime("%Y%m%d_%H%M%S")

print("Your Password is:", z + y)