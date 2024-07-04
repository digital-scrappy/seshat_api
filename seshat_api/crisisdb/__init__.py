from ..base_model import BaseAPICall

from ..models import (
    USLocation,
    USViolenceDataSource,
    CrisisConsequence,
    PowerTransition,
    HumanSacrifice,
    ExternalConflict,
    ExternalConflictSide,
    AgriculturalPopulationArableLand,
    GrossGrainSharedPerAgriculturalPopulation,
    NetGrainSharedPerAgriculturalPopulation,
    MilitaryExpense,
    SilverInflow,
    SilverStock,
    TotalPopulation,
    GDPPerCapita,
    DroughtEvent,
    LocustEvent,
    SocioeconomicTurmoilEvent,
    CropFailureEvent,
    FamineEvent,
    DiseaseOutbreak,
)

__all__ = [
    "USLocations",
    "USViolenceDataSources",
    "CrisisConsequences",
    "PowerTransitions",
    "HumanSacrifices",
    "ExternalConflicts",
    "ExternalConflictSides",
    "AgriculturalPopulationsArableLands",
    "GrossGrainSharedPerAgriculturalPopulation",
    "NetGrainSharedPerAgriculturalPopulation",
    "MilitaryExpenses",
    "SilverInflows",
    "SilverStocks",
    "TotalPopulations",
    "GDPPerCapitas",
    "DroughtEvents",
    "LocustEvents",
    "SocioeconomicTurmoilEvents",
    "CropFailureEvents",
    "FamineEvents",
    "DiseaseOutbreaks",
]


class USLocations(BaseAPICall):
    """
    A class for interacting with the US locations endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import USLocations
    >>> client = SeshatAPI()
    >>> us_locations = USLocations(client)
    """
    ENDPOINT = "/crisisdb/us-locations"
    SINGLE_MODEL = USLocation


class USViolenceDataSources(BaseAPICall):
    """
    A class for interacting with the US violence data sources endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import USViolenceDataSources
    >>> client = SeshatAPI()
    >>> us_violence_data_sources = USViolenceDataSources(client)
    """
    ENDPOINT = "/crisisdb/us-violence-data-sources"
    SINGLE_MODEL = USViolenceDataSource


class CrisisConsequences(BaseAPICall):
    """
    A class for interacting with the crisis consequences endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import CrisisConsequences
    >>> client = SeshatAPI()
    >>> crisis_consequences = CrisisConsequences(client)
    """
    ENDPOINT = "/crisisdb/crisis-consequences"
    SINGLE_MODEL = CrisisConsequence


class PowerTransitions(BaseAPICall):
    """
    A class for interacting with the power transitions endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import PowerTransitions
    >>> client = SeshatAPI()
    >>> power_transitions = PowerTransitions(client)
    """
    ENDPOINT = "/crisisdb/power-transitions"
    SINGLE_MODEL = PowerTransition


class HumanSacrifices(BaseAPICall):
    """
    A class for interacting with the human sacrifices endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import HumanSacrifices
    >>> client = SeshatAPI()
    >>> human_sacrifices = HumanSacrifices(client)
    """
    ENDPOINT = "/crisisdb/human-sacrifices"
    SINGLE_MODEL = HumanSacrifice


class ExternalConflicts(BaseAPICall):
    """
    A class for interacting with the external conflicts endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import ExternalConflicts
    >>> client = SeshatAPI()
    >>> external_conflicts = ExternalConflicts(client)
    """
    ENDPOINT = "/crisisdb/external-conflicts"
    SINGLE_MODEL = ExternalConflict


class ExternalConflictSides(BaseAPICall):
    """
    A class for interacting with the external conflict sides endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import ExternalConflictSides
    >>> client = SeshatAPI()
    >>> external_conflict_sides = ExternalConflictSides(client)
    """
    ENDPOINT = "/crisisdb/external-conflict-sides"
    SINGLE_MODEL = ExternalConflictSide


class AgriculturalPopulationsArableLands(BaseAPICall):
    """
    A class for interacting with the agricultural populations arable lands
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import AgriculturalPopulationsArableLands
    >>> client = SeshatAPI()
    >>> agricultural_populations_arable_lands = AgriculturalPopulationsArableLands(client)
    """
    ENDPOINT = "/crisisdb/agricultural-populationsarable-lands"
    SINGLE_MODEL = AgriculturalPopulationArableLand


