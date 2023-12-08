import pandas as pd
from ydata_profiling import ProfileReport

# Load the dataset
df = pd.read_csv('data/wine.data')

# Generate the profiling report
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)

# Save the report
profile.to_file('./profiling/report.html')
