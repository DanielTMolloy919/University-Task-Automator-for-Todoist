import csv
from datetime import date, timedelta

today = date.today()

this_week = 10 # The number of this week
start_week = 10 # The week you want to start repeating from
repeat_length = 1 # The number of weeks you want to repeat for

def date_to_string(date_obj): # Function to convert a python date object into a relative Todoist date sting
	delta = today - date_obj
	date_offset = delta.days # timedelta object to integer
	
	if date_offset == 0:
		return "today"
	elif date_offset < 0:
		return_string = "in " + str(abs(date_offset)) + " days"
		return return_string
	else:
		return_string = str(date_offset) + " days ago"
		return return_string

with open('University_Tasks.csv', 'w', newline='') as file:

    today = date.today()

    weekdates = []

    weekStart = today - timedelta(days=today.weekday()) # find the monday of this week

    iterationBeginning = weekStart - timedelta(weeks=(this_week - 1)) # find the monday of the first week

    weeks = [x for x in range(this_week,this_week + repeat_length)] # create array of weeks the user wants to be iterated over

    

    writer = csv.writer(file)

    writer.writerow(["TYPE","CONTENT","PRIORITY","INDENT","AUTHOR","RESPONSIBLE","DATE","DATE_LANG","TIMEZONE"]) # CSV rows that Todoist uses

    for i in weeks:
        section_name = "Week " + str(i);
        writer.writerow(["section", section_name]) 

       	thisMonday = iterationBeginning + timedelta(weeks=(i - 1)) # The monday of the current week

       	weekdates = [thisMonday + timedelta(days=i) for i in range(7)] # Date objects for each day in this week

        # # ELEC1710
        offset_date = date_to_string(weekdates[0])
        if i < 13:
            writer.writerow(["task", "ELEC1710 Prepare For W" + str(i) + " Lab @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            offset_date = date_to_string(weekdates[1])
            writer.writerow(["task", "ELEC1710 Lab W" + str(i) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            offset_date = date_to_string(weekdates[4])
            writer.writerow(["task", "ELEC1710 Lecture P1 W" + str(i) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            
            offset_date = date_to_string(weekdates[5])
            writer.writerow(["task", "ELEC1710 Lecture P2 W" + str(i) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            writer.writerow(["task", "ELEC1710 Tutorial " + str(i) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            

        #     writer.writerow(["task", "Statistics Workshop W" + str(i), 3, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
        # if i < 13:
        #     writer.writerow(["task", "Statistics Comp Lab W" + str(i), 3, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
        # if (i % 2) != 0 and i < 13:
        #     writer.writerow(["task", "Statistics Assignment W" + str(i), 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])

        # # ELEC2430
        offset_date = date_to_string(weekdates[0])
        if i < 13:
        #     offset_date = date_to_string(weekdates[5])
            writer.writerow(["task", "ELEC2430 Lecture P1 W" + str(i) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            offset_date = date_to_string(weekdates[2])
            writer.writerow(["task", "ELEC2430 Lecture P2 W" + str(i) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            writer.writerow(["task", "ELEC2430 Lab W" + str(i) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            offset_date = date_to_string(weekdates[4])
            writer.writerow(["task", "ELEC2430 Tutorial " + str(i - 1) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            writer.writerow(["task", "ELEC2430 Prepare For W" + str(i + 1) + " Lab @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])

        # # ENGG2500
        offset_date = date_to_string(weekdates[1])
        if i < 13:
            writer.writerow(["task", "ENGG2500 Lecture W" + str(i) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            offset_date = date_to_string(weekdates[2])
            writer.writerow(["task", "ENGG2500 Lab W" + str(i) + " @High_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
            offset_date = date_to_string(weekdates[4])
            writer.writerow(["task", "ENGG2500 Reflective Paragraph W" + str(i) + " @Low_Energy", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
        # offset_date = date_to_string(weekdates[3])
        # if (i % 2) != 0:
        #     writer.writerow(["task", "Elec Quiz W" + str(i + 1) + " Questions", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])
        # else:
        #     offset_date = date_to_string(weekdates[0])
        #     writer.writerow(["task", "Elec Quiz W" + str(i) + " Submit", 2, 1, "stracharater (10283909)","",offset_date,"en","Australia/Sydney"])