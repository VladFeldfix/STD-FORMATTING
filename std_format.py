import xlsxwriter

# global variables
XL = {}
def writexl(loc, text):
    worksheet.write(loc, text)
    XL[loc] = text

# READ CSV
file = open("STD.csv", 'r', encoding="utf-8")
headers = file.readline()
lines = file.readlines()
file.close()

# OPEN XL
workbook = xlsxwriter.Workbook('std.xlsx')
worksheet = workbook.add_worksheet('טבלת דרישות')
worksheet.right_to_left()

# write to XL
# headers
writexl("A1", "דרישת אב")
writexl("B1", "מס דרישה")
writexl("C1", "דרישת בן (פונקציה)")
writexl("D1", "הסבר לפונקציה (מה)")
writexl("E1", "סעיף תנאי הבדיקה")
writexl("F1", "תנאי בדיקה test condition (איך)")
writexl("G1", "מס תסריט")
writexl("H1", "תסריט הבדיקה test case")
writexl("I1", "מטרה")

# READ LINES FROM CSV
index = 1
DRISHAT_BEN_ID = 0
SEIF = 0
for line in lines:
    index += 1
    # remove \n
    line = line.replace("\n", "")
    
    # replace intext comma with #comma#
    fixed_line = ""
    replace_comma = False
    for ch in line:
        if ch == '"':
            replace_comma = not replace_comma
            ch = ""
        if ch == "," and replace_comma:
            ch = "#comma#"
        fixed_line += ch
    line = fixed_line

    # split line to list
    line = line.split(",")
    i = 0
    for x in line:
        line[i] = x.replace("#comma#", ",")
        i += 1
    
    if line[1] != "":
        DRISHAT_BEN_ID += 1
        SEIF = DRISHAT_BEN_ID
        write_DRISHAT_BEN_ID = DRISHAT_BEN_ID
    else:
        write_DRISHAT_BEN_ID = ""

    SEIF += 0.1
    SEIF = round(SEIF, 2)

    if line[3] != "":
        write_SEIF = SEIF
    else:
        write_SEIF = ""

    # write
    writexl("A"+str(index), line[0])
    writexl("B"+str(index), write_DRISHAT_BEN_ID)
    writexl("C"+str(index), line[1])
    writexl("D"+str(index), line[2])
    writexl("E"+str(index), write_SEIF)
    writexl("F"+str(index), line[3])
    writexl("G"+str(index), index-1)
    writexl("H"+str(index), line[4])
    writexl("I"+str(index), line[5])

# MERGE ver XL
for area in "ABCDEFGHI":
    x = 1
    pointer = area
    start = pointer+str(x)
    end = start
    while pointer+str(x) in XL:
        if XL[pointer+str(x)] != "":
            start = pointer+str(x)
        else:
            end = pointer+str(x)
            if start != end:
                worksheet.merge_range(start+":"+end, XL[pointer+str(x)])
        x += 1

workbook.close()