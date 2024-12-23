def calculate_age_and_grade(name, birth_year, score):
    current_year = 2025
    age = current_year - birth_year

    if score >= 80:
        grade = 'A'
    elif score >= 75:
        grade = 'B+'
    elif score >= 70:
        grade = 'B'
    elif score >= 65:
        grade = 'C+'
    elif score >= 60:
        grade = 'C'
    elif score >= 55:
        grade = 'D+'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'

    return {
        "name": name,
        "age": age,
        "grade": grade
    }

name = "Peter"
birth_year = 1998
score = 75

result = calculate_age_and_grade(name, birth_year, score)
output_path = "E:\Testing/Textfile.txt"
with open(output_path, "w", encoding="utf-8") as file:
    file.write(f"Name : {result['name']}\n")
    file.write(f"Age : {result['age']}\n")
    file.write(f"Software Testing Grade : {result['grade']}\n")

print(f"ผลลัพธ์ถูกบันทึกไว้ที่: {output_path}")