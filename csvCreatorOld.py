# Program Mission - Take inputs from user to create a customised Todoist csv project template for assessments and exam study
# Program Outline
# - Query if program is assessment or exam study
# - IF exam
#   - Get user to list all topic areas not studied yet and estimated hours of study for each DONE
#   - Query how many past papers are available DONE
#   - Estimate how long taking one practice paper and post-practice paper studying will take DONE
# - IF assessment
#   - Query user to list all substages of project, then number of hours of work required per DONE
#   - Query user for project milestones and due dates before finish date (e.g. Report Draft 1 must be complete 2 weeks before due date)
# - Query estimated number of hours available to study per week (maybe have this variable between weeks?)
# - Output CSV file which creates study plan based on available hours (with buffer), works out how many days in advance user must begin studying (with buffer)
#   - Additionally, CSV must take into account early submission date to avoid blackboard uploading issues etc.
# - Create regular backups to json file
#   - Enables user upload json file after modification for easy editing of mistakes in CSV files

import csv, json

# list of currently accepted types of templates
programsList = ['assessment','exam']
programType = ""

# asks the user to input the template type, and only finished when the user inputs an existing type on the 'programsList' list
def topicAreasHandling():
	print('\nPlease enter all topic areas not yet covered and the hours required to finish: ')

	topicAreasList = []

	while True:
		userInput = input()
		if not userInput:
			break
		
		elif topicAreasEntry(userInput):
			topicAreasList.append(topicAreasEntry(userInput))

		print(topicAreasList)

def topicAreasEntry(x):
	userInput = x.lower()

	userInputList = userInput.split()

	if len(userInputList) != 2:
		print("Error: Incorrect amount of arguments, please try again")
		return False

	try:
		userInputList[1] = float(userInputList[1])
	except:
		print("Error: You didn't enter an number, please try again")
		return False

	return userInputList

def pastPapersHandling():
	pastPapersDict = {}

	pastPapersDict['past paper'] = pastPapersEntry()

	while True:
		userInput = input("\nIs there another type of past paper? ")

		if not errorChecking(userInput,'boolean'):
			continue

		userInput = errorChecking(userInput, 'boolean')

		if userInput == 'y':
			while True:
				pastPaperName = input('\nWhat is the name of this past paper type? ')

				if not errorChecking(pastPaperName,'string'):
					continue

				pastPapersDict[pastPaperName] = pastPapersEntry()
				break
		else:
			break

	return pastPapersDict

def pastPapersEntry():
	print("\nEnter number of past papers available: ")

	pastPapersTemp = {}

	while True:
		userInput = input()

		if not errorChecking(userInput,'integer'):
			continue

		pastPapersTemp['amount'] = userInput

		break

	print("\nEnter approximate time to a finish past paper: ")

	while True:
		userInput = input()

		if not errorChecking(userInput,'float'):
			continue

		pastPapersTemp['time'] = userInput

		break

	return pastPapersTemp

def errorChecking(test,expectedType):
	testInput = test

	if expectedType == 'integer':
		try:
			testInput = int(testInput)
			return testInput
		except:
			print("Error: You didn't enter a number, please try again")
			return False

	elif expectedType == 'float':
		try:
			testInput = float(testInput)
			return testInput
		except:
			print("Error: You didn't enter a number, please try again")
			return False

	elif expectedType == 'string':
		try:
			testInput = float(testInput)
			print("Error: You didn't enter a number, please try again")
			return False
		except:
			return testInput

	elif expectedType == 'boolean':
		testInput = testInput.lower(

)		if testInput == 'y' or testInput == 'yes':
			testInput = 'y'
			return testInput
		elif testInput == 'n' or testInput == 'no':
			testInput = 'n'
			return testInput
		else:
			print("Error: you didn't enter with yes or no, please try again")
			return False

def studyPlanner():
	jsonPathway = './data/'
	studyHoursTemplate = jsonPathway + 'studyHoursTemplate.json'

	with open(studyHoursTemplate, 'r') as x:
		studyHoursDict = json.load(x)

	# Copy template for estimated number of weeks project spans

while True:
	programUserInput = input('Please enter type of program: ')
	programUserInput = programUserInput.lower()

	if programUserInput in programsList:
	    programType = programUserInput
	    break

	print('Error program type does not exist, please try again')

if programType == programsList[0]:
	topicAreasList = topicAreasHandling()

elif programType == programsList[1]:
	topicAreasList = topicAreasHandling()

	pastPapersDict = pastPapersHandling()

studyPlanner()