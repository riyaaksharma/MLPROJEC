import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from exception import CustomException
from logger import logging
import pandas as pd
from src.components import data_ingestion


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass 
# @dataclass automatically creates the __init__() method so you don't have to write it manually.

# It also creates a readable string version (__str__()) of the object so you can easily print and see its values.

# ✅ Saves time
# ✅ Makes code cleaner
# ✅ Perfect for config classes in ML projects!

class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv") #For storing the training data

    test_data_path: str=os.path.join('artifacts',"test.csv")# For storing the test data

    raw_data_path: str=os.path.join('artifacts',"data.csv") #For storing raw/original data

class DataIndegstion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #in this we are calling the above 3 paths and saving it to a variable

    def initiatie_data_ingestion(self):
        logging.info("Entered the data indegstion method or component")
        try:
            df = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\MLPro1\notebook\data\stud.csv')
            logging.info('Read dataset as dataframe') 

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Indegstion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:

            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIndegstion()
    obj.initiatie_data_ingestion()
