import random, hashlib

am="18184"

tmp=hashlib.sha256(am.encode()).hexdigest()

seed=int(tmp,16)

random.seed(seed)

lst=list(range(1,14))

random.shuffle(lst)

print(lst[:4])

input("press any key to continue...")
