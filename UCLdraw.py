import random

# Define the team information in pots
# Define the information for each pot
pot_1 = [
    {"team": "Manchester City", "coef": 145.000, "country": "Eng"},
    {"team": "Sevilla", "coef": 91.000, "country": "Esp"},
    {"team": "FC Barcelona", "coef": 98.000, "country": "Esp"},
    {"team": "Napoli", "coef": 81.000, "country": "Ita"},
    {"team": "Bayern München", "coef": 136.000, "country": "Ger"},
    {"team": "Paris Saint-Germain", "coef": 112.000, "country": "Fra"},
    {"team": "Benfica", "coef": 82.000, "country": "Por"},
    {"team": "Feyenoord", "coef": 51.000, "country": "Ned"}
]

pot_2 = [
    {"team": "Real Madrid", "coef": 121.000, "country": "Esp"},
    {"team": "Manchester United", "coef": 104.000, "country": "Eng"},
    {"team": "Internazionale", "coef": 96.000, "country": "Ita"},
    {"team": "Borussia Dortmund", "coef": 86.000, "country": "Ger"},
    {"team": "Atlético Madrid", "coef": 85.000, "country": "Esp"},
    {"team": "RB Leipzig", "coef": 84.000, "country": "Ger"},
    {"team": "FC Porto", "coef": 81.000, "country": "Por"},
    {"team": "Arsenal", "coef": 76.000, "country": "Eng"}
]

pot_3 = [
    {"team": "Shakhtar Donetsk", "coef": 63.000, "country": "Ukr"},
    {"team": "FC Salzburg", "coef": 59.000, "country": "Aut"},
    {"team": "Dinamo Zagreb", "coef": 55.000, "country": "Cro"},
    {"team": "Glasgow Rangers", "coef": 54.000, "country": "Sco"},
    {"team": "AC Milan", "coef": 50.000, "country": "Ita"},
    {"team": "Sporting Braga", "coef": 44.000, "country": "Por"},
    {"team": "Lazio", "coef": 42.000, "country": "Ita"},
    {"team": "Red Star Belgrade", "coef": 42.000, "country": "Srb"}
]

pot_4 = [
    {"team": "FC København", "coef": 40.500, "country": "Den"},
    {"team": "Young Boys", "coef": 34.500, "country": "Sui"},
    {"team": "Real Sociedad", "coef": 33.000, "country": "Esp"},
    {"team": "Galatasaray", "coef": 31.500, "country": "Tur"},
    {"team": "Celtic", "coef": 31.000, "country": "Sco"},
    {"team": "Newcastle United", "coef": 21.914, "country": "Eng"},
    {"team": "Union Berlin", "coef": 17.000, "country": "Ger"},
    {"team": "RC Lens", "coef": 12.232, "country": "Fra"}
]

# Function to assign a color to a group
def assign_color(group_number):
    return "red" if group_number < 5 else "blue"

# Function to simulate the group stage draw
def simulate_draw():
    groups = {}

    pot_groups = [pot_1, pot_2, pot_3, pot_4]
    group_colors = ["red", "red", "red", "red", "blue", "blue", "blue", "blue"]
    group_names = ["Group A", "Group B", "Group C", "Group D", "Group E", "Group F", "Group G", "Group H"]

    # Shuffle the teams from each pot into the groups one
    for pot in pot_groups:
        random.shuffle(pot)

    assigned_teams = []

    # Assign teams to groups, ensuring constraints are met
    # The code `for group_name, color in zip(group_names, group_colors):` is iterating over two lists,
    # `group_names` and `group_colors`, simultaneously.
    for group_name, color in zip(group_names, group_colors):
        group_teams = []

        for pot in pot_groups:
            for team in pot:
                if team["team"] not in assigned_teams:
                    group_teams.append(team)
                    assigned_teams.append(team["team"])
                    break

        groups[group_name] = {
            "color": color,
            "teams": group_teams
        }

    return groups




# Main function to run the simulation
def main():
    print("Simulating Champions League Group Stage Draw for the 2023/2024 season...\n")
    groups = simulate_draw()

    # Display the result
    for group, data in groups.items():
        teams = ", ".join([team["team"] for team in data["teams"]])
        color = data["color"]
        print(f"{group} ({color}): {teams}")

if __name__ == "__main__":
    main()
