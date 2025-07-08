# app/services/deal_fetcher.py
from typing import List
from ..models import Deal
from datetime import datetime

class DealFetcher:
    def fetch_deals(self) -> List[Deal]:
        # Example: Replace with DealOps API call
        return [
            Deal(id="D1", stage="Proposal Sent", last_updated=datetime.utcnow(), close_date=None)
        ]
