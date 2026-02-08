import sys
import os
from src.exception import CustomException
from src.loggings import logging
from src.utils import load_data
import pandas as pd

class prediction:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path = os.path.join("artifacts","preprocessing.pkl")
            model_path = os.path.join("artifacts","best_model.pkl")
            best_model = load_data(model_path)
            preprocessor = load_data(preprocessor_path)

            scaled_data = preprocessor.transform(features)
            pred = best_model.predict(scaled_data)
            return pred
        except Exception as e:
            raise CustomException(e,sys)
    
class customData:
    try :
        def __init__(self,
                        carat : float,
                        cut : str,
                        color : str,
                        clarity : str,
                        depth : float,
                        table : float,
                        x : float,
                        y : float,
                        z : float):
        
            self.carat = carat
            self.cut = cut
            self.color = color
            self.clarity = clarity
            self.depth = depth
            self.table = table
            self.x = x
            self.y = y
            self.z = z

        def get_data_in_df(self):
                
            data = {
                "carat": [self.carat],
                "cut": [self.cut],
                "color": [self.color],
                "clarity": [self.clarity],
                "depth": [self.depth],
                "table": [self.table],
                "x": [self.x],
                "y": [self.y],
                "z": [self.z]
            }

            new_data = pd.DataFrame(data)

            return new_data

    except Exception as e:
        raise CustomException(e,sys)