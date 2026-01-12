def get_player_position():
    print("=== Select Player Position")
    print("[1] Quarterback (QB)")
    print("[2] Running Back (RB)")
    print("[3] Wide Receiver (WR)")
    print("[4] Tight End (TE)")
    print("[5] Kicker (K)")
    print("[6] Defense & Special Teams (DST)")
    print("[7] Defensive Lineman (DL)")
    print("[8] Linebacker (LB)")
    print("[9] Defensive Back (DB)")

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

position = get_player_position()

player_name = get_player_name()

print(position)