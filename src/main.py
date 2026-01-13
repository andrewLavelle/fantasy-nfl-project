from data import get_data

def get_player_position():
    print("=== Select Player Position ===")
    print("[1] Quarterback")
    print("[2] Running Back")
    print("[3] Wide Receiver")
    print("[4] Tight End")
    print("[5] Kicker")
    print("[6] Defense & Special Teams")
    print("[7] Defensive Lineman")
    print("[8] Linebacker")
    print("[9] Defensive Back")

    valid_input = False
    position = int(input("Enter position [1-9]: "))
    while not valid_input:
        if position > 0 and position < 10:
            valid_input = True
        else:
            position = int(input("INVALID INPUT - Enter a valid position [1-9]: "))

    return position

def get_player_name():
    name = input("Enter player name: ")
    return name

### Entry point ###

plr_position = get_player_position()
plr_name = get_player_name()

plr_data = get_data(plr_position, plr_name)

print(plr_data)