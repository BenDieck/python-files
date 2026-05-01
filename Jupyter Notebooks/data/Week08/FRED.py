# pip install fredapi
from fredapi import Fred
import os
import json
import pandas
import matplotlib.pyplot as plt

api_key = os.environ["FRED_API_KEY"]
fred = Fred(api_key=api_key)
data = fred.get_series('SP500')
data.plot.bar()	
plt.show()