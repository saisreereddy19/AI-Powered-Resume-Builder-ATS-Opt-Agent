from pydantic import BaseModel

# For scoring request
class ScoreRequest(BaseModel):
    resume_text: str
    job_desc: str


# For enhancement request
class EnhanceRequest(BaseModel):
    resume_text: str
    job_desc: str
    template_name: str | None = None   # e.g., "altacv"
from pydantic import BaseModel

class ScoreRequest(BaseModel):
    resume_text: str
    job_desc: str

class EnhanceRequest(BaseModel):
    resume_text: str
    job_desc: str
