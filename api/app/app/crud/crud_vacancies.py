from typing import Any
from app.config import settings
from pymongo.client_session import ClientSession
from pymongo.results import UpdateResult
from app.crud.crud_base import CRUDBase
from app.schemas.scheme_vacancies import VacancyIn, VacancyOut
from app.schemas.constraint import Collections


class CRUDVacancies(CRUDBase[VacancyOut]):
    """Vacancies crud
    """

    async def create_or_replace(
        self,
        db: ClientSession,
        obj_in: VacancyIn
            ) -> UpdateResult:
        """Replace one existed document. If not exist - create it.

        Args:
            db (ClientSession): session
            obj_in (VacancyIn): data to replace

        Returns:
            UpdateResult: result of replace
        """
        return await db.client[self.db_name][self.col_name] \
            .replace_one(
                {"vacancy_id": obj_in.vacancy_id},
                obj_in.model_dump(),
                upsert=True
                    )


vacancies = CRUDVacancies(
    schema=VacancyIn,
    col_name=Collections.VACANCIES.value,
    db_name=settings.DB_NAME,
        )
