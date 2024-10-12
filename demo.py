from us_visa.pipline.training_pipeline import TrainPipeline

from us_visa.logger import logging

logging.info("Welcome to logs")

obj = TrainPipeline()
obj.run_pipeline()