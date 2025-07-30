#This file should deal entirely with creating the json/dictionary so that other files can use it 
#TODO:
#   [x] - Make a export function that converts dic to valid json obj

import re, jsonR

class processing:
    def __init__(self, file):
        self.file = file
        with open(self.file,"r") as f:
            self.__wholeshit = [line.strip() for line in f.readlines()]
        self.__i = 0    #the general index of where the code is in the file

    def theLoop(self):
        johnson = {}
        while self.__i < len(self.__wholeshit):
            currLine = self.__wholeshit[self.__i]
            search = re.search("sunday|monday|tuesday|wednesday|thursday|friday|saturday",currLine.lower())
            if search != None:
                date, dic = self.__grouping()
                johnson[date] = dic

            else:
                self.__i += 1

        self.__dic = johnson


    def __grouping(self):
        group = []
        line = self.__wholeshit[self.__i]
        while line != "":
            group.append(line)
            self.__i += 1
            line = self.__wholeshit[self.__i]
        return self.__disection(group)


    def __disection(self,list):
        outputDic = {}
        date = list[0]
        list.pop(0)
        for line in list:
            movement = re.search(".+(?= [-])",line) #finds all the movements
            reps = re.findall(r"\d+(?=[x])",line) #I had to use "raw strings" to make sure that the regular expression worked and didn"t put and ugly little message in the terminal
            weight = re.findall(r"[0-9.]{1,4}\w{2,3}(?=;)",line) # I could improve this regex by gathering both reps and weight in one regex and seperating them by getting different caputure groups
            numbers = []
            for x in range(len(reps)):
                rw = []
                rw.append(reps[x])
                rw.append(weight[x])
                numbers.append(rw)
            outputDic[movement.group()]=numbers
        return date,outputDic
    
    def getDic(self):
        return self.__dic

    def exportjson(self):
        return jsonR.dict2json(self.__dic)


if __name__ == "__main__":
    pull = processing("./data/pull.txt")
    pull.theLoop()
