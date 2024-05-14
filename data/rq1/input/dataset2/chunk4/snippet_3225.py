#Source: https://stackoverflow.com/questions/77073167/typeerror-expected-str-bytes-or-os-pathlike-object-not-dataframe-videoclass
import os
import pandas as pd

base_path = '/content/drive/MyDrive/Shoplifting Dataset (2022) - CV Laboratory MNNIT Allahabad/Shoplifting Dataset (2022) - CV Laboratory MNNIT Allahabad/Dataset/Dataset/'

normal_path = os.path.join(base_path, 'Normal')
shoplifting_path = os.path.join(base_path, 'Shoplifting')

if os.path.exists(normal_path) and os.path.exists(shoplifting_path):
    normal_files = [os.path.join(normal_path, filename) for filename in os.listdir(normal_path) if filename.endswith('.mp4')]
    shoplifting_files = [os.path.join(shoplifting_path, filename) for filename in os.listdir(shoplifting_path) if filename.endswith('.mp4')]

    # Create label lists
    normal_labels = [0] * len(normal_files)
    shoplifting_labels = [1] * len(shoplifting_files)

    # Combine the lists of paths and labels
    all_files = normal_files + shoplifting_files
    all_labels = normal_labels + shoplifting_labels

    # Create a DataFrame
    data = {'Video_Path': all_files, 'Label': all_labels}
    df = pd.DataFrame(data)

    # Print the first 5 rows
    print(df.head())
else:
    print(f"One or both of the directories '{normal_path}' and '{shoplifting_path}' do not exist.")



from sklearn.model_selection import train_test_split
train_df, val_df = train_test_split(df, test_size=0.25)