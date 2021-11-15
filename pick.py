import numpy as np
import pandas as pd
import re


def pick_civ(msg):
    df = pd.read_csv('civs.csv')
    civs = []
    civs = np.array(civs)

    msg.lstrip()
    msg = msg.lower()
    types = msg.split()

    if len(types) > 1:
        err = 'ERROR: I can only compute one type (future feature incoming). Two word types need underscore ie: cavalry_archer'
        civs = np.append(civs, err)

    if len(types) == 1:
        rows = df.loc[(df['type1'] == types[0])]
        civs = rows['Civ'].to_numpy()

    if len(types) == 0:
        civs = df['Civ'].to_numpy()

    if len(civs) > 0:
        pick = np.random.choice(civs, 1)
    else:
        pick = 'ERROR: no civs fit parameters or an error has occurred'

    return pick

