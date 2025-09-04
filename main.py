from dataModeOn import processing

pull = processing("./data/pull.txt")
pull.theLoop()
output = pull.exportjson()
with open("data.json", "w") as f:
    f.write(output)
