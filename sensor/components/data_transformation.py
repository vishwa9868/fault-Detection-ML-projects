from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from typing import Optional
import os,sys 
from sklearn.preprocessing import Pipeline
import pandas as pd
from sensor import utils
import numpy as np
from imblearn.combine import SMDTETomek
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler

class DataTransformation:

    def __init__(self,data_transformation_config:config_entity.DataTransformationConfig,
                    data_ingestion_artifact:artifact_entity.DataIngestionArtifact):

        try:
            self.data_transformation_config=data_transformation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise SensorException(e, sys)
    
    
    @classmethod
    def get_data_transformer_object(cls):
        try:
            simple_imputer = SimpleImputer(strategy="constant", fill_value=0)
            robust_scaler = RobustScaler()

            constant_pipeline = Pipeline(steps=[
                    ('Imputer', SimpleImputer(strategy='constant', fill_value=0)),
                    ('RobustScaler', RobustScaler())
                ])
            return pipeline
        except Exception as e:
            raise SensorException(e, sys)

    
    def initiate_data_transformation(self,) -> artifact_entity.DataTransformationArtifact:
        try:
            #reading
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv