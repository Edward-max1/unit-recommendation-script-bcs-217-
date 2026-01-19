# AI-Based Course Recommendation Expert System
# Rule-Based System using Forward Chaining

def get_choice(prompt, options):
    print(prompt)
    for key, value in options.items():
        print(f"{key}. {value}")
    return options.get(int(input("Enter option number: ")))

def recommend_courses(career, skill, learning):
    recommendations = set()

    # Rule Set 1: Data Science / AI
    if career == "Data Science / AI" and skill in ["Mathematics", "Programming"]:
        recommendations.update([
            "Data Analysis Techniques",
            "Intelligent Systems",
            "Interactive Programming with Python"
        ])

    # Rule Set 2: Software Development
    if career == "Software Development" and skill == "Programming":
        recommendations.update([
            "Advance Java Programming",
            "Interactive Programming with Python",
            "Information Systems"
        ])

    # Rule Set 3: Networking / Systems
    if career == "Networking / Systems":
        recommendations.update([
            "Network Programming",
            "Information Systems",
            "Advance Java Programming"
        ])

    # Rule Set 4: Embedded / Signal Processing
    if career == "Embedded / Signal Processing" and skill == "Mathematics":
        recommendations.update([
            "Signals and Systems",
            "Digital Signal Processing I",
            "Intelligent Systems"
        ])

    # Rule Set 5: Mobile / App Development
    if career == "Mobile / Application Development":
        recommendations.update([
            "Mobile Computing",
            "Interactive Programming with Python",
            "Advance Java Programming"
        ])

    # Constraint Rule
    if len(recommendations) < 3:
        recommendations.add("Interactive Programming with Python")

    return recommendations


# ----- User Interaction -----
career_options = {
    1: "Software Development",
    2: "Data Science / AI",
    3: "Networking / Systems",
    4: "Embedded / Signal Processing",
    5: "Mobile / Application Development"
}

skill_options = {
    1: "Programming",
    2: "Mathematics",
    3: "Networking",
    4: "Problem Solving"
}

learning_options = {
    1: "Theory-oriented",
    2: "Practical / Hands-on"
}

career = get_choice("\nSelect Career Interest:", career_options)
skill = get_choice("\nSelect Skill Strength:", skill_options)
learning = get_choice("\nSelect Learning Preference:", learning_options)

courses = recommend_courses(career, skill, learning)

print("\nRecommended Elective Units:")
for course in courses:
    print("-", course)
