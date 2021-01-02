import numpy as np
import pandas as pd


def pick_civ():
    df = pd.read_csv('civs.csv')
    civs = df['Civ']

    if len(civs) > 0:
        pick = np.random.choice(civs, 1)[0]
    else:
        pick = 'ERROR: no civs fit parameters or an error has occured'

    return pick
