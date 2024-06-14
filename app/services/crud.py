from app.models.table_models import Taps, Prints, Pays
from app.schemas.table_schemas import TapsCreate, PrintsCreate, PaysCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Tables():
    def __init__(self, db: Session) -> None:
        self.db = db
    
    def get_taps(self):
        try:
            return self.db.query(Taps).all()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching taps: {e}")
            return []
    
    def create_taps(self, taps: List[TapsCreate]):
        try:
            new_taps = [Taps(**tap.model_dump()) for tap in taps]
            self.db.bulk_save_objects(new_taps)
            self.db.commit()
            self.db.close()
            return new_taps
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error creating tap: {e}")
            return None
    
    def get_prints(self):
        try:
            return self.db.query(Prints).all()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching prints: {e}")
            return []

    def create_prints(self, prints: List[PrintsCreate]):
        try:
            new_prints = [Prints(**print.model_dump()) for print in prints]
            self.db.bulk_save_objects(new_prints)
            self.db.commit()
            self.db.close()
            return new_prints
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error creating print: {e}")
            return None

    def get_pays(self):
        try:
            return self.db.query(Pays).all()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching pays: {e}")
            return []

    def create_pays(self, pays: List[PaysCreate]):
        try:
            new_pays = [Pays(**pay.model_dump()) for pay in pays]
            self.db.bulk_save_objects(new_pays)
            self.db.commit()
            self.db.close()
            return new_pays
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error creating pay: {e}")
            return None