def go():
    # READ CSV
    file = open("STD.csv", 'r', encoding="utf-8")
    headers = file.readline()
    lines = file.readlines()
    file.close()

    # READ EACH LINE IN CSV TO CALCULATE HTML TEXT
    DRISHAT_AV = ""
    DRISHAT_AV_ID = 0
    DRISHAT_AV_ROWSPAN = {}
    DRISHAT_BEN = ""
    HESBER_FUNKZIA = ""
    DRISHAT_BEN_ID = 0
    DRISHAT_BEN_ROWSPAN = {}
    TASRIT = ""
    MISPAR_TASRIT  = 0
    MATARA = ""

    OUTPUT = []
    for line in lines:
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

        # set variables
        # drishat av
        if line[0] != "":
            DRISHAT_AV = line[0]
            DRISHAT_AV_ID += 1
        if not DRISHAT_AV_ID in DRISHAT_AV_ROWSPAN:
            DRISHAT_AV_ROWSPAN[DRISHAT_AV_ID] = 1
        else:
            DRISHAT_AV_ROWSPAN[DRISHAT_AV_ID] += 1
        
        # drishat ben
        if line[1] != "":
            DRISHAT_BEN = line[1]
            HESBER_FUNKZIA = line[2]
            DRISHAT_BEN_ID += 1
        if not DRISHAT_BEN_ID in DRISHAT_BEN_ROWSPAN:
            DRISHAT_BEN_ROWSPAN[DRISHAT_BEN_ID] = 1
            SEIF = DRISHAT_BEN_ID
        else:
            DRISHAT_BEN_ROWSPAN[DRISHAT_BEN_ID] += 1
        
        # tnaei bdika
        TNAEY_BDIKA = line[3]
        SEIF += 0.1
        SEIF = round(SEIF, 2)

        # tasrit
        TASRIT = line[4]
        MISPAR_TASRIT += 1

        # matara
        MATARA = line[5]

        # output line
        x = ""
        if line[1] != "":
            x = DRISHAT_BEN_ID
        OUTPUT.append((line[0], x, line[1], line[2], SEIF, line[3], MISPAR_TASRIT, line[4], line[5]))

    # WRITE HTML
    file = open("STD.html", 'w', encoding="utf-8")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<style>\n")
    file.write("table{font-family: arial, sans-serif; border-collapse: collapse; width: 100%; direction:rtl; text-align:right;}")
    file.write("td, th {border: 1px solid #dddddd;}")
    file.write("</style>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<table>\n")
    file.write("<tr>\n")
    file.write("<th>דרישת אב</th>\n")
    file.write("<th>מס דרישה</th>\n")
    file.write("<th>דרישת בן (פונקציה)</th>\n")
    file.write("<th>הסבר לפונקציה</th>\n")
    file.write("<th>סעיף תנאי הבדיקה</th>\n")
    file.write("<th>תנאי הבדיקה</th>\n")
    file.write("<th>מספר תסריט</th>\n")
    file.write("<th>תסריט הבדיקה</th>\n")
    file.write("<th>מטרה</th>\n")
    file.write("</tr>\n")
    for line in OUTPUT:
        file.write("<tr>\n")
        file.write("<td rowspan = "+DRISHAT_AV_ROWSPAN[9]+">"+str(line[0])+"</td>\n")
        file.write("<td>"+str(line[1])+"</td>\n")
        file.write("<td>"+str(line[2])+"</td>\n")
        file.write("<td>"+str(line[3])+"</td>\n")
        file.write("<td>"+str(line[4])+"</td>\n")
        file.write("<td>"+str(line[5])+"</td>\n")
        file.write("<td>"+str(line[6])+"</td>\n")
        file.write("<td>"+str(line[7])+"</td>\n")
        file.write("<td>"+str(line[8])+"</td>\n")
        file.write("</tr>\n")
    file.write("</table>\n")
    file.write("</body>\n")
    file.write("<footer>\n")
    file.write("</footer>\n")
    file.write("</html>\n")
    file.close()


