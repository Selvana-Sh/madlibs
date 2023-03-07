import random

# intro
print("--------Welcome to MAD LIBS--------")
#common words in at least two of the stories
general = {
  
  "noun1": "",
  "noun2": "",

  "adj1": "",
  "adj2" : "",
  "adj3"  :"",

  "number": 0,

  "color" : "",

  "sillyWord" : "",

  "time" : "",

  "verb_ing" : "",

  "properNoun" : "",

  "animal" : "",

}

#words in story no.1
temp_1 = {
  
  "noun3": "",
  "noun4" : "",
  
  "bodyPart1": "",
  "bodyPart2": "",

  "num1": 0,
  "num2": 0,
  
  "modeOfTransportation": "",
  "verb": ""
}

# words in story no.2
temp_2 = {
  "adverb" : "",
 
  "adjFeling1" : "",
  "adjFeeling2" : "",

  "verb1" : "",
  "verb2" : "" 
}

# words in story no.3
temp_3 = {

  "place" : "",
  "roomInHouse" : "",
  
  "adj4"  :"",

  "magicalCreaturePl1": "",
  "magicalCreaturePl2": "",

  "noun3" : "", #noun5

  "nounPl1" : "", #noun3
  "nounPl2" : "", #noun4
}

# select story
story = random.randint(1, 3)

#temprory test
#story = int(input("enter a number for story"))

# story 1:
def story_1():
  temp_1["num1"] += int(input("number: "))  
  general["time"] = str(input("mesure of  time: "))
  temp_1["modeOfTransportation"] = str(input("which mode of transportation : "))
  general["adj1"] = str(input("give us the first adjective: "))
  general["adj2"] = str(input("give us an adjective: "))
  general["noun1"] = str(input("give us the first noun: "))
  general["color"] = str(input("which color would you prefer: "))
  temp_1["bodyPart1"] = str(input("name a body part: "))
  temp_1["verb"] = str(input("which verb would you prefer?: "))
  temp_1["num2"] += int(input("give us anumber: "))
  temp_1["noun2"] = str(input("a noun please?: "))
  temp_1["noun3"] = str(input("give us another noun: "))
  temp_1["bodyPart2"] = str(input("name the last body part: "))
  temp_1["noun4"] = str(input("give us one last noun: "))
  general["adj3"] = str(input("give us an adjective: "))
  general["sillyWord"] = str(input("give us a silly Word: "))


# Story 2:
def story_2():
  general["properNoun"] = str(input("Give us a proper noun: "))
  general["noun1"] = str(input("Give us the first noun: "))
  temp_2["adjFeling1"] = str(input("Give us the first adjective which describes a feeling: "))
  temp_2["verb1"] = str(input("Give us the first verb: "))
  general["animal"] = str(input("Give us a name of an animal: "))
  temp_2["adjFeeling2"] = str(input("Give us the second adjective which describes a feeling: "))
  temp_2["verb2"] = str(input("Give us the second verb: "))
  general["color"] = str(input("Give us a color: "))
  general["verb_ing"] = str(input("Give us a verb ending with -ing: "))
  temp_2["adverb"] = str(input("Give us an adverb: "))
  general["number"] += int(input("Give us a number: "))
  general["time"] = str(input("Give us a time: "))
  general["sillyWord"] = str(input("Give us a silly word: "))
  general["noun2"] = str(input("Give us the second noun: "))

