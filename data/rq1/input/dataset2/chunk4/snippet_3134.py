#Source: https://stackoverflow.com/questions/64012754/geopandas-attributeerror-transaction-object-has-no-attribute-run-callable
from sqlalchemy import create_engine
import pandas as pd


def insert(df):
    calidades_df = df.copy()
    calidades_df.insert(loc=0, column='proceso', value=p['proceso'])
    calidades_df.insert(
        loc=len(calidades_df.columns),
        column='baja',
        value=False)

    engine = create_engine(
        "postgres://usr:pass#@localhost:5432/database"
    )
    with engine.begin() as conn:
        calidades_df.to_postgis(
            'calidades',
            conn,
            schema='ndvi',
            if_exists='append',
            index=False
            )