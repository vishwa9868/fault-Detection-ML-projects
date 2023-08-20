from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity import confug_entity
from sensor.config import mongo_client
from sensor.component.data_ingestion import DataIngestion
from sensor.component.data_validation import Datavalidation





try:
     logging.info("Starting the test_logger_and_exception")
     result = 3/0
     print(result)
except Exception as e:
     logging.debug(str(e))
     raise SensorException(e, sys)


if __name__=="__main__":
     try:
          test_logger_and_exception()
     except Exception as e:
          print(e)

if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact = data_ingestion.intiate_data_ingestion()
          
          data_validation_config = config_entity.DataValidationConfig(training_pipeline_config)
          DataValidation(data_validation_config, data_validation_config,     
                         data_ingestion_artifact=data_ingestion_artifact)
          
          data_validation_artifact=data_validation.intiate_data_validation()
     except Exception as e:
          print(e)
