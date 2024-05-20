import pandas as pd
import numpy as np

from pathlib import Path


class Account():
    def __init__(self, name, init_money=0):
        self.name = name,
        self._init_money = init_money
        self.operations = pd.DataFrame()

    def load_from_csv(self, path_to_csv):
        path = Path(path_to_csv)
        assert path.is_file()
        assert path.suffix == '.csv'

        self.operations = pd.read_csv(path, sep=';')
        # todo : remplacer virgule par point dans la colonne price de la DF
        pass

    @property
    def sum(self):
        return self.operations[['Price']].sum()
