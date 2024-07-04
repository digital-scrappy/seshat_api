from ..base_model import BaseAPICall

from ..models import (
    ResearchAssistant,
    PolityTerritory,
    PolityPopulation,
    PopulationOfTheLargestSettlement,
    SettlementHierarchy,
    AdministrativeLevel,
    ReligiousLevel,
    MilitaryLevel,
    ProfessionalMilitaryOfficer,
    ProfessionalSoldier,
    ProfessionalPriesthood,
    FullTimeBureaucrat,
    ExaminationSystem,
    MeritPromotion,
    SpecializedGovernmentBuilding,
    FormalLegalCode,
    Judge,
    Court,
    ProfessionalLawyer,
    IrrigationSystem,
    DrinkingWaterSupply,
    Market,
    FoodStorageSite,
    Road,
    Bridge,
    Canal,
    Port,
    MineOrQuarry,
    MnemonicDevice,
    NonwrittenRecord,
    WrittenRecord,
    Script,
    NonPhoneticWriting,
    PhoneticAlphabeticWriting,
    ListsTablesAndClassification,
    Calendar,
    SacredText,
    ReligiousLiterature,
    PracticalLiterature,
    History,
    Philosophy,
    ScientificLiterature,
    Fiction,
    Article,
    Token,
    PreciousMetal,
    ForeignCoin,
    IndigenousCoin,
    PaperCurrency,
    Courier,
    PostalStation,
    GeneralPostalService,
    CommunalBuilding,
    UtilitarianPublicBuilding,
    SymbolicBuilding,
    EntertainmentBuilding,
    KnowledgeOrInformationBuilding,
    OtherUtilitarianPublicBuilding,
    SpecialPurposeSite,
    CeremonialSite,
    BurialSite,
    TradingEmporium,
    Enclosure,
    LengthMeasurementSystem,
    AreaMeasurementSystem,
    VolumeMeasurementSystem,
    WeightMeasurementSystem,
    TimeMeasurementSystem,
    GeometricalMeasurementSystem,
    OtherMeasurementSystem,
    DebtAndCreditStructure,
    StoreOfWealth,
    SourceOfSupport,
    OccupationalComplexity,
    SpecialPurposeHouse,
    OtherSpecialPurposeSite,
    LargestCommunicationDistance,
    FastestIndividualCommunication,
)

__all__ = [
    "ResearchAssistants",
    "PolityTerritories",
    "PolityPopulations",
    "PopulationOfTheLargestSettlements",
    "SettlementHierarchies",
    "AdministrativeLevels",
    "ReligiousLevels",
    "MilitaryLevels",
    "ProfessionalMilitaryOfficers",
    "ProfessionalSoldiers",
    "ProfessionalPriesthoods",
    "FullTimeBureaucrats",
    "ExaminationSystems",
    "MeritPromotions",
    "SpecializedGovernmentBuildings",
    "FormalLegalCodes",
    "Judges",
    "Courts",
    "ProfessionalLawyers",
    "IrrigationSystems",
    "DrinkingWaterSupplies",
    "Markets",
    "FoodStorageSites",
    "Roads",
    "Bridges",
    "Canals",
    "Ports",
    "MinesOrQuarries",
    "MnemonicDevices",
    "NonwrittenRecords",
    "WrittenRecords",
    "Scripts",
    "NonPhoneticWritings",
    "PhoneticAlphabeticWritings",
    "ListsTablesAndClassifications",
    "Calendars",
    "SacredTexts",
    "ReligiousLiteratures",
    "PracticalLiteratures",
    "Histories",
    "Philosophies",
    "ScientificLiteratures",
    "Fictions",
    "Articles",
    "Tokens",
    "PreciousMetals",
    "ForeignCoins",
    "IndigenousCoins",
    "PaperCurrencies",
    "Couriers",
    "PostalStations",
    "GeneralPostalServices",
    "CommunalBuildings",
    "UtilitarianPublicBuildings",
    "SymbolicBuildings",
    "EntertainmentBuildings",
    "KnowledgeOrInformationBuildings",
    "OtherUtilitarianPublicBuildings",
    "SpecialPurposeSites",
    "CeremonialSites",
    "BurialSites",
    "TradingEmporia",
    "Enclosures",
    "LengthMeasurementSystems",
    "AreaMeasurementSystems",
    "VolumeMeasurementSystems",
    "WeightMeasurementSystems",
    "TimeMeasurementSystems",
    "GeometricalMeasurementSystems",
    "OtherMeasurementSystems",
    "DebtAndCreditStructures",
    "StoresOfWealth",
    "SourcesOfSupport",
    "OccupationalComplexities",
    "SpecialPurposeHouses",
    "OtherSpecialPurposeSites",
    "LargestCommunicationDistances",
    "FastestIndividualCommunications",
]


