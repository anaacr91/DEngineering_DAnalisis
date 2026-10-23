player_goals = {
    "Raúl": 25,
    "Rivaldo": 18,
    "Morientes": 19,
}


def display_goals(player):
    try:
        goals_number = player_goals[player]
    except KeyError:
        print("¡Player was not found!")
    else:
        print("Goals number is: " + str(goals_number))


if __name__ == "__main__":
    display_goals("Messi")
    display_goals("Raúl")
