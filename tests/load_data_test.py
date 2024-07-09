import pytest
import numpy as np
import pandas as pd
import steps.load_data as load_data

def test_load_raw_data():
    dataset=load_data.load_raw_data()
    assert dataset.empty == False