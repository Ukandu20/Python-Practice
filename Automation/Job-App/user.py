import os
from plantuml import PlantUML

# Define the use case scenarios
use_cases = {
    "Professor/Administrator": [
        "Create LinkedIn posts inviting recruiters",
        "Distribute access codes to students",
        "Manage student profiles"
    ],
    "Recruiter": [
        "Register on Campus Connect",
        "Utilize advanced search features",
        "Initiate direct messaging with candidates"
    ],
    "Student/Job Seeker": [
        "Create profile on Campus Connect",
        "Upload video showcasing skills",
        "Receive job offers from companies"
    ]
}

# Generate PlantUML code for the use-case diagram
plantuml_code = "@startuml\n"
plantuml_code += "left to right direction\n"

# Define actors
actors = list(use_cases.keys())
plantuml_code += "actor " + ", ".join(actors) + " as " + ", ".join(actors) + "\n\n"

# Define use cases
for actor, cases in use_cases.items():
    plantuml_code += "actor " + actor + " {\n"
    plantuml_code += "  " + "\n  ".join(cases) + "\n"
    plantuml_code += "}\n\n"

# Define interactions between actors and use cases
for actor, cases in use_cases.items():
    for case in cases:
        plantuml_code += actor + " --> " + case + "\n"

plantuml_code += "@enduml\n"

# Generate and save the use-case diagram
with open("use_case_diagram.txt", "w") as file:
    file.write(plantuml_code)

# Convert PlantUML code to image
uml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
uml.processes_file("use_case_diagram.txt")
