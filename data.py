import os
import tarfile
import urllib

import pandas as pd 
df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
print(df)