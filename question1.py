# Greedy approach to graph coloring problem
tables = ["Table1", "Table2", "Table3", "Table4", "Table5"]

groupLeader = ["Diane", "Magura", "Fabrice", "Taiwo", "Maysa", "Ruth", "Ken", "Masupa", "Jane"]

groups = {}
groups["Diane"] = []
groups["Magura"] = ["Taiwo"]
groups["Fabrice"] = ["Maysa"]
groups["Taiwo"] = ["Magura", "Ruth", "Ken", "Masupa"]
groups["Maysa"] = ["Fabrice"]
groups["Ruth"] = ["Taiwo"]
groups["Ken"] = ["Taiwo"]
groups["Masupa"] = ["Taiwo"]
groups["Jane"] = []

groupTables = {}


def check(groupleader, table):
    for group in groups.get(groupleader):
        nextTable = groupTables.get(group)
        if nextTable == table:
            return False

    return True


def getTable(groupleader):
    for table in tables:
        if check(groupleader, table):
            return table


def main():
    for groupLeader in groups:
        groupTables[groupLeader] = getTable(groupLeader)

    print(groupTables)


main()
