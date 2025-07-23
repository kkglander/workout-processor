#I need this code to look through my file, get the names for all the movements and check them against a list in a file
#If it doesn't match one of the names in the list, print it,  ask the user to change it to one that matches or to make a new movement name
# How should I exceute:
#   iterate through the whole document, find the lines where there are mismatches, save the line into a list or something and go back to it later make the change
import re,os
os.system('cls' if os.name == 'nt' else 'clear')#a system clear that works for both mac and Windows (should prolly know this because it might help in the future)

def file_check(file):
    movements = []#list of movements from movements.txt
    deviation = []#collection of the deviated movement names
    deviation_numb = []#collection of the whole strings containing the deviated names
    wholeShit = "" #for the whole shit
    text = file

    #puts all of the text file into the list "wholeShit"
    f = open(text,"r")
    wholeShit = f.readlines()
    f.seek(0)
    f.close

    #puts all of the movements into list 'movements' like this to be a file and not a set list so that I can add new movements when I branch out
    for lines in open("movements.txt","r"):
        movements.append(lines.rstrip("\n"))

    #finds all of the movements that don't match
    for line in open(text,"r"):
        match = re.search(".+(?= [-])",line) #regex that grabs the movements
        if match != None:
            if (match.group()).lower() not in movements:
                #print("URETHRA") #prints URETHRA
                deviation.append(match.group())
                deviation_numb.append(match.string)

    #the process of changing the incorrect movements to the correct ones
    move_file = open("movements.txt","a")
    if len(deviation) == 0: 
        # print("No issues with {:}. Ready to analyze!".format(file))
        pass
    else: 
        for x in range(len(deviation)):
            print("Some deviations found: ")
            print("List of known excersizes: ")
            print(*movements, sep="\n")# current list of movements for user reference
            print("\nCurrent deviation: {:}".format(deviation[x]))
            user = input("Enter correct movement or '.' to add a new movement: ")# gets user to type the correct name or enter . to make a new movement to the movement list
            if user != '.': 
                index = wholeShit.index(deviation_numb[x])#finds the position of the current deviated string in "wholeShit"(list containing the whole docuement)
                new = deviation_numb[x].replace(deviation[x],user)#uses the deviation group found to replace it with the user entered one into the rest of the string
                wholeShit[index] = new #puts it where it belongs
            else:
                user = input("Enter the new movement to be added to the list: ")
                move_file.write("\n"+user)

    f = open(text, "w")
    f.writelines(wholeShit)
    f.close

def movement_script(): 
    movements = []
    for lines in open("movements.txt","r"):
        movements.append(lines.rstrip("\n"))
    return movements

if __name__ == "__main__":
    print("This is evan.py")
