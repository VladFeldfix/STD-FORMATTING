import xlsxwriter

# global variables
XL = {}
def writexl(loc, text, format):
    worksheet.write(loc, text, format)
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

# format
whiteformat = workbook.add_format({'text_wrap': True, 'valign': 'vcenter', 'align': 'right', 'border': 1, 'bg_color': '#e1e8ed'})
blackformat = workbook.add_format({'text_wrap': True, 'valign': 'vcenter', 'align': 'right', 'border': 1, 'bg_color': '#bcd3e3'})
header_format = workbook.add_format({'bold': True, 'bg_color': 'black', 'color': 'white'})

# cell size
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 10)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 40)
worksheet.set_column('E:E', 15)
worksheet.set_column('F:F', 20)
worksheet.set_column('G:G', 10)
worksheet.set_column('H:H', 20)
worksheet.set_column('I:I', 40)

# write to XL
# headers
writexl("A1", "דרישת אב", header_format)
writexl("B1", "מס דרישה", header_format)
writexl("C1", "דרישת בן", header_format)
writexl("D1", "הסבר לפונקציה", header_format)
writexl("E1", "סעיף תנאי הבדיקה", header_format)
writexl("F1", "תנאי בדיקה", header_format)
writexl("G1", "מס תסריט", header_format)
writexl("H1", "תסריט הבדיקה", header_format)
writexl("I1", "מטרה", header_format)

# READ LINES FROM CSV
index = 1
DRISHAT_BEN_ID = 0
SEIF = 0
color = 1
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

    # color
    if line[0] != "":
        color *= -1
    if color == 1:
        tf = whiteformat
    else:
        tf = blackformat
    writexl("A"+str(index), line[0], tf)
    writexl("B"+str(index), write_DRISHAT_BEN_ID, tf)
    writexl("C"+str(index), line[1], tf)
    writexl("D"+str(index), line[2], tf)
    writexl("E"+str(index), write_SEIF, tf)
    writexl("F"+str(index), line[3], tf)
    writexl("G"+str(index), index-1, tf)
    writexl("H"+str(index), line[4], tf)
    writexl("I"+str(index), line[5], tf)

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