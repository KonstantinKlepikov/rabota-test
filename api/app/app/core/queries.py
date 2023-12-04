from pymongo.client_session import ClientSession
from app.core.http_session import SessionMaker
from app.schemas.scheme_vacancies import VacancyInOut
from app.crud.crud_vacancies import vacancies


class VacanciesQuery:
    """Query extaernal api for vacancies

    Atrs:
        session (SessionMaker): aiohttp session
        url (str): url for query
    """
    def __init__(
        self,
        session: SessionMaker,
        url: str,
            ) -> None:
        self.session = session
        self.url = url

    async def query_vacancies(self) -> list[VacancyInOut]:
        """Request for vacancies

        Returns:
            list[VacancyInOut]: validated query
        """
        response = await self.session.get_query(url=self.url)
        return [VacancyInOut(**res) for res in response]

    # TODO: test me
    async def get_and_create(self, db: ClientSession) -> None:
        """Get vacancies and save it to db

        Args:
            db (ClientSession): session
        """
        r = await self.query_vacancies()
        await vacancies.create_or_replace_many(db, r)
