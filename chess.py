import pandas as pd
def add_game(game):
    players = ['asa', 'jorde', 'shabha', 'brandon', 'tom']
    l = game.split(" ")
    if len(l) > 3:
        league = l[3]
    else:
        league = ""
    csvfile = "{}chess.csv".format(league)
    df = pd.read_csv(csvfile)
    if l[1] == "beat":
        df.at[players.index(l[0]), 'p'] += 3
        df.at[players.index(l[0]), 'w'] += 1
        df.at[players.index(l[2]), 'l'] += 1
    if l[1] == "drew":
        df.at[players.index(l[0]), 'p'] += 1
        df.at[players.index(l[2]), 'p'] += 1
        df.at[players.index(l[0]), 'd'] += 1
        df.at[players.index(l[2]), 'd'] += 1
    df.to_csv(csvfile, index=False)
    f = open("{}chess_log.log".format(league), "a")
    f.write(game+"\n")
    f.close()

