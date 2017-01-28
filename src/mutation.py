#mutation.py
def checkMutation():
    mutationtype = 0
    chance = random.uniform(0,1000)
    if 0 > chance > 935:
        mutationtype = 0
    if 935 > chance > 985:
        mutationtype = 1
    if 985 > chance > 995:
        mutationtype = 2
    else:
        mutationtype = 3
