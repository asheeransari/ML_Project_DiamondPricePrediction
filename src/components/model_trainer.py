import sys
import os
import pickle
from src.exception import CustomException
from src.loggings import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from src.utils import save_data,evaluate_models


@dataclass
class model_trainer_config:
    best_model_path = os.path.join("artifacts","best_model.pkl")
    LinearRegression_model_path = os.path.join("artifacts","LinearRegression_model.pkl")
    Lasso_model_path = os.path.join("artifacts","Lasso_model.pkl")
    Ridge_model_path = os.path.join("artifacts","Ridge_model.pkl")
    ElasticNet_model_path = os.path.join("artifacts","ElasticNet_model.pkl")


class model_trainer_class:
    def __init__(self):
        self.model_trainer_var = model_trainer_config()

    
    def initiate_model_trainer(self,new_train,new_test):
        logging.info("The Model Trainer Method Started...")
    
        try:

            train = pd.DataFrame(new_train)
            test = pd.DataFrame(new_test)
            logging.info("Train and Test Data is Converted into DataFrame...")

            X_train = train.iloc[:,:-1]
            X_test = test.iloc[:,:-1]
            y_train = train['price']
            y_test = test['price']
        
            models = {
                    "LinearRegression": LinearRegression(),
                    "Lasso": Lasso(),
                    "Ridge": Ridge(),
                    "ElasticNet": ElasticNet()
            }

            logging.info("The Model Evaluation Process Started...")
            trained_models,scores = evaluate_models(X_train,X_test,y_train,y_test,models)
            logging.info("All Models has been saved...")
            
            best_model_name = max(scores, key=scores.get)
            best_model_obj = trained_models[best_model_name]
            best_score = scores[best_model_name]

            save_data(self.model_trainer_var.best_model_path, best_model_obj)
            logging.info("Best Model has been saved...")
            
            return (
                self.model_trainer_var.best_model_path,
                best_model_name,
                best_score
            )
            
    



        except Exception as e:
            logging.info("Error occured in data ingestion config")
            raise CustomException(e,sys)