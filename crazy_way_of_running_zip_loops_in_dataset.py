import pandas as pd
import numpy as np
from tqdm import tqdm
import pandas as pd
from tqdm import tqdm
import librosa
df=pd.read_csv("/content/drive/MyDrive/kaggle/train_metadata.csv")
a=[]
for i,row in tqdm(df.iterrows()):
  data,sampling_rate=librosa.load("/content/drive/MyDrive/kaggle/train_audio/"+row["filename"])
  a.append([row["primary_label"],data])
