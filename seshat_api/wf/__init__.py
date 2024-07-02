from ..base_model import BaseAPICall

from ..models import (
    LongWall,
    Copper,
    Bronze,
    Iron,
    Steel,
    Javelin,
    Atlatl,
    Sling,
    Selfbow,
    CompositeBow,
    Crossbow,
    TensionSiegeEngine,
    SlingSiegeEngine,
    GunpowderSiegeArtillery,
    HandheldFirearm,
    WarClub,
    BattleAxe,
    Dagger,
    Sword,
    Spear,
    Polearm,
    Dog,
    Donkey,
    Horse,
    Camel,
    Elephant,
    WoodBarkEtc,
    Leather,
    Shield,
    Helmet,
    Breastplate,
    LimbProtection,
    ScaledArmor,
    LaminarArmor,
    PlateArmor,
    SmallVesselCanoeEtc,
    MerchantShipPressedIntoService,
    SpecializedMilitaryVessel,
    SettlementInDefensivePosition,
    WoodenPalisade,
    EarthRampart,
    Ditch,
    Moat,
    StoneWallNonMortared,
    StoneWallMortared,
    FortifiedCamp,
    ComplexFortification,
    ModernFortification,
    Chainmail,
)


class LongWalls(BaseAPICall):
    ENDPOINT = "/wf/long-walls"
    SINGLE_MODEL = LongWall


class Coppers(BaseAPICall):
    ENDPOINT = "/wf/coppers"
    SINGLE_MODEL = Copper


class Bronzes(BaseAPICall):
    ENDPOINT = "/wf/bronzes"
    SINGLE_MODEL = Bronze


class Irons(BaseAPICall):
    ENDPOINT = "/wf/irons"
    SINGLE_MODEL = Iron


class Steels(BaseAPICall):
    ENDPOINT = "/wf/steels"
    SINGLE_MODEL = Steel


class Javelins(BaseAPICall):
    ENDPOINT = "/wf/javelins"
    SINGLE_MODEL = Javelin


class Atlatls(BaseAPICall):
    ENDPOINT = "/wf/atlatls"
    SINGLE_MODEL = Atlatl


class Slings(BaseAPICall):
    ENDPOINT = "/wf/slings"
    SINGLE_MODEL = Sling


class SelfBows(BaseAPICall):
    ENDPOINT = "/wf/self-bows"
    SINGLE_MODEL = Selfbow


class CompositeBows(BaseAPICall):
    ENDPOINT = "/wf/composite-bows"
    SINGLE_MODEL = CompositeBow


class Crossbows(BaseAPICall):
    ENDPOINT = "/wf/crossbows"
    SINGLE_MODEL = Crossbow


class TensionSiegeEngines(BaseAPICall):
    ENDPOINT = "/wf/tension-siege-engines"
    SINGLE_MODEL = TensionSiegeEngine


class SlingSiegeEngines(BaseAPICall):
    ENDPOINT = "/wf/sling-siege-engines"
    SINGLE_MODEL = SlingSiegeEngine


class GunpowderSiegeArtilleries(BaseAPICall):
    ENDPOINT = "/wf/gunpowder-siege-artilleries"
    SINGLE_MODEL = GunpowderSiegeArtillery


class HandheldFirearms(BaseAPICall):
    ENDPOINT = "/wf/handheld-firearms"
    SINGLE_MODEL = HandheldFirearm


class WarClubs(BaseAPICall):
    ENDPOINT = "/wf/war-clubs"
    SINGLE_MODEL = WarClub


class BattleAxes(BaseAPICall):
    ENDPOINT = "/wf/battle-axes"
    SINGLE_MODEL = BattleAxe


class Daggers(BaseAPICall):
    ENDPOINT = "/wf/daggers"
    SINGLE_MODEL = Dagger


class Swords(BaseAPICall):
    ENDPOINT = "/wf/swords"
    SINGLE_MODEL = Sword


class Spears(BaseAPICall):
    ENDPOINT = "/wf/spears"
    SINGLE_MODEL = Spear


class Polearms(BaseAPICall):
    ENDPOINT = "/wf/polearms"
    SINGLE_MODEL = Polearm


