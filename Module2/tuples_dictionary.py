grades = {
    ("john", "math"): 5,
    ("alice", "biology"): 4,
    ("eva", "music"): 3,
    ("john", "englixh"): 4
}

john_math = grades[("john", "math")]
print("john's grade in math is",john_math)

grades[("florjon", "edukat fizike")] = 5
print(grades)

keys = list(grades.keys())
print(keys)

student, subject = keys[0]
print(student,"'s grades in",subject, "is", john_math)