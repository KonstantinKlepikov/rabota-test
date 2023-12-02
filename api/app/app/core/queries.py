from app.core.http_session import SessionMaker
from app.schemas.scheme_vacancies import VacancyIn


class VacanciesQuery:
    """Query extaernal api for vacancies

    Atrs:
        session (SessionMaker): aiohttp session
        url (str): url for entry query
    """
    def __init__(
        self,
        session: SessionMaker,
        url: str,
            ) -> None:
        self.session = session
        self.url = url

    async def query_vacancies(self) -> list[VacancyIn]:
        """Request for vacancies

        Args:
            db (ClientSession): session

        Returns:
            list[VacancyIn]: validated query
        """
        response = await self.session.get_query(url=self.url)
        return [VacancyIn(**res) for res in response]
