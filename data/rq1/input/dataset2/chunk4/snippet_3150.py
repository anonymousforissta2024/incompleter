#Source: https://stackoverflow.com/questions/69696035/typeerror-object-of-type-mappingproxy-is-not-json-serializable
import streamlit as st
import Controllers.ECGModel as ecgModel

def GetSourceProperty(filePath):
    ecg = ecgModel.ECG
    ecg.Source = "MIT"
    ecg.FileName = "100"
    ecg.Channel = 2
    ecg.Record = 11520000
    ecg.Time = 1800
    ecg.SampleRate = 500
    return ecg