import pandas as pd
def add_game(game):
    players = ['asa', 'jorde', 'shabha', 'brandon', 'tom']
    if len(game) > 3:
        league = game[3]
    else:
        league = ""
    csvfile = "{}chess.csv".format(league)
    df = pd.read_csv(csvfile)

    p1 = game[0].lower()
    gamestatus = game[1].lower()
    p2 = game[2].lower()
    if gamestatus == "beat":
        df.at[players.index(p1), 'p'] += 3
        df.at[players.index(p1), 'w'] += 1
        df.at[players.index(p2), 'l'] += 1
    elif gamestatus == "drew":
        df.at[players.index(p1), 'p'] += 1
        df.at[players.index(p2), 'p'] += 1
        df.at[players.index(p1), 'd'] += 1
        df.at[players.index(p2), 'd'] += 1
    df.to_csv(csvfile, index=False)
    f = open("{}chess_log.log".format(league), "a")
    f.write(game+"\n")
    f.close()

