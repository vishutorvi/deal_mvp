# app/services/summarizer.py
from ollama import chat
from typing import List

class Summarizer:
    def summarize(self, docs: List[bytes]) -> str:
        joined = "\n\n".join(d.decode() for d in docs)
        print("joined =", joined)
        response = chat(
            model="phi3:latest",
            messages=[
                {"role": "system", "content": "You are a deal assistant."},
                {"role": "user", "content": joined}
            ]
        )
        content = response.message.content
        if content is None:
          raise RuntimeError("Summarizer returned no content")
        return content
