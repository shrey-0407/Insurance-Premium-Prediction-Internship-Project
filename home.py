try:
    import streamlit as st
    from multiprocessing.dummy import Pipe
    from xml.etree.ElementTree import PI
    from matplotlib.style import context
    from insurance.logger import logging
    from insurance.exception import insuranceException
    import os,sys
    from insurance.config.configuration import Configuration
    from insurance.constant import get_current_time_stamp
    from insurance.pipeline.pipeline import Pipeline
    from insurance.entity.insurancepredictor import insurancePredictor,insuranceData
    from insurance.logger import get_log_dataframe
    insurance_DATA_KEY = "insurance_data"
    MEDIAN_insurance_VALUE_KEY = "median_house_value"
    ROOT_DIR = os.getcwd()
    LOG_FOLDER_NAME = "logs"
    PIPELINE_FOLDER_NAME = "insurance"
    SAVED_MODELS_DIR_NAME = "saved_models"
    LOG_DIR = os.path.join(ROOT_DIR, LOG_FOLDER_NAME)
    PIPELINE_DIR = os.path.join(ROOT_DIR, PIPELINE_FOLDER_NAME)
    MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)


    def predict(longitude,
            latitude,
            insurance_median_age,
            total_rooms,
            total_bedrooms,
            population,
            households,
            median_income,
            ocean_proximity):

            context = {
                insurance_DATA_KEY: None,
                MEDIAN_insurance_VALUE_KEY: None
            }

        
            
            insurance_data = insuranceData(longitude=longitude,
                                    latitude=latitude,
                                    insurance_median_age=insurance_median_age,
                                    total_rooms=total_rooms,
                                    total_bedrooms=total_bedrooms,
                                    population=population,
                                    households=households,
                                    median_income=median_income,
                                    ocean_proximity=ocean_proximity,
                                    )
            insurance_df = insurance_data.get_insurance_input_data_frame()
            insurance_predictor = insurancePredictor(model_dir=MODEL_DIR)
            median_insurance_value = insurance_predictor.predict(X=insurance_df)
            context = {
                insurance_DATA_KEY: insurance_data.get_insurance_data_as_dict(),
                MEDIAN_insurance_VALUE_KEY: median_insurance_value,
            }
            st.write(context[MEDIAN_insurance_VALUE_KEY])

    st.set_page_config(page_title="Demo", page_icon="🌍")

    with st.form("my_form"):
        
        longitude = st.text_input("Longitude")
        latitude = st.text_input("Latitude")
        insurance_median_age = st.text_input("insurance Median Age")
        total_rooms = st.text_input("Total Rooms")
        total_bedrooms = st.text_input("Total Bedrooms")
        population = st.text_input("Population")
        households = st.text_input("households")
        median_income = st.text_input("Median Income")
        ocean_proximity = st.selectbox("Ocean Proximity",
                            ("<1H OCEAN","INLAND","ISLAND","NEAR BAY","NEAR OCEAN",))

        
        
        
        
        
        

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(predict(longitude,
            latitude,
            insurance_median_age,
            total_rooms,
            total_bedrooms,
            population,
            households,
            median_income,
            ocean_proximity))

except Exception as e:
    print(e)
