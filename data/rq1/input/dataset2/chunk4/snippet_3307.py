#Source: https://stackoverflow.com/questions/77670448/plotly-creating-charts-using-excel-data-attribute-error
import plotly.express as px
import pandas as pd
kleb = pd.read_excel("/content/skrzypce_k_bufory.xlsx")
df = px.data.kleb()
fig = px.violin(df, y="% coverage", color="Amount", violinmode='overlay', hover_data=kleb.columns)
fig.show()