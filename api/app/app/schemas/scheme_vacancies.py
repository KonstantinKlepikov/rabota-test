from typing import Any
from pydantic import BaseModel
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated


def strip_spaces(v: Any) -> str | int | float:
    if isinstance(v, str):
        return v.replace(' ', '')
    if isinstance(v, int) or isinstance(v, float):
        return v


SalaryVolume = Annotated[int, BeforeValidator(strip_spaces)]


class VacancyIn(BaseModel):
    """Vacancy in
    """
    vacancy_id: int
    vacplacement_id: int | None = None
    profid: int | None = None
    proftitle: str | None = None
    placeid: int | None = None
    placetitle: str | None = None
    salary_volume: SalaryVolume | None = None
    salary_type: int | None = None
    directionid: int | None = None
    directiontitle: str | None = None
    stafftype: int | None = None
    vdescription: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    is_active: int | None = None
    salary_volume_ex: str | None = None
    clientid: int | None = None
    clientname: str | None = None
    flghot: int | None = None
    region_id: int | None = None
    search_desc: str | None = None
    search_geo: str | None = None
    regionname: str | None = None
    stationname: str | None = None
    numentries: str | None = None
    numgeoentries: str | None = None
    baseindex: int | None = None
    flgstemmer: int | None = None
    salary_type_title: str | None = None
    salary_hour: float | None = None
    salary_day: float | None = None
    salary_week: float | None = None
    salary_month: float | None = None
    websitevacancynum: str | None = None
    titleweb: str | None = None

    class Config:
        extra = 'allow'


class VacancyOut(BaseModel):
    """"""
