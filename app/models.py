import json

from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.exc import SQLAlchemyError

from app.db import Base, session


class Transaction(Base):
    __tablename__ = "transactions"

    idx = Column(Integer, primary_key=True)
    transaction_id = Column(String)
    inputs = Column(String)
    outputs = Column(String)
    amount = Column(Numeric)
    timestamp = Column(Integer)

    @staticmethod
    def save_transaction_to_db(tx_details):
        """
        Save a transaction's details to the PostgreSQL database
        :param tx_details: Dictionary with transaction details
        """
        try:
            inputs_json = json.dumps(tx_details["inputs"])
            outputs_json = json.dumps(tx_details["outputs"])

            new_transaction = Transaction(
                transaction_id=tx_details["tx_id"],
                inputs=inputs_json,
                outputs=outputs_json,
                amount=tx_details["amount"],
                timestamp=tx_details["timestamp"]
            )

            session.add(new_transaction)
            session.commit()

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error saving transaction: {e}")
