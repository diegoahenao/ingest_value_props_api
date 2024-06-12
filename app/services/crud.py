from app.models.table_models import Taps, Prints, Pays
from app.schemas.table_schemas import TapsCreate, PrintsCreate, PaysCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging

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
    
    def create_tap(self, tap: TapsCreate):
        try:
            new_tap = Taps(**tap.model_dump())
            self.db.add(new_tap)
            self.db.commit()
            self.db.refresh(new_tap)
            self.db.close()
            return new_tap
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

    def create_print(self, print: PrintsCreate):
        try:
            new_print = Prints(**print.model_dump())
            self.db.add(new_print)
            self.db.commit()
            self.db.refresh(new_print)
            self.db.close()
            return new_print
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

    def create_pay(self, pay: PaysCreate):
        try:
            new_pay = Pays(**pay.model_dump())
            self.db.add(new_pay)
            self.db.commit()
            self.db.refresh(new_pay)
            self.db.close()
            return new_pay
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error creating pay: {e}")
            return None