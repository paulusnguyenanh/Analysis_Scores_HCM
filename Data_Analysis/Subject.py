# read file
with open("data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# turn each student to a list
for i in range(len(students)):
	students[i] = students[i].split(",")

# remove empty list (end of file)
students.pop()

# number of students who took 0,1,2,3,... subjects
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	for i in range(11):
		if s[i+5] != "-1":
			count += 1

	num_of_exam_taken[count] += 1

print(num_of_exam_taken)


import matplotlib.pyplot as plt
labels = "2", "3", "4", "5", "6", "7", "other"
sizes = [122, 2598, 4334, 318, 2730, 64261, 81]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue',"#FFEB3B","#AED581","#FFD54F"]


fig1, ax1 = plt.subplots()
ax1.set_title("tỉ lệ số môn thi")
ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)

plt.show()

