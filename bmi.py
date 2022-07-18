# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np


#Running the command to upload the dataset
from google.colab import files
uploaded=files.upload()


data=pd.read_json('data.json')
data.to_csv('data_csv_format.csv')
data_csv=pd.read_csv('data_csv_format.csv')
data_csv.head()


data_csv['BMI']=data_csv['WeightKg']/((data_csv['HeightCm']/100)*(data_csv['HeightCm']/100))


data_csv['weightcategory']=np.select(
    [data_csv['BMI'].between(0,18.5,inclusive=False),
     data_csv['BMI'].between(18.5,25,inclusive=False),
     data_csv['BMI'].between(25,30,inclusive=False),
     data_csv['BMI'].between(30,35,inclusive=False),
     data_csv['BMI'].between(35,40,inclusive=False)],
     [
      'UnderWeight','Normal Weight','Over weight','Moderately obese','Severely obese'
     ],
     default='Very severely obese'
)


value='Over weight'
count=0
for i in range(len(data_csv)):
  
  if(data_csv.loc[i, "weightcategory"]==value):
    count=count+1
print(str(count)+" "+'people are'+" "+value)
