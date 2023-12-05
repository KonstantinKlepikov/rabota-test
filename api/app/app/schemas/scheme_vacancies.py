from typing import Any
from pydantic import BaseModel
from pydantic.functional_validators import BeforeValidator, AfterValidator
from typing_extensions import Annotated


# TODO: test me
def strip_spaces(v: Any) -> str | int | float:
    if isinstance(v, str):
        return v.replace(' ', '')
    if isinstance(v, int) or isinstance(v, float):
        return v


# TODO: test me
def get_and_words(v: list[str]) -> list[str]:
    """ This used for AND words db query
    """
    return ['"' + w + '"' for w in v]


SalaryVolume = Annotated[int, BeforeValidator(strip_spaces)]
SearchString = Annotated[list[str], AfterValidator(get_and_words)]


class VacancyInOut(BaseModel):
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
        # allow extra fields withoud validation
        extra = 'allow'

        json_schema_extra = {
            "example": {
                "vacancy_id": 1020000000001,
                "vacplacement_id": 152,
                "profid": 4,
                "proftitle": "Работник торгового зала ",
                "placeid": 143,
                "placetitle": "Уфа",
                "salary_volume": 53240,
                "salary_type": 0,
                "directionid": 2,
                "directiontitle": "Ритейл",
                "stafftype": 0,
                "vdescription": "Требуются работники торгового зала в сеть гипермаркетов ",
                "address": "Республика Башкортостан, г. Уфа, ул. Губайдуллина, д.  6",
                "latitude": 54.720907,
                "longitude": 56.000813,
                "is_active": 1,
                "salary_volume_ex": "53240 р./мес.",
                "clientid": 1770000000070,
                "clientname": "Auchan (Ашан)",
                "flghot": 1,
                "region_id": 2,
                "search_desc": "работник торгов зал сет гипермаркет сканеровщик сит ритейл аша",
                "search_geo": "республик башкортоста г. уф ул губайдуллин",
                "regionname": "Республика Башкортостан",
                "stationname": None,
                "numentries": None,
                "numgeoentries": None,
                "baseindex": 102,
                "flgstemmer": 0,
                "salary_type_title": "р./мес.",
                "salary_hour": 220.0,
                "salary_day": 2420.0,
                "salary_week": 12100.0,
                "salary_month": 53240.0,
                "websitevacancynum": "020152",
                "titleweb": None,
                    }
                }


class VacancySearchFields(BaseModel):
    """Fields for query pattern

    Use exclude_none with dumb() method to exclude
    non-values for query
    """
    profid: int | None = None
    placeid: int | None = None
    clientid: int | None = None

    class Config:

        json_schema_extra = {
            "example": {
                "profid": 4,
                "placeid": 143,
                "clientid": 1770000000070
                    }
                }


class VacancyTextSearch(VacancySearchFields):
    """Query db for vacancy pattern

    Use exclude_none with dumb() method to exclude
    non-values for query
    """
    placeid: int | None = None
    profid: int | None = None
    clientid: int | None = None
    searchstring: SearchString
