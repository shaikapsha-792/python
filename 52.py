# Team Data
teams = [
    ("Alpha",
     ["Asha", "Rahul", "Kiran"],
     [85, 90, 95]),

    ("Beta",
     ["Arun", "Divya", "Nisha"],
     [88, 92, 90]),

    ("Gamma",
     ["Sai", "Ravi"],
     [90, 90, 90]),

    ("Delta",
     ["Anu", "Rohit", "Vikas"],
     [85, 90, 95])
]

MIN_TEAM_SIZE = 3
MAX_TEAM_SIZE = 5

valid_teams = []
invalid_teams = []

# Team Validation
for team_name, members, scores in teams:   # tuple unpacking

    member_count = len(members)

    if member_count < MIN_TEAM_SIZE \
       or member_count > MAX_TEAM_SIZE:

        invalid_teams.append(
            (team_name, "Invalid Team Size")
        )

    else:
        total_score = sum(scores)

        valid_teams.append(
            (
                team_name,
                total_score,
                scores[-1],      # final round score
                member_count
            )
        )

# Ranking with Tie Rules
ranked_teams = sorted(
    valid_teams,
    key=lambda x: (-x[1], -x[2], x[0])
)

print("LEADERBOARD")
print("-" * 40)

rank = 1

for team_name, total, final_round, size in ranked_teams:

    print(
        f"{rank}. {team_name}"
        f" | Total={total}"
        f" | Final Round={final_round}"
        f" | Members={size}"
    )

    rank += 1

print("\nINVALID TEAMS")

for team in invalid_teams:
    print(team)

# Summary Tuple
summary = (
    len(teams),
    len(valid_teams),
    len(invalid_teams)
)

# Tuple Unpacking
total_teams, valid_count, invalid_count = summary

print("\nSUMMARY")
print("Total Teams :", total_teams)
print("Valid Teams :", valid_count)
print("Invalid Teams :", invalid_count)