class GrossGrainSharedPerAgriculturalPopulation(BaseAPICall):
    """
    A class for interacting with the gross grain shared per agricultural
    population endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import GrossGrainSharedPerAgriculturalPopulation
    >>> client = SeshatAPI()
    >>> gross_grain_shared_per_agricultural_population = GrossGrainSharedPerAgriculturalPopulation(client)
    """
    ENDPOINT = "/crisisdb/gross-grain-shared-per-agricultural-populations"
    SINGLE_MODEL = GrossGrainSharedPerAgriculturalPopulation


class NetGrainSharedPerAgriculturalPopulation(BaseAPICall):
    """
    A class for interacting with the net grain shared per agricultural
    population endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import NetGrainSharedPerAgriculturalPopulation
    >>> client = SeshatAPI()
    >>> net_grain_shared_per_agricultural_population = NetGrainSharedPerAgriculturalPopulation(client)
    """
    ENDPOINT = "/crisisdb/net-grain-shared-per-agricultural-populations"
    SINGLE_MODEL = NetGrainSharedPerAgriculturalPopulation


class MilitaryExpenses(BaseAPICall):
    """
    A class for interacting with the military expenses endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import MilitaryExpenses
    >>> client = SeshatAPI()
    >>> military_expenses = MilitaryExpenses(client)
    """
    ENDPOINT = "/crisisdb/military-expenses"
    SINGLE_MODEL = MilitaryExpense


class SilverInflows(BaseAPICall):
    """
    A class for interacting with the silver inflows endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import SilverInflows
    >>> client = SeshatAPI()
    >>> silver_inflows = SilverInflows(client)
    """
    ENDPOINT = "/crisisdb/silver-inflows"
    SINGLE_MODEL = SilverInflow


class SilverStocks(BaseAPICall):
    """
    A class for interacting with the silver stocks endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import SilverStocks
    >>> client = SeshatAPI()
    >>> silver_stocks = SilverStocks(client)
    """
    ENDPOINT = "/crisisdb/silver-stocks"
    SINGLE_MODEL = SilverStock


class TotalPopulations(BaseAPICall):
    """
    A class for interacting with the total populations endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import TotalPopulations
    >>> client = SeshatAPI()
    >>> total_populations = TotalPopulations(client)
    """
    ENDPOINT = "/crisisdb/total-populations"
    SINGLE_MODEL = TotalPopulation


class GDPPerCapitas(BaseAPICall):
    """
    A class for interacting with the GDP per capitas endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import GDPPerCapitas
    >>> client = SeshatAPI()
    >>> gdp_per_capitas = GDPPerCapitas(client)
    """
    ENDPOINT = "/crisisdb/gdp-per-capitas"
    SINGLE_MODEL = GDPPerCapita


class DroughtEvents(BaseAPICall):
    """
    A class for interacting with the drought events endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import DroughtEvents
    >>> client = SeshatAPI()
    >>> drought_events = DroughtEvents(client)
    """
    ENDPOINT = "/crisisdb/drought-events"
    SINGLE_MODEL = DroughtEvent


class LocustEvents(BaseAPICall):
    """
    A class for interacting with the locust events endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import LocustEvents
    >>> client = SeshatAPI()
    >>> locust_events = LocustEvents(client)
    """
    ENDPOINT = "/crisisdb/locust-events"
    SINGLE_MODEL = LocustEvent


class SocioeconomicTurmoilEvents(BaseAPICall):
    """
    A class for interacting with the socioeconomic turmoil events endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import SocioeconomicTurmoilEvents
    >>> client = SeshatAPI()
    >>> socioeconomic_turmoil_events = SocioeconomicTurmoilEvents(client)
    """
    ENDPOINT = "/crisisdb/socioeconomic-turmoil-events"
    SINGLE_MODEL = SocioeconomicTurmoilEvent


class CropFailureEvents(BaseAPICall):
    """
    A class for interacting with the crop failure events endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import CropFailureEvents
    >>> client = SeshatAPI()
    >>> crop_failure_events = CropFailureEvents(client)
    """
    ENDPOINT = "/crisisdb/crop-failure-events"
    SINGLE_MODEL = CropFailureEvent


class FamineEvents(BaseAPICall):
    """
    A class for interacting with the famine events endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import FamineEvents
    >>> client = SeshatAPI()
    >>> famine_events = FamineEvents(client)
    """
    ENDPOINT = "/crisisdb/famine-events"
    SINGLE_MODEL = FamineEvent


class DiseaseOutbreaks(BaseAPICall):
    """
    A class for interacting with the disease outbreaks endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.crisisdb import DiseaseOutbreaks
    >>> client = SeshatAPI()
    >>> disease_outbreaks = DiseaseOutbreaks(client)
    """
    ENDPOINT = "/crisisdb/disease-outbreaks"
    SINGLE_MODEL = DiseaseOutbreak
