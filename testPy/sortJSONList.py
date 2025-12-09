import json
from typing import List, Dict, Any, Union

#!/usr/bin/env python3
# File: /home/nagarro/Desktop/Workspace/sortJSONList.py
# Creates a JSON list of student info, saves it, loads it, and shows sorting examples.


STUDENTS_JSON = "students.json"

sample_students: List[Dict[str, Any]] = [
    {"id": 1, "name": "Alice Johnson", "age": 20, "grade": 88.5, "subjects": ["Math", "Physics"]},
    {"id": 2, "name": "Bob Smith",     "age": 22, "grade": 91.0, "subjects": ["History", "English"]},
    {"id": 3, "name": "Cara Lee",      "age": 19, "grade": 79.0, "subjects": ["Biology", "Chemistry"]},
    {"id": 4, "name": "David Kim",     "age": 21, "grade": 91.0, "subjects": ["Math", "Computer Science"]},
    {"id": 5, "name": "Eva Green",     "age": 20, "grade": 85.0, "subjects": ["Art", "Design"]},
]

def save_json(path: str, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def sort_students(students: List[Dict[str, Any]],
                  key: Union[str, callable] = "name",
                  reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sort students by a dict key name (e.g. 'name', 'age', 'grade') or by a callable.
    Stable sort; non-existent keys are treated as None.
    """
    if isinstance(key, str):
        key_func = lambda s: s.get(key)
    else:
        key_func = key
    return sorted(students, key=key_func, reverse=reverse)

if __name__ == "__main__":
    # Save sample list to students.json
    save_json(STUDENTS_JSON, sample_students)

    # Load and print original
    students = load_json(STUDENTS_JSON)
    print("Original:")
    print(json.dumps(students, indent=2, ensure_ascii=False))

    # Examples of sorting
    by_name = sort_students(students, key="name")
    by_grade_desc = sort_students(students, key="grade", reverse=True)
    by_grade_then_age = sorted(students, key=lambda s: (-s.get("grade", 0), s.get("age", 0)))

    print("\nSorted by name:")
    print(json.dumps(by_name, indent=2, ensure_ascii=False))

    print("\nSorted by grade (desc):")
    print(json.dumps(by_grade_desc, indent=2, ensure_ascii=False))

    print("\nSorted by grade (desc) then age (asc):")
    print(json.dumps(by_grade_then_age, indent=2, ensure_ascii=False))