import pymongo
import pandas as pd
import json
#provide the mongo localhost url to connect python to mongodb
import os
@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str= os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secrete_key:str = os.getenv("AWS_SECRETE_ACCESS_KEY")





env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)