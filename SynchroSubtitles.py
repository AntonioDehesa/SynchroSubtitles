import datetime
inputFile='español.srt' #change the name for the file you want to change
outputFile='salida.srt' #change it for the name of the output file
time_delay = 43         #displace the subtitles or text for this many seconds. 


def chop_time(t):       #This function cuts the last three zeros of the miliseconds
    return t[:-4]



wr = open(outputFile, 'w')
rd = open(inputFile,'r')
formatOne = "%H:%M:%S.%f "      #This two are the formats of the subtitles. Change them as you see fit. 
formatTwo = " %H:%M:%S.%f\n"
for row in rd:                  #Go through all the file
    if ('-->' in row):          #This is the symbol that divides the timestamps of the subtitles. If this symbol is present in the
                                #line, it means this line is a subtitle. Change it as you see fit. 
        row = row.replace(',','.')          #datetime does not accept ',' so we change it to '.'
        firstTime = row.split("-->")[0]     #This is the first timestamp
        secondTime = row.split("-->")[1]    #This is the second timestamp
        time1 = datetime.datetime.strptime(firstTime,formatOne) #We obtain the timestamps in the needed formats
        time2 = datetime.datetime.strptime(secondTime,formatTwo)
        correctTime1 = time1 + datetime.timedelta(0,time_delay) #The change is performed in these lines. 
        correctTime2 = time2 + datetime.timedelta(0,time_delay)
        correctTimeString1 = correctTime1.strftime(formatOne)
        correctTimeString2 = correctTime2.strftime(formatTwo)
        stringList = [correctTimeString1.replace('.',','),' --> ',correctTimeString2.replace('.',',')]#We return the ',' to where it should be
        stringList[0] = chop_time(stringList[0])    #We cut the zeros
        stringList[2] = chop_time(stringList[2]) + "\n" #The lineskip is added
        finalString = ''.join(stringList)           #Finally, the string is added to the 
        wr.write(''.join(finalString))
    else:
        wr.write(''.join(row))
    