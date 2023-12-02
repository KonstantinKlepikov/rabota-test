from pydantic import BaseModel


class VacancyIn(BaseModel):
    """Vacancy in
    """
    vacancy_id: int | None = None
    vacplacement_id: int | None = None
    profid: int | None = None
    proftitle: str | None = None
    placeid: int | None = None
    placetitle: str | None = None
    salary_volume: int | None = None
    salary_type: bool | None = None
    directionid: int | None = None
    directiontitle: str | None = None
    stafftype: bool | None = None
    vdescription: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    is_active: bool | None = None
    salary_volume_ex: str | None = None
    clientid: int | None = None
    clientname: str | None = None
    flghot: bool | None = None
    region_id: int | None = None
    search_desc: str | None = None
    search_geo: str | None = None
    regionname: str | None = None
    stationname: str | None = None
    numentries: str | None = None
    numgeoentries: str | None = None
    baseindex: int | None = None
    flgstemmer: bool | None = None
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
