'''Write a Python program to:

- Create two sets of student skills.
- Add one new skill using add().
- Add multiple skills using update().
- Remove one skill.
- Print:
  - Union
  - Intersection
  - Difference
  - Symmetric Difference
- Print the total number of skills and the sorted skills.'''
skills_set_a = {"Python", "Data Analysis", "SQL"}
print("The first set of skills:",skills_set_a)
skills_set_b = {"SQL", "Machine Learning", "Tableau", "Git"}
print("The second set of skills:",skills_set_b)
print("===================================================================")
skills_set_a.add("java")
print("The added list:",skills_set_a)
skills_set_b.remove("Git")
print("After removing Git:", skills_set_b)
skills_set_b.update(["Docker","AI"])
print("The update list:",skills_set_b)
union_skills =skills_set_a.union(skills_set_b)
print("The union of skills set:",union_skills)
intersection_skills = skills_set_a.intersection(skills_set_b)
print("The intersection of skills set:",intersection_skills)
difference_skills = skills_set_a.difference(skills_set_b)
print("The difference of skills set:",difference_skills)
symmetric_skills = skills_set_a.symmetric_difference(skills_set_b)
print("The symmetric of skills set:",symmetric_skills)
print("The total number of skills:",len(union_skills))
print("The sorted skills set:",sorted(union_skills))
print("===================================================================")