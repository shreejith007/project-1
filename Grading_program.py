Student_score={
    "Ram":81,
    "Shyam":78,
    "Preeti":99,
    "john":74,
    "Nayan":62,
}
Student_grade={} #empty dictionary cretaed here 

for student in Student_score:
    score=Student_score[student]
    if score >90:
        Student_grade[student]="outstanding"
    elif score >80 and score <89:
       Student_grade[student]="Exceed Expectation"
    elif score>70 and score <79:
        Student_grade[student]="Acceptable"
    else:
        Student_grade[student]="Fail"
        
print(Student_grade)