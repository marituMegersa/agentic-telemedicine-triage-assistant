from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.telemedicine_triage_assistant.schemas import AgenticTelemedicineTriageAssistantSessionCreate, AgenticTelemedicineTriageAssistantSessionResponse
from app.domain.telemedicine_triage_assistant.service import AgenticTelemedicineTriageAssistantService

router = APIRouter(prefix="/api/v1/telemedicine_triage_assistant", tags=["Agentic Telemedicine Triage Assistant Domain"])

@router.post("/sessions", response_model=AgenticTelemedicineTriageAssistantSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticTelemedicineTriageAssistantSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Telemedicine Triage Assistant.
    """
    return AgenticTelemedicineTriageAssistantService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticTelemedicineTriageAssistantSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticTelemedicineTriageAssistantService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
