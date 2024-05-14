#Source: https://stackoverflow.com/questions/69839628/attributeerror-nonetype-object-has-no-attribute-dropna
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@dataclass
class NumericColumn:
  col_name: str = None
  serie: pd.Series = None


  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    return self.serie.dropna().unique.size

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna().sum()