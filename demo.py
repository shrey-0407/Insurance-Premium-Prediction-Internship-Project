from insurance.pipeline.pipeline import Pipeline
from insurance.exception import insuranceException
from insurance.logger import logging
from insurance.config.configuration import Configuartion
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_validation_config = Configuartion().get_data_validation_config()
        #print(data_validation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()