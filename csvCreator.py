import csv
from datetime import date, timedelta

start_week = 1
end_week = 10
beginning_of_semester_date = date(2021,7,19)

def date_to_string(date_offset):
    if date_offset == 0:
        return "today"
    elif date_offset > 0:
        return_string = "in " + str(date_offset) + " days"
        return return_string
    else:
        return_string = str(abs(date_offset)) + " days ago"
        return return_string

with open('University_Tasks.csv', 'w', newline='') as file:

    week = start_week

    start_date = beginning_of_semester_date

    today = date.today()

    weekdates = []

    weekStart = start_date - timedelta(days=start_date.weekday()) # find the monday of this week

    for i in range(7): # create an array of this week's dates
        week_day = weekStart + timedelta(days=i)
        days_to = week_day - today
        weekdates.append(days_to.days)

    #weekdates = [x+7 for x in weekdates]

    #my_string = date_to_string(weekdates[2])

    writer = csv.writer(file)

    writer.writerow(["TYPE","CONTENT","PRIORITY","INDENT","AUTHOR","RESPONSIBLE","DATE","DATE_LANG","TIMEZONE"])

    for i in range(week,end_week):
        section_name = "Week " + str(i);
        writer.writerow(["section", section_name])
        if (i != week):
            weekdates = [x+7 for x in weekdates]

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