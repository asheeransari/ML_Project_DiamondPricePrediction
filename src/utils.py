import sys
import os
from src.exception import CustomException
from src.loggings import logging
import pickle
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.metrics import r2_score

def save_data(file_path,obj):

    path = os.path.dirname(file_path)
    os.makedirs(path, exist_ok=True)
    with open(file_path, 'wb') as file:
                pickle.dump(obj, file)

logging.info("The Model Evaluation Function Started...")
def evaluate_models(X_train,X_test,y_train,y_test,models):
        try:

            scores = {}
            trained_models = {}

            for name, model in models.items():
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                r2 = r2_score(y_test, y_pred)

                scores[name] = r2
                trained_models[name] = model

                save_data(os.path.join("artifacts", f"{name}.pkl"), model)
                logging.info("The Model Evaluation Function Executed Successfully...")

            return trained_models,scores
        

        except Exception as e:
              raise CustomException(e,sys)

def load_data(path):
      with open(path,'rb') as file:
            model = pickle.load(file)
      
      return model