class ResearchAssistants(BaseAPICall):
    ENDPOINT = "/sc/research-assistants"
    SINGLE_MODEL = ResearchAssistant


class PolityTerritories(BaseAPICall):
    ENDPOINT = "/sc/polity-territories"
    SINGLE_MODEL = PolityTerritory


class PolityPopulations(BaseAPICall):
    ENDPOINT = "/sc/polity-populations"
    SINGLE_MODEL = PolityPopulation


class PopulationOfTheLargestSettlements(BaseAPICall):
    ENDPOINT = "/sc/population-of-the-largest-settlements"
    SINGLE_MODEL = PopulationOfTheLargestSettlement


class SettlementHierarchies(BaseAPICall):
    ENDPOINT = "/sc/settlement-hierarchies"
    SINGLE_MODEL = SettlementHierarchy


class AdministrativeLevels(BaseAPICall):
    ENDPOINT = "/sc/administrative-levels"
    SINGLE_MODEL = AdministrativeLevel


class ReligiousLevels(BaseAPICall):
    ENDPOINT = "/sc/religious-levels"
    SINGLE_MODEL = ReligiousLevel


class MilitaryLevels(BaseAPICall):
    ENDPOINT = "/sc/military-levels"
    SINGLE_MODEL = MilitaryLevel


class ProfessionalMilitaryOfficers(BaseAPICall):
    ENDPOINT = "/sc/professional-military-officers"
    SINGLE_MODEL = ProfessionalMilitaryOfficer


class ProfessionalSoldiers(BaseAPICall):
    ENDPOINT = "/sc/professional-soldiers"
    SINGLE_MODEL = ProfessionalSoldier


class ProfessionalPriesthoods(BaseAPICall):
    ENDPOINT = "/sc/professional-priesthoods"
    SINGLE_MODEL = ProfessionalPriesthood


class FullTimeBureaucrats(BaseAPICall):
    ENDPOINT = "/sc/full-time-bureaucrats"
    SINGLE_MODEL = FullTimeBureaucrat


class ExaminationSystems(BaseAPICall):
    ENDPOINT = "/sc/examination-systems"
    SINGLE_MODEL = ExaminationSystem


class MeritPromotions(BaseAPICall):
    ENDPOINT = "/sc/merit-promotions"
    SINGLE_MODEL = MeritPromotion


class SpecializedGovernmentBuildings(BaseAPICall):
    ENDPOINT = "/sc/specialized-government-buildings"
    SINGLE_MODEL = SpecializedGovernmentBuilding


class FormalLegalCodes(BaseAPICall):
    ENDPOINT = "/sc/formal-legal-codes"
    SINGLE_MODEL = FormalLegalCode


class Judges(BaseAPICall):
    ENDPOINT = "/sc/judges"
    SINGLE_MODEL = Judge


class Courts(BaseAPICall):
    ENDPOINT = "/sc/courts"
    SINGLE_MODEL = Court


class ProfessionalLawyers(BaseAPICall):
    ENDPOINT = "/sc/professional-lawyers"
    SINGLE_MODEL = ProfessionalLawyer


class IrrigationSystems(BaseAPICall):
    ENDPOINT = "/sc/irrigation-systems"
    SINGLE_MODEL = IrrigationSystem


class DrinkingWaterSupplies(BaseAPICall):
    ENDPOINT = "/sc/drinking-water-supplies"
    SINGLE_MODEL = DrinkingWaterSupply


class Markets(BaseAPICall):
    ENDPOINT = "/sc/markets"
    SINGLE_MODEL = Market


class FoodStorageSites(BaseAPICall):
    ENDPOINT = "/sc/food-storage-sites"
    SINGLE_MODEL = FoodStorageSite


class Roads(BaseAPICall):
    ENDPOINT = "/sc/roads"
    SINGLE_MODEL = Road


