from src import mlProject
from src.mlProject import logger
from src.mlProject.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline


Stage = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {Stage} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {Stage} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e