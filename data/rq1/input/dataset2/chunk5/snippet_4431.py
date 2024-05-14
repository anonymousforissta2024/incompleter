#Source: https://stackoverflow.com/questions/66763769/import-soundfile-as-sf-but-on-jupyter-notebook-sf-gives-nameerror
import soundfile as sf
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = sf.read(batch["file"])
    batch["speech"] = speech_array
    batch["sampling_rate"] = sampling_rate
    batch["target_text"] = batch["text"]
    return batch

timit = timit.map(speech_file_to_array_fn, remove_columns=timit.column_names["train"], num_proc=4)