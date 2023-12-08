import os
import pandas as pd
from ydata_profiling import ProfileReport

# Load the dataset
df = pd.read_fwf('data/wine.data')

if not os.path.exists('profiling'):
    os.makedirs('profiling')

# Generate the profiling report
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
profile.to_file('./profiling/report.html')
