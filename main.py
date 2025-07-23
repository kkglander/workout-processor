from dataModeOn import processing
import pprint

pull = processing("./data/pull.txt")
pull.theLoop()
result = pull.getDic()
pprint.pprint(result)



