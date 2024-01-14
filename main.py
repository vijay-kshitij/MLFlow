import sys
from src import mlProject
from src.mlProject import logger
from src.mlProject.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage2_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage4_model_trainer import ModelTrainerTrainingPipeline
from src.mlProject.pipeline.stage5_model_evaluation import ModelEvaluationTrainingPipeline


Stage = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {Stage} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {Stage} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


Stage = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {Stage} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {Stage} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


Stage = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {Stage} started <<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {Stage} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


Stage = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {Stage} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {Stage} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

Stage = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {Stage} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {Stage} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e