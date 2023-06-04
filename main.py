from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity.config_entity import DataIngestionConfig

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
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config)
          print(data_ingestion_config.to_dict())
     except Exception as e:
          print(e)