class Bridges(BaseAPICall):
    ENDPOINT = "/sc/bridges"
    SINGLE_MODEL = Bridge


class Canals(BaseAPICall):
    ENDPOINT = "/sc/canals"
    SINGLE_MODEL = Canal


class Ports(BaseAPICall):
    ENDPOINT = "/sc/ports"
    SINGLE_MODEL = Port


class MinesOrQuarries(BaseAPICall):
    ENDPOINT = "/sc/mines-or-quarries"
    SINGLE_MODEL = MineOrQuarry


class MnemonicDevices(BaseAPICall):
    ENDPOINT = "/sc/mnemonic-devices"
    SINGLE_MODEL = MnemonicDevice


class NonwrittenRecords(BaseAPICall):
    ENDPOINT = "/sc/nonwritten-records"
    SINGLE_MODEL = NonwrittenRecord


class WrittenRecords(BaseAPICall):
    ENDPOINT = "/sc/written-records"
    SINGLE_MODEL = WrittenRecord


class Scripts(BaseAPICall):
    ENDPOINT = "/sc/scripts"
    SINGLE_MODEL = Script


class NonPhoneticWritings(BaseAPICall):
    ENDPOINT = "/sc/non-phonetic-writings"
    SINGLE_MODEL = NonPhoneticWriting


class PhoneticAlphabeticWritings(BaseAPICall):
    ENDPOINT = "/sc/phonetic-alphabetic-writings"
    SINGLE_MODEL = PhoneticAlphabeticWriting


class ListsTablesAndClassifications(BaseAPICall):
    ENDPOINT = "/sc/lists-tables-and-classifications"
    SINGLE_MODEL = ListsTablesAndClassification


class Calendars(BaseAPICall):
    ENDPOINT = "/sc/calendars"
    SINGLE_MODEL = Calendar


class SacredTexts(BaseAPICall):
    ENDPOINT = "/sc/sacred-texts"
    SINGLE_MODEL = SacredText


class ReligiousLiteratures(BaseAPICall):
    ENDPOINT = "/sc/religious-literatures"
    SINGLE_MODEL = ReligiousLiterature


class PracticalLiteratures(BaseAPICall):
    ENDPOINT = "/sc/practical-literatures"
    SINGLE_MODEL = PracticalLiterature


class Histories(BaseAPICall):
    ENDPOINT = "/sc/histories"
    SINGLE_MODEL = History


class Philosophies(BaseAPICall):
    ENDPOINT = "/sc/philosophies"
    SINGLE_MODEL = Philosophy


class ScientificLiteratures(BaseAPICall):
    ENDPOINT = "/sc/scientific-literatures"
    SINGLE_MODEL = ScientificLiterature


class Fictions(BaseAPICall):
    ENDPOINT = "/sc/fictions"
    SINGLE_MODEL = Fiction


class Articles(BaseAPICall):
    ENDPOINT = "/sc/articles"
    SINGLE_MODEL = Article


class Tokens(BaseAPICall):
    ENDPOINT = "/sc/tokens"
    SINGLE_MODEL = Token


class PreciousMetals(BaseAPICall):
    ENDPOINT = "/sc/precious-metals"
    SINGLE_MODEL = PreciousMetal


class ForeignCoins(BaseAPICall):
    ENDPOINT = "/sc/foreign-coins"
    SINGLE_MODEL = ForeignCoin


class IndigenousCoins(BaseAPICall):
    ENDPOINT = "/sc/indigenous-coins"
    SINGLE_MODEL = IndigenousCoin


class PaperCurrencies(BaseAPICall):
    ENDPOINT = "/sc/paper-currencies"
    SINGLE_MODEL = PaperCurrency


class Couriers(BaseAPICall):
    ENDPOINT = "/sc/couriers"
    SINGLE_MODEL = Courier


class PostalStations(BaseAPICall):
    ENDPOINT = "/sc/postal-stations"
    SINGLE_MODEL = PostalStation


class GeneralPostalServices(BaseAPICall):
    ENDPOINT = "/sc/general-postal-services"
    SINGLE_MODEL = GeneralPostalService


class CommunalBuildings(BaseAPICall):
    ENDPOINT = "/sc/communal-buildings"
    SINGLE_MODEL = CommunalBuilding


