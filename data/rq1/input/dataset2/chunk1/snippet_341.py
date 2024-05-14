#Source: https://stackoverflow.com/questions/77361799/attributeerror-dataframe-object-has-no-attribute-group-by
import polars as pl
df = pl.DataFrame(
    {
        "a": ["a", "b", "a", "b", "c"],
        "b": [1, 2, 1, 3, 3],
        "c": [5, 4, 3, 2, 1],
    }
)
df.group_by("a").agg(pl.col("b").sum())