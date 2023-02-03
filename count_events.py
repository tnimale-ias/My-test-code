str1 = open("data/events.txt").read()

print("Events: "+str(str1.count("\n")*10))
print("Impression: "+str(str1.count("impression")*10))
print("Unload: "+str(str1.count("unload")*10))
print("Load: "+str((str1.count("\n")-str1.count("impression")-str1.count("unload"))*10))

