def convert_to_buddhist_era(age):
    current_year = 2568 
    buddhist_era_year = current_year - age
    return buddhist_era_year

def convert_grade_to_rank(grade):
    grade_to_rank = {
        "A": "High Distinction",
        "B+": "Distinction",
        "B": "Distinction",
        "C+": "Good",
        "C": "Good",
        "D+": "Normal",
        "D": "Normal",
        "F": "Failed"
    }
    return grade_to_rank.get(grade, "Unknown Rank")


def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    data = {}
    for line in lines:
        key, value = line.strip().split(" : ")
        data[key.strip()] = value.strip()
    return data

def main():
    file_path = "E:\Testing/Textfile.txt" 

    data = read_file(file_path)
    
    name = data.get("Name")
    age = int(data.get("Age", 0))
    grade = data.get("Software Testing Grade")
    
    buddhist_era = convert_to_buddhist_era(age)
    rank = convert_grade_to_rank(grade)
    
    print(f"Name : {name}")
    print(f"Buddhist Era : {buddhist_era}")
    print(f"Software Testing Rank : {rank}")

if __name__ == "__main__":
    main()
