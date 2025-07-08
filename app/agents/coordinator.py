# app/agents/coordinator.py
from ..services.deal_fetcher import DealFetcher
from ..services.document_fetcher import DocumentFetcher
from ..services.summarizer import Summarizer
from ..services.task_service import TaskService
from ..interfaces import IDealCoordinator

class DealCoordinator(IDealCoordinator):
    def __init__(self):
        self.fetcher = DealFetcher()
        self.doc_fetcher = DocumentFetcher()
        self.summarizer = Summarizer()
        self.task_srv = TaskService()

    def run(self):
        for deal in self.fetcher.fetch_deals():
            docs = self.doc_fetcher.fetch(deal.id)
            summary = self.summarizer.summarize(docs)
            # Naive rule: always create a follow-up task
            desc = f"Summary for {deal.id}: {summary[:100]}..."
            self.task_srv.create_task(deal.id, desc)
