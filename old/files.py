import re,os,evan
os.system("cls" if os.name == "nt" else "clear")#a system clear that works for both mac and Windows (should prolly know this because it might help in the future)

#notes/checklist:
#[ ] - refactor everything everything
#
#
#How to think about the library
#library {
#   date : {
#       movement : [[reps,weight] , [reps,weight]]
#       movement : [[reps,weight] , [reps,weight]]
#}      
#   date : { movement : [[reps,weight] , [reps,weight]] , movement : [[reps,weight] , [reps,weight]] }
#}

class reader():
    def __init__(self,file):
        """
        On innitializing the file, it takes all of the data from a file and organizes it into library. 
        so that I can focus in making all of the other functions reading and interpreting the data
        """
        self.file = file
        f = open(self.file,"r")
        for line in f:
            pass
            last_line = line
        f.close
        if last_line != ".":
            appendation = open(self.file,"a")
            appendation.write("\n.")
            appendation.close
            print("FIXED!")
        f = open(self.file,"r")
        f.seek(0)
        line = f.readline()
        library = {} #The massive library that holds all the data
        info = ""
        while line != ".": #period is the document ender to prevent an infinite loop
            line = f.readline()
            search = re.search("^\n",line)
            if search == None: #if the line does not start with a "\n" then go to the next search
                subSearch = re.search("sunday|monday|tuesday|wednesday|thursday|friday|saturday",line.lower())
                subSearch2 = re.search(". - .+;$",line) #regex explained -> ((anycharacter) - (anycharacter)(One or more occurences)  (endsWith)(;))
                if subSearch != None:
                    date = line.rstrip() #They key for the dictionary
                    library[date] = {} #hopefully adds a list to the dictionary
                elif subSearch2 != None:
                    info = line.rstrip()
                    movement = re.search(".+(?= [-])",info) #finds all the movements
                    reps = re.findall(r"\d+(?=[x])",info) #I had to use "raw strings" to make sure that the regular expression worked and didn"t put and ugly little message in the terminal
                    weight = re.findall(r"\d{1,3}\w{2,3}(?=;)",info) # I could improve this regex by gathering both reps and weight in one regex and seperating them by getting different caputure groups
                    library[date].update({movement.group():[]}) # I need this to sperarate the movement from the weight/rep recording
                    rw = []
                    for x in range(len(reps)):
                        rw.append(reps[x])
                        rw.append(weight[x])
                        library[date][movement.group()].append(rw) # I need this to sperarate the movement from the weight/rep recording
                        rw=[]
        f.close
        self.library = library
    
    def on_day(self,day):
        for key in self.library:
            if day.lower() in key.lower():
                print("{:} : {:}\n\n".format(key,self.library[key]))

    def print_lib(self):
        for key in self.library:
            print(key,":")
            for keebler in self.library[key]:
                print("\t",keebler,":")
                for array in self.library[key][keebler]:
                    print(f"\t\t {array[0]}x{array[1]}")

    def rawLib(self):
        print(self.library)

    def one_exercise(self,exercise): #Every instance of an exercise printed

        print("{:} over time:\n".format(exercise))

        for key in self.library: #For the first ditionary layer meaning {date: {}, date: {}}
            for keebler in self.library[key]:# for the second dictionary layer meaning {date: ->{movement: [reps,weight]}<- }
                if keebler.lower() == exercise.lower(): #compares the exercise names

                    print("{:}".format(key))

                    for array in self.library[key][keebler]:
                        print(f"\t-{array[0]}x{array[1]}")
