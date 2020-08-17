import os;os.system("cls")
num_subjects = int(float(input(" ENTER NUMBER OF SUBJECTS : ")))
counter = 0
marks_list = []
while (counter != num_subjects) :
    marks = int(float(input(" ENTER MARK OF SUBJECT : ")))
    marks_list.append(marks)
    counter += 1
print(" YOUR AVERAGE MARKS ARE :",((sum(marks_list))/num_subjects))
