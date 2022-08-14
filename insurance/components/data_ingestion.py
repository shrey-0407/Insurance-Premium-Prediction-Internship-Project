from insurance.entity.config_entity import DataIngestionConfig
from insurance.entity.artifact_entity import DataIngestionArtifact
import sys,os
from insurance.exception import insuranceException
from insurance.logger import logging

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise insuranceException(e,sys)


    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise insuranceException(e,sys) from e