# story 3:
def story_3():
  general["properNoun"] = str(input("Give us a proper noun: "))
  general["adj1"] = str(input("give us the first adjective: "))
  general["color"] = str(input("Give us a color: "))
  general["animal"] = str(input("Give us a name of an animal: "))
  temp_3["place"] = str(input("Name a place: "))
  general["adj2"] = str(input("give us an adjective: "))
  temp_3["magicalCreaturePl1"] = str(input("Give us a name for the first magical place: "))
  general["adj3"] = str(input("give us an adjective: "))
  temp_3["magicalCreaturePl2"] = str(input("Give us a name for the second magical place: "))
  temp_3["roomInHouse"] = str(input("Name a room in a House: "))
  general["noun1"] = str(input("Give us the first noun: "))
  general["noun2"] = str(input("Give us the second noun: "))
  temp_3["nounPl1"]= str(input("Give us the first noun (in plural): "))
  temp_3["adj4"] =str(input("Give us an adjective: "))
  temp_3["nounPl2"]= str(input("Give us the second noun (in plural): "))
  general["number"] += int(input("Give us a number: "))
  general["time"] = str(input("Give us a time: "))
  general["verb_ing"] = str(input("Give us a verb ending with -ing: "))
  temp_3["adj5"] =str(input("Give us an adjective: "))
  temp_3["noun3"] = str(input("Give us the last noun: "))

if(story== 1):
  print("\nYou've got the First Story!!\n")
  story_1()
  print("\nYour story is done\n")
  op1 = f'It was about {temp_1["num1"]} {general["time"]} ago when i arrived at the hospital in a {temp_1["modeOfTransportation"]}\nThe hospital is a/an {general["adj1"]} place, there are a lot of {general["adj2"]} {general["noun1"]} here. There are nurses here who have {general["color"]} {temp_1["bodyPart1"]}.\nIf someone wants to come into my room I told them that they have to {temp_1["verb"]} first.\nI\'ve decorated my room with {temp_1["num2"]} {general["noun2"]}.\nToday I talked to a doctor and they were wearing a {temp_1["noun3"]} on their {temp_1["bodyPart2"]}.\nI heard that all doctors {temp_1["verb"]} {temp_1["noun4"]}every day for breakfast. The most {general["adj3"]} thing about being in the hospital is the {general["sillyWord"]} {general["noun1"]}'
  print(op1)
elif(story==2):
  print("\nYou've got the Second Story!!\n")
  story_2()
  print("\nYour story is done\n")
  op2 = f'This weekend I\'m going camping with {general["properNoun"]}.\nI packed my lantern, sleeping bag, and {general["noun1"]}.\nI am so {temp_2["adjFeling1"]} to {temp_2["verb1"]} in a tent.\nI am {temp_2["adjFeeling2"]}.\nwe might see a(n) {general["animal"]}, I hear they\'re kind of dangerous.While we\'re camping, we are going to hike, fish, and {temp_2["verb2"]}.\nI have heard that the {general["color"]} lake is great for {general["verb_ing"]}\nThen we will {temp_2["adverb"]} hike through the forest for {general["number"]} {general["time"]}.\nIf I see a {general["color"]} {general["animal"]} while hiking, I am going to bring it home as a pet!\nAt night we will tell {general["number"]} {general["sillyWord"]} stories and roast {general["noun2"]} around the campfire!!'
  print(op2)
elif(story==3):
  print("\nYou've got the Third Story!!\n")
  story_3()
  print("\nYour story is done\n")
  op3 = f'Dear {general["properNoun"]}, I am writing to you from a {general["adj1"]} castle in an enchanted forest.\nI found myself here one day after going for a ride on a {general["color"]} {general["animal"]} in {temp_3["place"]}.\nThere are {general["adj2"]} {temp_3["magicalCreaturePl1"]} and {general["adj3"]} {temp_3["magicalCreaturePl2"]} here!\nIn the {temp_3["roomInHouse"]} there is a pool full of {general["noun1"]}.\nI fall asleep each night on a {general["noun2"]} of {temp_3["nounPl1"]} and dream of {temp_3["adj4"]} {temp_3["nounPl2"]}.\nIt feels as though I have lived here for {general["number"]} {general["time"]}.\nI hope one day you can visit, although the only way to get here now is {general["verb_ing"]} on a {temp_3["adj5"]} {temp_3["noun3"]}!!'
  print(op3)
else:
  print("what the hell man:/")

print("\nThank you for playing our game!")