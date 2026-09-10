from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.telemedicine_triage_assistant.models import AgenticTelemedicineTriageAssistantSession, AgenticTelemedicineTriageAssistantItem
from app.domain.telemedicine_triage_assistant.schemas import AgenticTelemedicineTriageAssistantSessionCreate, AgenticTelemedicineTriageAssistantItemCreate

class AgenticTelemedicineTriageAssistantService:
    @staticmethod
    def create_session(db: Session, data: AgenticTelemedicineTriageAssistantSessionCreate) -> AgenticTelemedicineTriageAssistantSession:
        db_obj = AgenticTelemedicineTriageAssistantSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticTelemedicineTriageAssistantSession:
        return db.query(AgenticTelemedicineTriageAssistantSession).filter(AgenticTelemedicineTriageAssistantSession.id == session_id).first()
