import pytest
import numpy as np
import pandas as pd
import steps.load_data as load_data
from deepchecks.tabular.checks import ColumnsInfo
#from deepchecks.tabular.checks import ColumnsInfo
def test_load_raw_data():
    dataset=load_data.load_raw_data()
    assert dataset.empty == False