class std_formatting_old:
    def __init__(self):
        # initiation
        self.OUTPUT = []
        self.readcsv()

    def line_to_list(self, line):
        # get a line return a list
        line = line.replace("\n", "")
        new_line = ""
        if '"' in line:
            change_comma = False
            for ch in line:
                if ch == '"':
                    change_comma = not change_comma
                    ch = ""
                if ch == ',' and change_comma:
                    ch = '#comma'
                new_line += ch
        else:
            new_line = line
        line = new_line.split(",")
        x = 0
        while x < len(line)-1:
            if '#comma' in line[x]:
                line[x] = line[x].replace("#comma", ",")
            x += 1
        return line

    def readcsv(self):
        # read csv file
        file = open("STD.csv", 'r', encoding="utf-8")
        self.headers = file.readline()
        self.headers = self.line_to_list(self.headers)
        self.lines = file.readlines()
        file.close()
        self.for_each_line()
    
    def for_each_line(self):
        # general variables
        drishat_av = ""
        drishat_ben = ""
        mispar_drisha = 0
        seif_tnaei_bdika = 0.0
        mispar_tasrit = 0
        self.rospan = {}
        
        # go over each line
        line_number = 0
        rowspans_key = 0
        for line in self.lines:
            line = self.line_to_list(line)
            if line[0] != drishat_av:
                if line[0] != "":
                    drishat_av = line[0]
                    rowspans_key = line_number
                    self.rospan[rowspans_key] = 0
                else:
                    self.rospan[line_number] = 1
            self.rospan[rowspans_key] += 1
            drishat_ben = line[1]
            if drishat_ben != "":
                mispar_drisha += 1
                seif_tnaei_bdika =  float(mispar_drisha)
            hesber_la_funccia = line[2]
            tnaey_bdika = line[3]
            if tnaey_bdika != "":
                seif_tnaei_bdika += 0.1
            seif_tnaei_bdika = round(seif_tnaei_bdika, 2)
            tasrit_brika = line[4]
            mispar_tasrit += 1
            matara = line[5]
            self.OUTPUT.append((drishat_av, mispar_drisha, drishat_ben, hesber_la_funccia, seif_tnaei_bdika, tnaey_bdika, mispar_tasrit, tasrit_brika, matara))            
            line_number += 1
            #print(drishat_av)
            #input(self.rospan)

        self.generate_html()
    
    def generate_html(self):
        file = open("STD.html", 'w', encoding="utf-8")
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("<style>\n")
        file.write("table{font-family: arial, sans-serif; border-collapse: collapse; width: 100%; direction:rtl; text-align:right;}")
        file.write("td, th {border: 1px solid #dddddd;}")
        file.write("</style>\n")
        file.write("</head>\n")
        file.write("<header>\n")
        file.write("<table>\n")

        file.write("</table>\n")
        file.write("</header>\n")
        file.write("<body>\n")
        file.write("<table>\n")
        file.write("<tr>\n")
        file.write("<th>דרישת אב</th>\n")
        file.write("<th>מס דרישה</th>\n")
        file.write("<th>דרישת בן (פונקציה)</th>\n")
        file.write("<th>הסבר לפונקציה</th>\n")
        file.write("<th>סעיף תנאי הבדיקה</th>\n")
        file.write("<th>תנאי הבדיקה</th>\n")
        file.write("<th>מספר תסריט</th>\n")
        file.write("<th>תסריט הבדיקה</th>\n")
        file.write("<th>מטרה</th>\n")
        file.write("</tr>\n")
        i = 0
        print(self.rospan)
        for line in self.OUTPUT:
            file.write("<tr>\n")
            e = 0
            for element in line:
                rowspan = ""
                print(i)
                if e == 0:
                    rowspan = "rowspan="+str(self.rospan[i])
                file.write("<td "+rowspan+">"+str(element)+"</td>\n")
                e += 1
            file.write("</tr>\n")
            i += 1
        file.write("</table>\n")
        file.write("</body>\n")
        file.write("<footer>\n")

        file.write("</footer>\n")
        file.write("</html>\n")

#std = std_formatting()

go()