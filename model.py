import numpy as np
import pandas as pd
import pickle
#import 
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.ensemble import RandomForestRegressor


def createModule():
     df = pd.read_csv('laptop_data.csv')

     df.drop(columns = ['Unnamed: 0'],inplace = True)

     df['Ram'] = df['Ram'].str.replace('GB', '')
     df['Weight'] = df['Weight'].str.replace('kg', '')

     df['Ram'] = df['Ram'].astype('int32')
     df['Weight'] = df['Weight'].astype('float32')

     df['Touchscreen'] = df['ScreenResolution'].apply(lambda x:1 if 'Touchscreen' in x else 0)

     df['IPS'] = df['ScreenResolution'].apply(lambda x:1 if 'IPS' in x else 0)

     new = df['ScreenResolution'].str.split('x',n=1,expand = True)

     df['X_res'] = new[0]
     df['Y_res'] = new[1]

     df['Touchscreen'] = df['ScreenResolution'].apply(lambda x:1 if 'Touchscreen' in x else 0)

     df['IPS'] = df['ScreenResolution'].apply(lambda x:1 if 'IPS' in x else 0)

     new = df['ScreenResolution'].str.split('x',n=1,expand = True)

     df['X_res'] = new [0]
     df['Y_res'] = new [1]

     df['X_res'] = df['X_res'].str.replace(',','').str.findall(r'(\d+\.?\d+)').apply(lambda x:x[0])

     df['X_res'] = df['X_res'].astype('int')
     df['Y_res'] = df['Y_res'].astype('int')

     df['ppi'] = (((df['X_res']**2 + 2 + df['Y_res']**2))**0.5/df['Inches']).astype('float')

     df.drop(columns = ['ScreenResolution', 'Inches', 'X_res', 'Y_res'],inplace = True)

     df['Cpu Name'] = df['Cpu'].apply(lambda x:" ".join(x.split()[0:3]))

     def fetch_processor(text):
          if text == 'Intel Core i7' or text == 'Intel Core i5' or text == 'Intel Core i3':
               return text
          else:
               if text.split()[0] == 'Intel':
                    return 'Other Intel Processor'
               else:
                    return 'AMD Processor'

     df['Cpu brand'] = df['Cpu Name'].apply(fetch_processor)

     df.drop(columns=['Cpu','Cpu Name'],inplace = True)

     df['Memory'] = df['Memory'].astype(str).replace('\.0', '',regex=True)
     df["Memory"] = df["Memory"].str.replace('GB','')
     df["Memory"] = df["Memory"].str.replace('TB','000')
     new = df["Memory"].str.split("+",n = 1 ,expand = True)

     df["first"] = new[0]
     df["first"] = df["first"].str.strip()

     df["second"] = new[1]

     df["Layer1HDD"] = df["first"].apply(lambda x: 1 if "HDD" in x else 0)
     df["Layer1SSD"] = df["first"].apply(lambda x: 1 if "SSD" in x else 0)
     df["Layer1Hybrid"] = df["first"].apply(lambda x: 1 if "Hybrid" in x else 0)
     df["Layer1Flash_Storage"] = df["first"].apply(lambda x: 1 if "Flash Storage" in x else 0)

     df['first'] = df['first'].str.replace(r'\D', '')

     df["second"].fillna("0", inplace = True)

     df["Layer2HDD"] = df["second"].apply(lambda x: 1 if "HDD" in x else 0)
     df["Layer2SSD"] = df["second"].apply(lambda x: 1 if "SSD" in x else 0)
     df["Layer2Hybrid"] = df["second"].apply(lambda x: 1 if "Hybrid" in x else 0)
     df["Layer2Flash_Storage"] = df["second"].apply(lambda x: 1 if "Flash Storage" in x else 0)

     df['second'] = df['second'].str.replace(r'\D', '')

     df["first"] = df["first"].astype(int)
     df["second"] = df["second"].astype(int)

     df["HDD"] = (df["first"]*df["Layer1HDD"]+df["second"]*df["Layer2HDD"])
     df["SSD"] = (df["first"]*df["Layer1SSD"]+df["second"]*df["Layer2SSD"])
     df["Hybrid"] = (df["first"]*df["Layer1Hybrid"]+df["second"]*df["Layer2Hybrid"])
     df["Flash_Storage"] = (df["first"]*df["Layer1Flash_Storage"]+df["second"]*df["Layer2Flash_Storage"])

     df.drop(columns = ['first', 'second', 'Layer1HDD', 'Layer1SSD', 'Layer1Hybrid', 'Layer1Flash_Storage', 'Layer2HDD', 'Layer2SSD', 'Layer2Hybrid', 'Layer2Flash_Storage'],inplace= True)

     df.drop(columns = ['Memory'],inplace = True)

     df.drop(columns=['Hybrid','Flash_Storage'],inplace = True)

     df ['Gpu brand']=df['Gpu'].apply(lambda x:x.split()[0])

     df=df[df['Gpu brand'] != 'ARM']

     df.drop(columns=['Gpu'],inplace=True)

     def cat_os(inp):
          if inp == 'Windows 10' or inp == 'Windows 7' or inp == 'Windows 10 s':
               return 'Windows'
          elif inp == 'macOS' or inp == 'Mach OS X':
               return 'Mac'
          else:
               return 'Others/No OS/Linux'

     df['os'] = df['OpSys'].apply(cat_os)

     df.drop(columns = ['OpSys'],inplace=True)

     X = df.drop(columns=['Price'])
     y = np.log(df['Price'])

     from sklearn.model_selection import train_test_split
     X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.10,random_state = 2)

     step1 = ColumnTransformer(transformers=[
     ('col_tnf',OneHotEncoder(sparse = False, drop = 'first'),[0,1,7,10,11])
     ],remainder='passthrough')

     step2 = RandomForestRegressor(n_estimators = 100,
                                   random_state = 3,
                                   max_samples = 0.5,
                                   max_features = 0.75,
                                   max_depth = 15)

     pipe = Pipeline([
     ('step1',step1),
     ('step2',step2)
     ])

     pipe.fit(X_train,y_train)

     y_pred = pipe.predict(X_test)

     pickle.dump(df,open('df.csv','wb'))
     pickle.dump(pipe,open('pipe.pkl','wb'))