import asyncio
from pymongo.client_session import ClientSession
from pymongo.results import UpdateResult
from app.crud.crud_base import CRUDBase
from app.schemas.scheme_vacancies import VacancyInOut, VacancyTextSearch
from app.schemas.constraint import Collections
from app.config import settings


class CRUDVacancies(CRUDBase[VacancyInOut]):
    """Vacancies crud
    """
    # TODO: test me
    async def create_or_replace(
        self,
        db: ClientSession,
        obj_in: VacancyInOut
            ) -> UpdateResult:
        """Replace one existed document. If not exist - creates it.

        Args:
            db (ClientSession): session
            obj_in (VacancyInOut): data to replace

        Returns:
            UpdateResult: result of replace
        """
        return await db.client[self.db_name][self.col_name] \
            .replace_one(
                {"vacancy_id": obj_in.vacancy_id},
                obj_in.model_dump(),
                upsert=True
                    )

    # TODO: test me
    async def create_or_replace_many(
        self,
        db: ClientSession,
        obj_in: list[VacancyInOut]
            ) -> list[UpdateResult]:
        """Replace many existed documents. If not exist - creates them.
        Args:
            db (ClientSession): session
            obj_in (list[VacancyInOut]): data to replace

        Returns:
            list[UpdateResult]: result of replace
        """
        tasks = [self.create_or_replace(db, i) for i in obj_in]
        result = await asyncio.gather(*tasks, return_exceptions=True)
        return [res for res in result if not isinstance(res, Exception)]

    # TODO: test me
    async def text_search(
        self,
        db: ClientSession,
        obj_in: VacancyTextSearch
            ) -> list[VacancyInOut]:
        """_summary_

        Args:
            db (ClientSession): session
            obj_in (VacancyTextSearch): search parameters

        Returns:
            list[VacancyInOut]: search result
        """
        q = obj_in.model_dump(exclude_none=True, exclude=('searchstring', ))
        t = {"$text": {"$search": ' '.join(obj_in.searchstring)}}
        q.update(t)
        result = []
        async for res in db.client[self.db_name][self.col_name].find(q):
            del res['_id']
            result.append(VacancyInOut(**res))
        return result


vacancies = CRUDVacancies(
    schema=VacancyInOut,
    col_name=Collections.VACANCIES.value,
    db_name=settings.DB_NAME,
        )
