
import json

from pydantic import BaseModel

from app.providers.orchestrator import ai_orchestrator


class NoticeAssistRequest(BaseModel):
    content: str

from pydantic import BaseModel


async def analyze_notice(content: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Notice Content: {content}"},
    ]

    response, _ = await ai_orchestrator.generate_chat_with_fallback(
        messages,
        temperature=0.3,
    )

    try:
        return json.loads(response)
    except (TypeError, json.JSONDecodeError):
        return response

class NoticeAssistRequest(BaseModel):
    content: str

