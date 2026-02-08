import sys
import os
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.loggings import logging
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from src.utils import save_data

@dataclass
class transformation_config:
    preprocessing_path = os.path.join("artifacts","preprocessing.pkl")
    new_train_data = os.path.join("artifacts","new_train_data.csv")
    new_test_data = os.path.join("artifacts","new_test_data.csv")

class transformation_class:
    def __init__(self):
        self.transformation_var = transformation_config()

    def get_preprocessor(self):
        logging.info("Preprocessing is Started...")

        try:

            num_col = ["carat","depth","table","x","y","z"]
            cat_col = ["cut","color","clarity"]

            cut_val = ['Ideal','Premium', 'Very Good', 'Good', 'Fair']
            clarity_val = ['I1','SI2','SI1','VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
            color_val = ['D','E','F','G','H','I','J']

            num_Pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy = 'median')),
                    ("StandardScaler",StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy = "most_frequent")),
                    ("encoding",OrdinalEncoder(categories = [cut_val,color_val,clarity_val])),
                    ("StandardScaler",StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ("num_transformer",num_Pipeline,num_col),
                ("cat_transformer",cat_pipeline,cat_col)
                ]
            )

            return preprocessor
        
        except Exception as e:
            logging.info("Error occured in preprocessing pipeline")
            raise CustomException(e,sys)

    
    def initiate_data_transformation(self,train_path,test_path):
        logging.info("The Data Transformation Method Started...")
    
        try:
            logging.info("The Data is Loaded for Transformation...")
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            train_data = train_data.drop(labels=["id"],axis = 1)
            test_data = test_data.drop(labels=["id"],axis = 1)

            X_train = train_data.iloc[:,:-1]
            y_train = train_data[['price']]

            X_test = test_data.iloc[:,:-1]
            y_test = test_data[['price']]

            logging.info("The Preprocessing Method Started...")
            preprocessor = self.get_preprocessor()
            new_X_train = pd.DataFrame(preprocessor.fit_transform(X_train),columns=preprocessor.get_feature_names_out())
            new_X_test = pd.DataFrame(preprocessor.transform(X_test),columns=preprocessor.get_feature_names_out())

            new_train = pd.concat([new_X_train,y_train],axis = 1)
            new_test = pd.concat([new_X_test,y_test],axis = 1)

            new_train.to_csv(self.transformation_var.new_train_data,index = True)
            logging.info("The new_train file has been saved in artifacts folder")
            new_test.to_csv(self.transformation_var.new_test_data,index = True)
            logging.info("The new_test file has been saved in artifacts folder")

            save_data(file_path = self.transformation_var.preprocessing_path,
                      obj = preprocessor)
            logging.info("The Preprocessor.pkl file has beeen saved in artifacts folder")

            return (
                new_train,
                new_test,
                self.transformation_var.preprocessing_path
                )
        
        except Exception as e:
            logging.info("Error occured in transformation pipeline")
            raise CustomException(e,sys)
