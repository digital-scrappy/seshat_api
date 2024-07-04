from ..base_model import BaseAPICall

from ..models import (
    PolityResearchAssistant,
    PolityOriginalName,
    PolityAlternativeName,
    PolityDuration,
    PolityPeakYear,
    PolityDegreeOfCentralization,
    PolitySuprapolity,
    PolityUTMTimezone,
    PolityCapital,
    PolityLanguage,
    PolityLinguisticFamily,
    PolityLanguageGenus,
    PolityReligionGenus,
    PolityReligionFamily,
    PolityReligion,
    PolityRelationshipToPrecedingEntity,
    PolityPrecedingEntity,
    PolitySucceedingEntity,
    PolitySupraculturalEntity,
    PolityScaleOfSupraculturalInteraction,
    PolityAlternateReligionGenus,
    PolityAlternateReligionFamily,
    PolityAlternateReligion,
    PolityExpert,
    PolityEditor,
    PolityReligiousTradition,
)

__all__ = [
    "PolityResearchAssistants",
    "PolityOriginalNames",
    "PolityAlternativeNames",
    "PolityDurations",
    "PolityPeakYears",
    "PolityDegreeOfCentralizations",
    "PolitySuprapolities",
    "PolityUTMTimezones",
    "PolityCapitals",
    "PolityLanguages",
    "PolityLinguisticFamilies",
    "PolityLanguageGenuses",
    "PolityReligionGenuses",
    "PolityReligionFamilies",
    "PolityReligions",
    "PolityRelationshipToPrecedingEntities",
    "PolityPrecedingEntities",
    "PolitySucceedingEntities",
    "PolitySupraculturalEntities",
    "PolityScaleOfSupraculturalInteractions",
    "PolityAlternateReligionGenuses",
    "PolityAlternateReligionFamilies",
    "PolityAlternateReligions",
    "PolityExperts",
    "PolityEditors",
    "PolityReligiousTraditions",
]


class PolityResearchAssistants(BaseAPICall):
    ENDPOINT = "/general/polity-research-assistants"
    SINGLE_MODEL = PolityResearchAssistant


class PolityOriginalNames(BaseAPICall):
    ENDPOINT = "/general/polity-original-names"
    SINGLE_MODEL = PolityOriginalName


class PolityAlternativeNames(BaseAPICall):
    ENDPOINT = "/general/polity-alternative-names"
    SINGLE_MODEL = PolityAlternativeName


class PolityDurations(BaseAPICall):
    ENDPOINT = "/general/polity-durations"
    SINGLE_MODEL = PolityDuration


class PolityPeakYears(BaseAPICall):
    ENDPOINT = "/general/polity-peak-years"
    SINGLE_MODEL = PolityPeakYear


class PolityDegreeOfCentralizations(BaseAPICall):
    ENDPOINT = "/general/polity-degree-of-centralizations"
    SINGLE_MODEL = PolityDegreeOfCentralization


class PolitySuprapolities(BaseAPICall):
    ENDPOINT = "/general/polity-suprapolities"
    SINGLE_MODEL = PolitySuprapolity


class PolityUTMTimezones(BaseAPICall):
    ENDPOINT = "/general/polity-utm-timezones"
    SINGLE_MODEL = PolityUTMTimezone


class PolityCapitals(BaseAPICall):
    ENDPOINT = "/general/polity-capitals"
    SINGLE_MODEL = PolityCapital


class PolityLanguages(BaseAPICall):
    ENDPOINT = "/general/polity-languages"
    SINGLE_MODEL = PolityLanguage


class PolityLinguisticFamilies(BaseAPICall):
    ENDPOINT = "/general/polity-linguistic-families"
    SINGLE_MODEL = PolityLinguisticFamily


class PolityLanguageGenuses(BaseAPICall):
    ENDPOINT = "/general/polity-language-genuses"
    SINGLE_MODEL = PolityLanguageGenus


class PolityReligionGenuses(BaseAPICall):
    ENDPOINT = "/general/polity-religion-genuses"
    SINGLE_MODEL = PolityReligionGenus


class PolityReligionFamilies(BaseAPICall):
    ENDPOINT = "/general/polity-religion-families"
    SINGLE_MODEL = PolityReligionFamily


class PolityReligions(BaseAPICall):
    ENDPOINT = "/general/polity-religions"
    SINGLE_MODEL = PolityReligion


class PolityRelationshipToPrecedingEntities(BaseAPICall):
    ENDPOINT = "/general/polity-relationship-to-preceding-entities"
    SINGLE_MODEL = PolityRelationshipToPrecedingEntity


class PolityPrecedingEntities(BaseAPICall):
    ENDPOINT = "/general/polity-preceding-entities"
    SINGLE_MODEL = PolityPrecedingEntity


class PolitySucceedingEntities(BaseAPICall):
    ENDPOINT = "/general/polity-succeeding-entities"
    SINGLE_MODEL = PolitySucceedingEntity


class PolitySupraculturalEntities(BaseAPICall):
    ENDPOINT = "/general/polity-supracultural-entities"
    SINGLE_MODEL = PolitySupraculturalEntity


class PolityScaleOfSupraculturalInteractions(BaseAPICall):
    ENDPOINT = "/general/polity-scale-of-supracultural-interactions"
    SINGLE_MODEL = PolityScaleOfSupraculturalInteraction


class PolityAlternateReligionGenuses(BaseAPICall):
    ENDPOINT = "/general/polity-alternate-religion-genuses"
    SINGLE_MODEL = PolityAlternateReligionGenus


class PolityAlternateReligionFamilies(BaseAPICall):
    ENDPOINT = "/general/polity-alternate-religion-families"
    SINGLE_MODEL = PolityAlternateReligionFamily


class PolityAlternateReligions(BaseAPICall):
    ENDPOINT = "/general/polity-alternate-religions"
    SINGLE_MODEL = PolityAlternateReligion


class PolityExperts(BaseAPICall):
    ENDPOINT = "/general/polity-experts"
    SINGLE_MODEL = PolityExpert


class PolityEditors(BaseAPICall):
    ENDPOINT = "/general/polity-editors"
    SINGLE_MODEL = PolityEditor


class PolityReligiousTraditions(BaseAPICall):
    ENDPOINT = "/general/polity-religious-traditions"
    SINGLE_MODEL = PolityReligiousTradition
