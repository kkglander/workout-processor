#This file is for converting the dictionary to a json
#To be honest, i thought this would be harder

def dict2json(dict):
    dict_string = str(dict)
    aJSONhopefully = dict_string.replace("'",'"')
    return aJSONhopefully
