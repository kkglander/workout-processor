import re
import tempfile, subprocess

#A lot of this code is similar to 'dataModeOn', i could make it into a base class
#i'll decide that whenever i refactor
#still need to make the movement validation part of this

class Validate:
    def __init__(self, file) -> None:
        self.__filename = file
        self.__movementList = []
        self.__data = []
        self.__index = 0
        self.__deviationsList = []

        with open(file, 'r') as f:
            self.__data = [line.strip() for line in f.readlines()]


    def theLoop(self) -> None:
        while self.__index < len(self.__data):
            currLine = self.__data[self.__index]
            search = re.search("sunday|monday|tuesday|wednesday|thursday|friday|saturday",currLine.lower())
            if search != None:
                self.dayPatternValidation(currLine)
                self.__index += 1
                self.movementPatternValidation()             
            else:
                self.__index += 1
        self.corrections()


    def dayPatternValidation(self, currLine) -> None:
        search = re.search(r"(sunday|monday|tuesday|wednesday|thursday|friday|saturday) (\d{2}/\d{2}/\d{4})", currLine.lower())
        if search == None:
            #it doesn't match so add it to the list
            self.__deviationsList.append(self.__index)
        


    def movementPatternValidation(self) -> None:
        currLine = self.__data[self.__index]
        while currLine != "":
            search = re.search(r".+(?= [-]) -( \d+(?=[x]))x(\d+(lbs|kg)(?=;))(; *\d+x\d+(lbs|kg))*;", currLine.lower())
            if search == None:
                #its doesn't match the pattern so we add it to the list
                self.__deviationsList.append(self.__index)
            self.__index += 1
            currLine = self.__data[self.__index]


    def corrections(self) -> None:
        passedtext = """This is the corrections file, the following lines all deviate from the pattern intended for the code to function,
Please correct them, then save and exit this file
Intended Date Pattern: WeekDay MM/DD/YYYY
Intended Movement Pattern: MovementName - RepsxWeight; RepsxWeight;...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n
"""
        for lineNum in self.__deviationsList:
            addition = self.__data[lineNum]
            passedtext += f"{addition}\n"

        with tempfile.NamedTemporaryFile(suffix=".tmp", mode="w+") as temp:
            temp.write(passedtext)
            temp.flush()
            temp_name = temp.name
        
            subprocess.call(["nvim", temp_name])
    
            with open(temp_name, "r") as f:
                file = f.readlines()
                for i in range(7):
                    file.pop(0)

        for i in range(len(self.__deviationsList)):
            lineNum = self.__deviationsList[i]
            self.__data[lineNum] = file[i].strip()

        self.TESTexportCorrections()


    def TESTexportCorrections(self) -> None:
        exportData = []
        for line in self.__data:
            exportData.append(line + "\n")

        with open(f"./data/testlegs.txt", "w") as f:
            f.writelines(exportData)


    def exportCorrections(self) -> None:
        with open(self.__filename, "w") as f:
            f.writelines(self.__data)


if __name__ == "__main__":
    test = Validate("./data/legs.txt")
    test.theLoop()

