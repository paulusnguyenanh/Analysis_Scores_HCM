file = open("raw_data.txt","r")

# read first student

data = file.readline()

# make data to list

data = data.split("\\n")

#remove \r and \t 

for i in range(len(data)):
 	data[i] = data[i].replace("\\r","")
 	data[i] = data[i].replace("\\t","")


# remove tags
for i in range(len(data)):
	tags = []
	for j in range(len(data[i])):
		if data[i][j] == "<":
			begin = j
		if data[i][j] == ">":
			end = j
			tags.append(data[i][begin:end+1])

	for tag in tags:
		data[i] = data[i].replace(tag, "")

#remove whitespace characters 

for i in range(len(data)):
	data[i] = data[i].strip()

#remove empty lines

unempty_lines = []

for i in range(len(data)):
	if data[i] != "":
		unempty_lines.append(data[i])


data = unempty_lines

#choose infor

name = data[7]
dob = data[8]
scores = data[9]
data = [name,dob,scores]

#load unicode 

chars = []
codes = []
file = open("unicode.txt", encoding="utf-8")

unicode_table = file.read().split("\n")

for code in unicode_table:
	x = code.split(" ")
	chars.append(x[0])
	codes.append(x[1])

#replace special characters in name an scores

for i in range(len(chars)):
	name=name.replace(codes[i],chars[i])
	scores=scores.replace(codes[i],chars[i])
for i in range(len(name)):
	if name[i:i+2] == "&#":
		name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:]

for i in range(len(scores)):
	if scores[i:i+2] == "&#":
		scores = scores[:i] + chr(int(scores[i+2:i+5])) + scores[i+6:]


# change to lower case
name = name.lower()
scores = scores.lower()

# split dob

dob_list = dob.split("/")

dd = int(dob_list[0])
mm= int(dob_list[1])
yy = int(dob_list[2])

# process scores 
# remove 
scores = scores.replace(":","")
scores = scores.replace("khxh ", "khxh   ")
scores = scores.replace("khtn ", "khtn   ")
scores = scores.replace("10", " 10")
scores_list = scores.split("   ")


data = [name,str(dd),str(mm),str(yy)]
#add scores to data

for subject in ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]:
	if subject in scores_list:
		subject_name_position = scores_list.index(subject)
		subject_score_position = subject_name_position + 1
		subject_score = scores_list[subject_score_position]
		data.append(str(subject_score))
	else:
		data.append("-1")
#write data to file clean_data.txt

file = open("clean_data.txt",encoding="utf-8",mode="w")	
for i in range(len(data)):
	file.write(data[i] + ",")

