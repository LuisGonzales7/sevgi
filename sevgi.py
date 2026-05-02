import time
import random

colors = [
    "\033[91m",
    "\033[92m",
    "\033[93m",
    "\033[94m",
    "\033[95m",
    "\033[96m",
    "\033[97m"
]

reset = "\033[0m"

mesaj = "Eylülü çok seviyorum"

numara = 412300

while True:
    renk = random.choice(colors)
    print(f"{renk}{numara} - {mesaj}{reset}")
    numara += 1
    time.sleep(0.05)