class Dogs(BaseAPICall):
    ENDPOINT = "/wf/dogs"
    SINGLE_MODEL = Dog


class Donkeys(BaseAPICall):
    ENDPOINT = "/wf/donkeys"
    SINGLE_MODEL = Donkey


class Horses(BaseAPICall):
    ENDPOINT = "/wf/horses"
    SINGLE_MODEL = Horse


class Camels(BaseAPICall):
    ENDPOINT = "/wf/camels"
    SINGLE_MODEL = Camel


class Elephants(BaseAPICall):
    ENDPOINT = "/wf/elephants"
    SINGLE_MODEL = Elephant


class WoodBarksEtc(BaseAPICall):
    ENDPOINT = "/wf/wood-bark-etc"
    SINGLE_MODEL = WoodBarkEtc


class Leathers(BaseAPICall):
    ENDPOINT = "/wf/leathers"
    SINGLE_MODEL = Leather


class Shields(BaseAPICall):
    ENDPOINT = "/wf/shields"
    SINGLE_MODEL = Shield


class Helmets(BaseAPICall):
    ENDPOINT = "/wf/helmets"
    SINGLE_MODEL = Helmet


class Breastplates(BaseAPICall):
    ENDPOINT = "/wf/breastplates"
    SINGLE_MODEL = Breastplate


class LimbProtections(BaseAPICall):
    ENDPOINT = "/wf/limb-protections"
    SINGLE_MODEL = LimbProtection


class ScaledArmors(BaseAPICall):
    ENDPOINT = "/wf/scaled-armors"
    SINGLE_MODEL = ScaledArmor


class LaminarArmors(BaseAPICall):
    ENDPOINT = "/wf/laminar-armors"
    SINGLE_MODEL = LaminarArmor


class PlateArmors(BaseAPICall):
    ENDPOINT = "/wf/plate-armors"
    SINGLE_MODEL = PlateArmor


class SmallVesselsCanoesEtc(BaseAPICall):
    ENDPOINT = "/wf/small-vessel-canoe-etc"
    SINGLE_MODEL = SmallVesselCanoeEtc


class MerchantShipsPressedIntoService(BaseAPICall):
    ENDPOINT = "/wf/merchant-ship-pressed-into-service"
    SINGLE_MODEL = MerchantShipPressedIntoService


class SpecializedMilitaryVessels(BaseAPICall):
    ENDPOINT = "/wf/specialized-military-vessels"
    SINGLE_MODEL = SpecializedMilitaryVessel


class SettlementInDefensivePositions(BaseAPICall):
    ENDPOINT = "/wf/settlement-in-defensive-positions"
    SINGLE_MODEL = SettlementInDefensivePosition


class WoodenPalisades(BaseAPICall):
    ENDPOINT = "/wf/wooden-palisades"
    SINGLE_MODEL = WoodenPalisade


class EarthRamparts(BaseAPICall):
    ENDPOINT = "/wf/earth-ramparts"
    SINGLE_MODEL = EarthRampart


class Ditches(BaseAPICall):
    ENDPOINT = "/wf/ditches"
    SINGLE_MODEL = Ditch


class Moats(BaseAPICall):
    ENDPOINT = "/wf/moats"
    SINGLE_MODEL = Moat


class StoneWallsNonMortared(BaseAPICall):
    ENDPOINT = "/wf/stone-walls-non-mortared"
    SINGLE_MODEL = StoneWallNonMortared


class StoneWallsMortared(BaseAPICall):
    ENDPOINT = "/wf/stone-walls-mortared"
    SINGLE_MODEL = StoneWallMortared


class FortifiedCamps(BaseAPICall):
    ENDPOINT = "/wf/fortified-camps"
    SINGLE_MODEL = FortifiedCamp


class ComplexFortifications(BaseAPICall):
    ENDPOINT = "/wf/complex-fortifications"
    SINGLE_MODEL = ComplexFortification


class ModernFortifications(BaseAPICall):
    ENDPOINT = "/wf/modern-fortifications"
    SINGLE_MODEL = ModernFortification


class Chainmails(BaseAPICall):
    ENDPOINT = "/wf/chainmails"
    SINGLE_MODEL = Chainmail
