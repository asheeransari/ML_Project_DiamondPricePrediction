import sys
import os
from src.exception import CustomException
from src.loggings import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd

@dataclass
class ingestion_config:
    raw_data = os.path.join("artifacts","raw_data")
    train_data = os.path.join("artifacts","train_data.csv")
    test_data = os.path.join("artifacts","test_data.csv")


class ingestion_class:
    def __init__(self):
        self.ingestion_var = ingestion_config()
    
    def initiate_data_ingestion(self):
        logging.info("The Data Ingestion Method Started...")
    
        try:

            data = pd.read_csv(os.path.join("notebooks/data","gemstone.csv"))
            logging.info("The data is loaded from csv")
            train_dt,test_dt = train_test_split(data,test_size = 0.20,random_state = 42)
            logging.info("The data is splited in train and test")

            raw_data_path = os.path.join(self.ingestion_var.raw_data,"raw_data.csv")

            os.makedirs(self.ingestion_var.raw_data,exist_ok = True)
            logging.info("The raw data file has been created in artifacts folder")

            data.to_csv(raw_data_path,index = True)
            logging.info("The raw_data file has been saved in artifacts folder")
            data.to_csv(self.ingestion_var.train_data,index = True)
            logging.info("The train_data file has been saved in artifacts folder")
            data.to_csv(self.ingestion_var.test_data,index = True)
            logging.info("The test_data file has been saved in artifacts folder")

            return(
                self.ingestion_var.train_data,
                self.ingestion_var.test_data
            )



        except Exception as e:
            logging.info("Error occured in data ingestion config")
            raise CustomException(e,sys)
        