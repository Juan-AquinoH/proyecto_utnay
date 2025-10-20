# The following dictionary shows the grades of all subjects for each student. 
#Create a new dictionary that contains only the student's name and their average 
#grade.  
#Note: You may use the sum() function, which takes a list or tuple and returns the 
#sum of its elements. 
grades = {
    "Guillermo Arroyo": {"Matematicas": 85, "Fisica": 90, "English": 78},
    "Francisco Carrillo": {"Matematicas": 75, "Fisica": 80, "English": 88},
    "Gilberto Escamilla": {"Matematicas": 92, "Fisica": 87, "English": 85}
}

average_grades = {}

for student, subjects in grades.items():
    total = sum(subjects.values())
    average = total / len(subjects)
    average_grades[student] = average
    print(f"{student}: {average:.2f}")

print("Average Grades:", average_grades)

#resultados esperados:
#Guillermo Arroyo: 84.33
#Francisco Carrillo: 81.00
#Gilberto Escamilla: 88.00
#Average Grades: {'Guillermo Arroyo': 84.33333333333333, 'Francisco Carrillo': 81.0, 'Gilberto Escamilla': 88.0#