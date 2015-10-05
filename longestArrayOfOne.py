filename = "INPUT.TXT"

file = open(filename)
str = file.readline()
lastMax = 0
count = 0

for i in range(0, len(str)):
	if str[i] == "0":
		lastMax = count if count >= lastMax else lastMax
		count = 0
	if str[i] == "1" :
		count = count + 1

filenameOutput = "OUTPUT.TXT"
output = open(filenameOutput, "w")
output.write(lastMax)
