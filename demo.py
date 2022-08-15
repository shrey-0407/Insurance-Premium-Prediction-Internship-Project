from insurance.pipeline.pipeline import Pipeline
from insurance.exception import insuranceException
from insurance.logger import logging
from insurance.config.configuration import Configuartion
from insurance.components.data_transformation import DataTransformation
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()