from app.models.meeting_room import MeetingRoom
from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.base import CRUDBase


class CRUDMeetingRoom(CRUDBase):

    async def get_room_id_by_name(
            self,
            room_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(self.model.id).where(
                self.model.name == room_name
            )
        )
        return db_room_id.scalars().first()


meeting_room_crud = CRUDMeetingRoom(MeetingRoom)