class UtilitarianPublicBuildings(BaseAPICall):
    ENDPOINT = "/sc/utilitarian-public-buildings"
    SINGLE_MODEL = UtilitarianPublicBuilding


class SymbolicBuildings(BaseAPICall):
    ENDPOINT = "/sc/symbolic-buildings"
    SINGLE_MODEL = SymbolicBuilding


class EntertainmentBuildings(BaseAPICall):
    ENDPOINT = "/sc/entertainment-buildings"
    SINGLE_MODEL = EntertainmentBuilding


class KnowledgeOrInformationBuildings(BaseAPICall):
    ENDPOINT = "/sc/knowledge-or-information-buildings"
    SINGLE_MODEL = KnowledgeOrInformationBuilding


class OtherUtilitarianPublicBuildings(BaseAPICall):
    ENDPOINT = "/sc/other-utilitarian-public-buildings"
    SINGLE_MODEL = OtherUtilitarianPublicBuilding


class SpecialPurposeSites(BaseAPICall):
    ENDPOINT = "/sc/special-purpose-sites"
    SINGLE_MODEL = SpecialPurposeSite


class CeremonialSites(BaseAPICall):
    ENDPOINT = "/sc/ceremonial-sites"
    SINGLE_MODEL = CeremonialSite


class BurialSites(BaseAPICall):
    ENDPOINT = "/sc/burial-sites"
    SINGLE_MODEL = BurialSite


class TradingEmporia(BaseAPICall):
    ENDPOINT = "/sc/trading-emporia"
    SINGLE_MODEL = TradingEmporium


class Enclosures(BaseAPICall):
    ENDPOINT = "/sc/enclosures"
    SINGLE_MODEL = Enclosure


class LengthMeasurementSystems(BaseAPICall):
    ENDPOINT = "/sc/length-measurement-systems"
    SINGLE_MODEL = LengthMeasurementSystem


class AreaMeasurementSystems(BaseAPICall):
    ENDPOINT = "/sc/area-measurement-systems"
    SINGLE_MODEL = AreaMeasurementSystem


class VolumeMeasurementSystems(BaseAPICall):
    ENDPOINT = "/sc/volume-measurement-systems"
    SINGLE_MODEL = VolumeMeasurementSystem


class WeightMeasurementSystems(BaseAPICall):
    ENDPOINT = "/sc/weight-measurement-systems"
    SINGLE_MODEL = WeightMeasurementSystem


class TimeMeasurementSystems(BaseAPICall):
    ENDPOINT = "/sc/time-measurement-systems"
    SINGLE_MODEL = TimeMeasurementSystem


class GeometricalMeasurementSystems(BaseAPICall):
    ENDPOINT = "/sc/geometrical-measurement-systems"
    SINGLE_MODEL = GeometricalMeasurementSystem


class OtherMeasurementSystems(BaseAPICall):
    ENDPOINT = "/sc/other-measurement-systems"
    SINGLE_MODEL = OtherMeasurementSystem


class DebtAndCreditStructures(BaseAPICall):
    ENDPOINT = "/sc/debt-and-credit-structures"
    SINGLE_MODEL = DebtAndCreditStructure


class StoresOfWealth(BaseAPICall):
    ENDPOINT = "/sc/stores-of-wealth"
    SINGLE_MODEL = StoreOfWealth


class SourcesOfSupport(BaseAPICall):
    ENDPOINT = "/sc/sources-of-support"
    SINGLE_MODEL = SourceOfSupport


class OccupationalComplexities(BaseAPICall):
    ENDPOINT = "/sc/occupational-complexities"
    SINGLE_MODEL = OccupationalComplexity


class SpecialPurposeHouses(BaseAPICall):
    ENDPOINT = "/sc/special-purpose-houses"
    SINGLE_MODEL = SpecialPurposeHouse


class OtherSpecialPurposeSites(BaseAPICall):
    ENDPOINT = "/sc/other-special-purpose-sites"
    SINGLE_MODEL = OtherSpecialPurposeSite


class LargestCommunicationDistances(BaseAPICall):
    ENDPOINT = "/sc/largest-communication-distances"
    SINGLE_MODEL = LargestCommunicationDistance


class FastestIndividualCommunications(BaseAPICall):
    ENDPOINT = "/sc/fastest-individual-communications"
    SINGLE_MODEL = FastestIndividualCommunication
