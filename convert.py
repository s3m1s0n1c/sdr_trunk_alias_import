import csv

csvFile = 'import.csv'
xmlFile = 'alias.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
    else:
        xmlData.write("\n")

        xmlData.write('   ' + '<alias list="' + row[0] + '" ' + 'group="' + row[1] + '" ' + 'iconName="' + row[2] + '" ' +  'color="' + row[3] + '" ' + 'name="' + row[4] + '">')
        xmlData.write('\n')
        xmlData.write('     ' + '<id type="' + row[5] + '" ' + 'value="' + row[6] + '" ' + 'protocol="' + row[7] + '"/>')
        xmlData.write('\n')
        xmlData.write('   ' + '</alias>')



    rowNum +=1

xmlData.close()

