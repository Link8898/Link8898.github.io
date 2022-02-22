import random

name = "Atlas"
verb = "Running"
verb = verb.lower() # Convert to lowercase
adjective = "happy"
adjective = adjective.lower() # Convert to lowercase
location = "Aperture Laboratories"

starterInt = random.randrange(0,3)
middle1Int = random.randrange(0,3)
middle2Int = random.randrange(0,3)
middle3Int = random.randrange(0,3)
endInt = random.randrange(0,3)

starters = ("Oh my beloved " + name, "Looking upon you, " + name, "Oh how I adore you, " + name)
middles1 = ("Seeing you " + verb, "Oh how I adore you when you're " + verb, "Such a sight to see you " + verb)
middles2 = ("out at " + location, "passed " + location, "nearby " + location)
middles3 = ("I wish to be as " + adjective + " as you.", "I yearn to see you " + adjective + " once again.", "I wish for you to be as " + adjective + " as can be.")
ends = ("Until we meet again, I shall wait for your return.", "Oh how I long to see you once again.", "I hope we meet again some day.")

starter = starters[starterInt]
middle1 = middles1[middle1Int]
middle2 = middles2[middle2Int]
middle3 = middles3[middle3Int]
end = ends[endInt]

finalPoem = starter + ", " + middle1 + " " + middle2 + ", " + middle3 + " " + end
print(finalPoem)