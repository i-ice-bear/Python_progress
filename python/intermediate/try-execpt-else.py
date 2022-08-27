def trailFunction(*args):
    print(type(args))


try:
    trailFunction("state")

except:
    trailFunction("state-2")
    print("working on except")
else:
    trailFunction("state-3")

    print("Working on else")
finally:
    trailFunction("state-4")

    print("Working on finally")
