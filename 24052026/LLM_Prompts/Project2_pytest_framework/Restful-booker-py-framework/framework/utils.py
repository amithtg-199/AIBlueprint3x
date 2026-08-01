import uuid


def unique_string(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8]}"
