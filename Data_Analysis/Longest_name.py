# read file
with open("clean_data.csv", encoding="utf8") as file:
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

max_name_length = 0 # Độ dài của tên
index = 0 # Vị trí của tên dài nhất
for i in range(len(students)):
	# so sánh độ dài của học sinh i với max_length_index
	# Nếu dài hơn thì lấy nó làm thí sinh dài nhất
	if len(students[i][1]) >= max_name_length:
		max_name_length = len(students[i][1])
		index = i

# In số báo danh
print(students[index][0])
# In tên 
print(students[index][1])