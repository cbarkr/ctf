witches = ["weatherwax", "ogg", "garlick", "nitt", "aching", "dismass"]
second = 0
third = 1 + second
fourth = (third + third) - second
fifth = 3 + fourth

res = witches[fifth] + "." + witches[third] + "." + witches[second] + "." + witches[(fifth + second) - third] + "." + witches[3] + "." + witches[fourth]
print(res)
