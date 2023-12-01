from app.config import settings
from app.crud.crud_base import CRUDBase
from app.schemas.scheme_vacancies import VacancyIn, VacancyOut
from app.schemas.constraint import Collections


class CRUDVacancies(CRUDBase[VacancyOut]):
    """Vacancies crud
    """


vacancies = CRUDVacancies(
    schema=VacancyIn,
    col_name=Collections.VACANCIES.value,
    db_name=settings.DB_NAME,
        )
