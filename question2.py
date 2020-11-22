# Greedy approach to graph coloring problem
# Have two sessions a day morning AM and afternoon PM
slots = ["MonAM", "MonPM", "TueAM", "TuePM", "WedAM", "WedPM", "ThurAM", "ThurPM", "FriAM", "FriPM"]

courses = ["ML", "CR", "AL", "S", "AD", "DM", "SE", "D"]

coursesMap = {"ML": ["CR", "S", "AD", "DM", "D"],
              "CR": ["ML", "AD", "DM"],
              "AL": ["DM", "SE", "D"],
              "S": ["ML", "D"],
              "AD": ["ML", "CR", "DM"],
              "DM": ["ML", "CR", "AL", "AD", "SE"],
              "SE": ["AL", "DM"],
              "D": ["ML", "AL", "S"]}

timeTable = {}

def check(course, slot):
    for cs in coursesMap.get(course):
        nextSess = timeTable.get(cs)
        if nextSess == slot:
            return False

    return True


def getSlot(course):
    for slot in slots:
        if check(course, slot) and sum(value == slot for value in timeTable.values()) < 2:
            return slot


def main():
    for course in courses:
        timeTable[course] = getSlot(course)

    print()
    print(timeTable)


main()

