from loadfactors import open_load_combinations, factored_max, Load
import pathlib
import numpy as np

NBCC_COMBOS = open_load_combinations(
    pathlib.Path(__file__).parents[1] / 'src' / 'loadfactors' / 'NBCC_vec_full.json'
    ) # This is perhaps not a convenient location for this...

L1 = Load(D=2.3, L=2.4, S=0.9) # Not all fields need be entered

def test_max_factored():
    assert factored_max(L1, NBCC_COMBOS) == 7.375