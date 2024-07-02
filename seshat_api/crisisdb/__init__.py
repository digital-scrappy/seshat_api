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

class USLocations(BaseAPICall):
    ENDPOINT = "/crisisdb/us-locations"
    SINGLE_MODEL = USLocation


class USViolenceDataSources(BaseAPICall):
    ENDPOINT = "/crisisdb/us-violence-data-sources"
    SINGLE_MODEL = USViolenceDataSource


class CrisisConsequences(BaseAPICall):
    ENDPOINT = "/crisisdb/crisis-consequences"
    SINGLE_MODEL = CrisisConsequence


class PowerTransitions(BaseAPICall):
    ENDPOINT = "/crisisdb/power-transitions"
    SINGLE_MODEL = PowerTransition


class HumanSacrifices(BaseAPICall):
    ENDPOINT = "/crisisdb/human-sacrifices"
    SINGLE_MODEL = HumanSacrifice


class ExternalConflicts(BaseAPICall):
    ENDPOINT = "/crisisdb/external-conflicts"
    SINGLE_MODEL = ExternalConflict


class ExternalConflictSides(BaseAPICall):
    ENDPOINT = "/crisisdb/external-conflict-sides"
    SINGLE_MODEL = ExternalConflictSide


class AgriculturalPopulationsArableLands(BaseAPICall):
    ENDPOINT = "/crisisdb/agricultural-populationsarable-lands"
    SINGLE_MODEL = AgriculturalPopulationArableLand


class GrossGrainSharedPerAgriculturalPopulation(BaseAPICall):
    ENDPOINT = "/crisisdb/gross-grain-shared-per-agricultural-populations"
    SINGLE_MODEL = GrossGrainSharedPerAgriculturalPopulation


class NetGrainSharedPerAgriculturalPopulation(BaseAPICall):
    ENDPOINT = "/crisisdb/net-grain-shared-per-agricultural-populations"
    SINGLE_MODEL = NetGrainSharedPerAgriculturalPopulation


class MilitaryExpenses(BaseAPICall):
    ENDPOINT = "/crisisdb/military-expenses"
    SINGLE_MODEL = MilitaryExpense


class SilverInflows(BaseAPICall):
    ENDPOINT = "/crisisdb/silver-inflows"
    SINGLE_MODEL = SilverInflow


class SilverStocks(BaseAPICall):
    ENDPOINT = "/crisisdb/silver-stocks"
    SINGLE_MODEL = SilverStock


class TotalPopulations(BaseAPICall):
    ENDPOINT = "/crisisdb/total-populations"
    SINGLE_MODEL = TotalPopulation


class GDPPerCapitas(BaseAPICall):
    ENDPOINT = "/crisisdb/gdp-per-capitas"
    SINGLE_MODEL = GDPPerCapita


class DroughtEvents(BaseAPICall):
    ENDPOINT = "/crisisdb/drought-events"
    SINGLE_MODEL = DroughtEvent


class LocustEvents(BaseAPICall):
    ENDPOINT = "/crisisdb/locust-events"
    SINGLE_MODEL = LocustEvent


class SocioeconomicTurmoilEvents(BaseAPICall):
    ENDPOINT = "/crisisdb/socioeconomic-turmoil-events"
    SINGLE_MODEL = SocioeconomicTurmoilEvent


class CropFailureEvents(BaseAPICall):
    ENDPOINT = "/crisisdb/crop-failure-events"
    SINGLE_MODEL = CropFailureEvent


class FamineEvents(BaseAPICall):
    ENDPOINT = "/crisisdb/famine-events"
    SINGLE_MODEL = FamineEvent


class DiseaseOutbreaks(BaseAPICall):
    ENDPOINT = "/crisisdb/disease-outbreaks"
    SINGLE_MODEL = DiseaseOutbreak
