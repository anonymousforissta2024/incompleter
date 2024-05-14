#Source: https://stackoverflow.com/questions/58032310/pandas-resample-raises-type-error-for-index-consisting-of-datetime-objects
# %%
import pandas as pd
print(f"pandas version: {pd.__version__}\n\n")

data = pd.DataFrame({"created": ['2019-03-07T11:01:07.361+0000',
                                 '2019-06-05T15:09:51.203+0100',
                                 '2019-06-05T15:09:51.203+0100'],
                     "value": [10, 20, 30]})

# %%
print(f"original type: {type(data.created[0])}\n")
data.info()

# %%
data.created = pd.to_datetime(data.created)

# %%
print(f"updated type: {type(data.created[0])}\n")
data.info()

# %%
data.set_index("created", inplace=True)
data.info()

# %%
data.resample("D").mean()