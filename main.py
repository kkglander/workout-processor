from dataModeOn import processing

pull = processing("./data/dummydata.txt")
pull.theLoop()
print(pull.exportjson())
