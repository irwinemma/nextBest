# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
nextbestaction_TEST = dataiku.Dataset("NEXTBESTACTION_TEST_1")
nextbestaction_TEST_df = nextbestaction_TEST.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

nba_PyTest_df = nextbestaction_TEST_df # For this sample code, simply copy input to output


# Write recipe outputs
nba_PyTest = dataiku.Dataset("NBA_PyTest")
nba_PyTest.write_with_schema(nba_PyTest_df)

