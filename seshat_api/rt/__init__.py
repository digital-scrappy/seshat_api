from ..base_model import BaseAPICall

from ..models import (
    WidespreadReligion,
    OfficialReligion,
    ElitesReligion,
    TheologicalSyncretismOfDifferentReligion,
    SyncretismOfReligiousPracticesAtTheLevelOfIndividualBeliever,
    ReligiousFragmentation,
    FrequencyOfGovernmentalViolenceAgainstReligiousGroup,
    GovernmentRestrictionsOnPublicWorship,
    GovernmentRestrictionsOnPublicProselytizing,
    GovernmentRestrictionsOnConversion,
    GovernmentPressureToConvert,
    GovernmentRestrictionsOnPropertyOwnershipForAdherentsOfAndReligiousGroup,
    TaxesBasedOnReligiousAdherenceOrOnReligiousActivityAndInstitution,
    GovernmentalObligationsForReligiousGroupToApplyForOfficialRecognition,
    GovernmentRestrictionsOnConstructionOfReligiousBuilding,
    GovernmentRestrictionsOnReligiousEducation,
    GovernmentRestrictionsOnCirculationOfReligiousLiterature,
    GovernmentDiscriminationAgainstReligiousGroupTakingUpCertainOccupationOrFunction,
    FrequencyOfSocietalViolenceAgainstReligiousGroup,
    SocietalDiscriminationAgainstReligiousGroupTakingUpCertainOccupationOrFunction,
    SocietalPressureToConvertOrAgainstConversion,
)

class WidespreadReligions(BaseAPICall):
    ENDPOINT = "/rt/widespread-religions"
    SINGLE_MODEL = WidespreadReligion


class OfficialReligions(BaseAPICall):
    ENDPOINT = "/rt/official-religions"
    SINGLE_MODEL = OfficialReligion


class ElitesReligions(BaseAPICall):
    ENDPOINT = "/rt/elites-religions"
    SINGLE_MODEL = ElitesReligion


class TheologicalSyncretismOfDifferentReligions(BaseAPICall):
    ENDPOINT = "/rt/theological-syncretism-of-different-religions"
    SINGLE_MODEL = TheologicalSyncretismOfDifferentReligion


class SyncretismOfReligiousPracticesAtTheLevelOfIndividualBelievers(
    BaseAPICall
):
    ENDPOINT = "/rt/syncretism-of-religious-practices-at-the-level-of-individual-believers"
    SINGLE_MODEL = SyncretismOfReligiousPracticesAtTheLevelOfIndividualBeliever


class ReligiousFragmentations(BaseAPICall):
    ENDPOINT = "/rt/religious-fragmentations"
    SINGLE_MODEL = ReligiousFragmentation


class FrequencyOfGovernmentalViolenceAgainstReligiousGroups(BaseAPICall):
    ENDPOINT = (
        "/rt/frequency-of-governmental-violence-against-religious-groups"
    )
    SINGLE_MODEL = FrequencyOfGovernmentalViolenceAgainstReligiousGroup


class GovernmentRestrictionsOnPublicWorships(BaseAPICall):
    ENDPOINT = "/rt/government-restrictions-on-public-worships"
    SINGLE_MODEL = GovernmentRestrictionsOnPublicWorship


class GovernmentRestrictionsOnPublicProselytizings(BaseAPICall):
    ENDPOINT = "/rt/government-restrictions-on-public-proselytizings"
    SINGLE_MODEL = GovernmentRestrictionsOnPublicProselytizing


class GovernmentRestrictionsOnConversions(BaseAPICall):
    ENDPOINT = "/rt/government-restrictions-on-conversions"
    SINGLE_MODEL = GovernmentRestrictionsOnConversion


class GovernmentPressureToConverts(BaseAPICall):
    ENDPOINT = "/rt/government-pressure-to-converts"
    SINGLE_MODEL = GovernmentPressureToConvert


class GovernmentRestrictionsOnPropertyOwnershipForAdherentsOfAndReligiousGroups(
    BaseAPICall
):
    ENDPOINT = "/rt/government-restrictions-on-property-ownership-for-adherents-of-and-religious-groups"
    SINGLE_MODEL = GovernmentRestrictionsOnPropertyOwnershipForAdherentsOfAndReligiousGroup


class TaxesBasedOnReligiousAdherenceOrOnReligiousActivitiesAndInstitutions(
    BaseAPICall
):
    ENDPOINT = "/rt/taxes-based-on-religious-adherence-or-on-religious-activities-and-institutions"
    SINGLE_MODEL = (
        TaxesBasedOnReligiousAdherenceOrOnReligiousActivityAndInstitution
    )


class GovernmentalObligationsForReligiousGroupsToApplyForOfficialRecognitions(
    BaseAPICall
):
    ENDPOINT = "/rt/governmental-obligations-for-religious-groups-to-apply-for-official-recognitions"
    SINGLE_MODEL = (
        GovernmentalObligationsForReligiousGroupToApplyForOfficialRecognition
    )


class GovernmentRestrictionsOnConstructionOfReligiousBuildings(BaseAPICall):
    ENDPOINT = (
        "/rt/government-restrictions-on-construction-of-religious-buildings"
    )
    SINGLE_MODEL = GovernmentRestrictionsOnConstructionOfReligiousBuilding


class GovernmentRestrictionsOnReligiousEducations(BaseAPICall):
    ENDPOINT = "/rt/government-restrictions-on-religious-educations"
    SINGLE_MODEL = GovernmentRestrictionsOnReligiousEducation


class GovernmentRestrictionsOnCirculationOfReligiousLiteratures(BaseAPICall):
    ENDPOINT = (
        "/rt/government-restrictions-on-circulation-of-religious-literatures"
    )
    SINGLE_MODEL = GovernmentRestrictionsOnCirculationOfReligiousLiterature


class GovernmentDiscriminationAgainstReligiousGroupsTakingUpCertainOccupationsOrFunctions(
    BaseAPICall
):
    ENDPOINT = "/rt/government-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions"
    SINGLE_MODEL = GovernmentDiscriminationAgainstReligiousGroupTakingUpCertainOccupationOrFunction


class FrequencyOfSocietalViolenceAgainstReligiousGroups(BaseAPICall):
    ENDPOINT = "/rt/frequency-of-societal-violence-against-religious-groups"
    SINGLE_MODEL = FrequencyOfSocietalViolenceAgainstReligiousGroup


class SocietalDiscriminationAgainstReligiousGroupsTakingUpCertainOccupationsOrFunctions(
    BaseAPICall
):
    ENDPOINT = "/rt/societal-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions"
    SINGLE_MODEL = SocietalDiscriminationAgainstReligiousGroupTakingUpCertainOccupationOrFunction


class SocietalPressureToConvertOrAgainstConversions(BaseAPICall):
    ENDPOINT = "/rt/societal-pressure-to-convert-or-against-conversions"
    SINGLE_MODEL = SocietalPressureToConvertOrAgainstConversion
