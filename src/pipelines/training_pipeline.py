import sys
import os
from src.exception import CustomException
from src.loggings import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd
from src.components.data_ingestion import ingestion_class
from src.components.data_transformation import transformation_class
from src.components.model_trainer import model_trainer_class



def main():
    ingestion_class_obj = ingestion_class()
    train,test = ingestion_class_obj.initiate_data_ingestion()
    transformation_class_obj = transformation_class()
    new_train,new_test,preprocessor_path = transformation_class_obj.initiate_data_transformation(train,test)
    model_trainer_class_obj = model_trainer_class()
    best_model_path,best_model,best_accuracy = model_trainer_class_obj.initiate_model_trainer(new_train,new_test)
    result = f"The Best Model is : {best_model} with {best_accuracy}"
    return result

if __name__ == "__main__":
    result = main()
    print(result)

    

