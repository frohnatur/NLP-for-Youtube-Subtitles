import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
import pandas as pd

import sys
from streamlit import cli as stcli

if st.button('Explorative Datenanalyse der Inputdaten'):
    data = pd.read_csv('VideoStatisiken/HandOfBloodPolSubj', index_col=0)
    pr = ProfileReport(data, explorative=True)
    st_profile_report(pr)

if __name__ == "__main__":
  filename = 'ProfileReport.py'
  sys.argv = ["streamlit", "run", filename]
  sys.exit(stcli.main())
