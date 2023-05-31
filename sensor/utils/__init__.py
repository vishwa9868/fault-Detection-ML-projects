import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
        logging.info("Reading data from database: {database_name} and collection: {collection_name}")
        df=pd.Dataframe(list(mongo_client[database_name][collection_nmae].find()))
        logging.info(f"Found columns: {df.columns}")
        if " _id" in df.columns:
            df = df.drop(" _id" , axis=1)
        return df
    except Exception as e:
        raise SensorException(e, sys)