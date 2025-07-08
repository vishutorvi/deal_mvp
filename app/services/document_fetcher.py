# app/services/document_fetcher.py
from typing import List

class DocumentFetcher:
    def __init__(self, path="app/sample.txt"):
        self.path = path

    def fetch(self, deal_id: str) -> List[bytes]:
        return [open(self.path, "rb").read()]
