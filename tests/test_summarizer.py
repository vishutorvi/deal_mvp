import pytest
from app.services.summarizer import Summarizer

class DummyResp:
    def __init__(self): self.message = type("M", (), {"content": "Hello"})
def dummy_chat(*args, **kwargs):
    return DummyResp()

@pytest.fixture(autouse=True)
def patch_chat(monkeypatch):
    import app.services.summarizer
    monkeypatch.setattr(app.services.summarizer, "chat", dummy_chat)

def test_summarize():
    summarizer = Summarizer()
    out = summarizer.summarize([b"test doc"])
    assert "Hello" in out
