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
    Camels,
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

__all__ = [
    "LongWalls",
    "Coppers",
    "Bronzes",
    "Irons",
    "Steels",
    "Javelins",
    "Atlatls",
    "Slings",
    "SelfBows",
    "CompositeBows",
    "Crossbows",
    "TensionSiegeEngines",
    "SlingSiegeEngines",
    "GunpowderSiegeArtilleries",
    "HandheldFirearms",
    "WarClubs",
    "BattleAxes",
    "Daggers",
    "Swords",
    "Spears",
    "Polearms",
    "Dogs",
    "Donkeys",
    "Horses",
    "Camels",
    "Elephants",
    "WoodBarksEtc",
    "Leathers",
    "Shields",
    "Helmets",
    "Breastplates",
    "LimbProtections",
    "ScaledArmors",
    "LaminarArmors",
    "PlateArmors",
    "SmallVesselsCanoesEtc",
    "MerchantShipsPressedIntoService",
    "SpecializedMilitaryVessels",
    "SettlementInDefensivePositions",
    "WoodenPalisades",
    "EarthRamparts",
    "Ditches",
    "Moats",
    "StoneWallsNonMortared",
    "StoneWallsMortared",
    "FortifiedCamps",
    "ComplexFortifications",
    "ModernFortifications",
    "Chainmails",
]


class LongWalls(BaseAPICall):
    """
    A class for interacting with the long walls endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import LongWalls
    >>> client = SeshatAPI()
    >>> long_walls = LongWalls(client)
    """
    ENDPOINT = "/wf/long-walls"
    SINGLE_MODEL = LongWall


class Coppers(BaseAPICall):
    """
    A class for interacting with the coppers endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Coppers
    >>> client = SeshatAPI()
    >>> coppers = Coppers(client)
    """
    ENDPOINT = "/wf/coppers"
    SINGLE_MODEL = Copper


class Bronzes(BaseAPICall):
    """
    A class for interacting with the bronzes endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Bronzes
    >>> client = SeshatAPI()
    >>> bronzes = Bronzes(client)
    """
    ENDPOINT = "/wf/bronzes"
    SINGLE_MODEL = Bronze


class Irons(BaseAPICall):
    """
    A class for interacting with the irons endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Irons
    >>> client = SeshatAPI()
    >>> irons = Irons(client)
    """
    ENDPOINT = "/wf/irons"
    SINGLE_MODEL = Iron


class Steels(BaseAPICall):
    """
    A class for interacting with the steels endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Steels
    >>> client = SeshatAPI()
    >>> steels = Steels(client)
    """
    ENDPOINT = "/wf/steels"
    SINGLE_MODEL = Steel


class Javelins(BaseAPICall):
    """
    A class for interacting with the javelins endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Javelins
    >>> client = SeshatAPI()
    >>> javelins = Javelins(client)
    """
    ENDPOINT = "/wf/javelins"
    SINGLE_MODEL = Javelin


class Atlatls(BaseAPICall):
    """
    A class for interacting with the atlatls endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Atlatls
    >>> client = SeshatAPI()
    >>> atlatls = Atlatls(client)
    """
    ENDPOINT = "/wf/atlatls"
    SINGLE_MODEL = Atlatl


class Slings(BaseAPICall):
    """
    A class for interacting with the slings endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Slings
    >>> client = SeshatAPI()
    >>> slings = Slings(client)
    """
    ENDPOINT = "/wf/slings"
    SINGLE_MODEL = Sling


class SelfBows(BaseAPICall):
    """
    A class for interacting with the self-bows endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import SelfBows
    >>> client = SeshatAPI()
    >>> self_bows = SelfBows(client)
    """
    ENDPOINT = "/wf/self-bows"
    SINGLE_MODEL = Selfbow


class CompositeBows(BaseAPICall):
    """
    A class for interacting with the composite-bows endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import CompositeBows
    >>> client = SeshatAPI()
    >>> composite_bows = CompositeBows(client)
    """
    ENDPOINT = "/wf/composite-bows"
    SINGLE_MODEL = CompositeBow


class Crossbows(BaseAPICall):
    """
    A class for interacting with the crossbows endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Crossbows
    >>> client = SeshatAPI()
    >>> crossbows = Crossbows(client)
    """
    ENDPOINT = "/wf/crossbows"
    SINGLE_MODEL = Crossbow


class TensionSiegeEngines(BaseAPICall):
    """
    A class for interacting with the tension siege engines endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import TensionSiegeEngines
    >>> client = SeshatAPI()
    >>> tension_siege_engines = TensionSiegeEngines(client)
    """
    ENDPOINT = "/wf/tension-siege-engines"
    SINGLE_MODEL = TensionSiegeEngine


class SlingSiegeEngines(BaseAPICall):
    """
    A class for interacting with the sling siege engines endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import SlingSiegeEngines
    >>> client = SeshatAPI()
    >>> sling_siege_engines = SlingSiegeEngines(client)
    """
    ENDPOINT = "/wf/sling-siege-engines"
    SINGLE_MODEL = SlingSiegeEngine


class GunpowderSiegeArtilleries(BaseAPICall):
    """
    A class for interacting with the gunpowder siege artilleries endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import GunpowderSiegeArtilleries
    >>> client = SeshatAPI()
    >>> gunpowder_siege_artilleries = GunpowderSiegeArtilleries(client)
    """
    ENDPOINT = "/wf/gunpowder-siege-artilleries"
    SINGLE_MODEL = GunpowderSiegeArtillery


class HandheldFirearms(BaseAPICall):
    """
    A class for interacting with the handheld firearms endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import HandheldFirearms
    >>> client = SeshatAPI()
    >>> handheld_firearms = HandheldFirearms(client)
    """
    ENDPOINT = "/wf/handheld-firearms"
    SINGLE_MODEL = HandheldFirearm


class WarClubs(BaseAPICall):
    """
    A class for interacting with the war clubs endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import WarClubs
    >>> client = SeshatAPI()
    >>> war_clubs = WarClubs(client)
    """
    ENDPOINT = "/wf/war-clubs"
    SINGLE_MODEL = WarClub


class BattleAxes(BaseAPICall):
    """
    A class for interacting with the battle axes endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import BattleAxes
    >>> client = SeshatAPI()
    >>> battle_axes = BattleAxes(client)
    """
    ENDPOINT = "/wf/battle-axes"
    SINGLE_MODEL = BattleAxe


class Daggers(BaseAPICall):
    """
    A class for interacting with the daggers endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Daggers
    >>> client = SeshatAPI()
    >>> daggers = Daggers(client)
    """
    ENDPOINT = "/wf/daggers"
    SINGLE_MODEL = Dagger


class Swords(BaseAPICall):
    """
    A class for interacting with the swords endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Swords
    >>> client = SeshatAPI()
    >>> swords = Swords(client)
    """
    ENDPOINT = "/wf/swords"
    SINGLE_MODEL = Sword


class Spears(BaseAPICall):
    """
    A class for interacting with the spears endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Spears
    >>> client = SeshatAPI()
    >>> spears = Spears(client)
    """
    ENDPOINT = "/wf/spears"
    SINGLE_MODEL = Spear


class Polearms(BaseAPICall):
    """
    A class for interacting with the polearms endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Polearms
    >>> client = SeshatAPI()
    >>> polearms = Polearms(client)
    """
    ENDPOINT = "/wf/polearms"
    SINGLE_MODEL = Polearm


class Dogs(BaseAPICall):
    """
    A class for interacting with the dogs endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Dogs
    >>> client = SeshatAPI()
    >>> dogs = Dogs(client)
    """
    ENDPOINT = "/wf/dogs"
    SINGLE_MODEL = Dog


class Donkeys(BaseAPICall):
    """
    A class for interacting with the donkeys endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Donkeys
    >>> client = SeshatAPI()
    >>> donkeys = Donkeys(client)
    """
    ENDPOINT = "/wf/donkeys"
    SINGLE_MODEL = Donkey


class Horses(BaseAPICall):
    """
    A class for interacting with the horses endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Horses
    >>> client = SeshatAPI()
    >>> horses = Horses(client)
    """
    ENDPOINT = "/wf/horses"
    SINGLE_MODEL = Horse


class Camels(BaseAPICall):
    """
    A class for interacting with the camels endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Camels
    >>> client = SeshatAPI()
    >>> camels = Camels(client)
    """
    ENDPOINT = "/wf/camels"
    SINGLE_MODEL = Camels


class Elephants(BaseAPICall):
    """
    A class for interacting with the elephants endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Elephants
    >>> client = SeshatAPI()
    >>> elephants = Elephants(client)
    """
    ENDPOINT = "/wf/elephants"
    SINGLE_MODEL = Elephant


class WoodBarksEtc(BaseAPICall):
    """
    A class for interacting with the woodbark, etc endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import WoodBarksEtc
    >>> client = SeshatAPI()
    >>> wood_barks_etc = WoodBarksEtc(client)
    """
    ENDPOINT = "/wf/wood-bark-etc"
    SINGLE_MODEL = WoodBarkEtc


class Leathers(BaseAPICall):
    """
    A class for interacting with the leathers endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Leathers
    >>> client = SeshatAPI()
    >>> leathers = Leathers(client)
    """
    ENDPOINT = "/wf/leathers"
    SINGLE_MODEL = Leather


class Shields(BaseAPICall):
    """
    A class for interacting with the shields endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Shields
    >>> client = SeshatAPI()
    >>> shields = Shields(client)
    """
    ENDPOINT = "/wf/shields"
    SINGLE_MODEL = Shield


class Helmets(BaseAPICall):
    """
    A class for interacting with the helmets endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Helmets
    >>> client = SeshatAPI()
    >>> helmets = Helmets(client)
    """
    ENDPOINT = "/wf/helmets"
    SINGLE_MODEL = Helmet


class Breastplates(BaseAPICall):
    """
    A class for interacting with the breastplates endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Breastplates
    >>> client = SeshatAPI()
    >>> breastplates = Breastplates(client)
    """
    ENDPOINT = "/wf/breastplates"
    SINGLE_MODEL = Breastplate


class LimbProtections(BaseAPICall):
    """
    A class for interacting with the limb protections endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import LimbProtections
    >>> client = SeshatAPI()
    >>> limb_protections = LimbProtections(client)
    """
    ENDPOINT = "/wf/limb-protections"
    SINGLE_MODEL = LimbProtection


class ScaledArmors(BaseAPICall):
    """
    A class for interacting with the scaled armors endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import ScaledArmors
    >>> client = SeshatAPI()
    >>> scaled_armors = ScaledArmors(client)
    """
    ENDPOINT = "/wf/scaled-armors"
    SINGLE_MODEL = ScaledArmor


class LaminarArmors(BaseAPICall):
    """
    A class for interacting with the laminar armors endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import LaminarArmors
    >>> client = SeshatAPI()
    >>> laminar_armors = LaminarArmors(client)
    """
    ENDPOINT = "/wf/laminar-armors"
    SINGLE_MODEL = LaminarArmor


class PlateArmors(BaseAPICall):
    """
    A class for interacting with the plate armors endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import PlateArmors
    >>> client = SeshatAPI()
    >>> plate_armors = PlateArmors(client)
    """
    ENDPOINT = "/wf/plate-armors"
    SINGLE_MODEL = PlateArmor


class SmallVesselsCanoesEtc(BaseAPICall):
    """
    A class for interacting with the small vessels, canoes, etc. endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import SmallVesselsCanoesEtc
    >>> client = SeshatAPI()
    >>> small_vessels_canoes_etc = SmallVesselsCanoesEtc(client)
    """
    ENDPOINT = "/wf/small-vessel-canoe-etc"
    SINGLE_MODEL = SmallVesselCanoeEtc


class MerchantShipsPressedIntoService(BaseAPICall):
    """
    A class for interacting with the merchant ships pressed into service
    endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import MerchantShipsPressedIntoService
    >>> client = SeshatAPI()
    >>> merchant_ships_pressed_into_service = MerchantShipsPressedIntoService(client)
    """
    ENDPOINT = "/wf/merchant-ship-pressed-into-service"
    SINGLE_MODEL = MerchantShipPressedIntoService


class SpecializedMilitaryVessels(BaseAPICall):
    """
    A class for interacting with the specialized military vessels endpoint of
    the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import SpecializedMilitaryVessels
    >>> client = SeshatAPI()
    >>> specialized_military_vessels = SpecializedMilitaryVessels(client)
    """
    ENDPOINT = "/wf/specialized-military-vessels"
    SINGLE_MODEL = SpecializedMilitaryVessel


class SettlementInDefensivePositions(BaseAPICall):
    """
    A class for interacting with the settlement in defensive positions endpoint
    of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import SettlementInDefensivePositions
    >>> client = SeshatAPI()
    >>> settlement_in_defensive_positions = SettlementInDefensivePositions(client)
    """
    ENDPOINT = "/wf/settlement-in-defensive-positions"
    SINGLE_MODEL = SettlementInDefensivePosition


class WoodenPalisades(BaseAPICall):
    """
    A class for interacting with the wooden palisades endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import WoodenPalisades
    >>> client = SeshatAPI()
    >>> wooden_palisades = WoodenPalisades(client)
    """
    ENDPOINT = "/wf/wooden-palisades"
    SINGLE_MODEL = WoodenPalisade


class EarthRamparts(BaseAPICall):
    """
    A class for interacting with the earth ramparts endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import EarthRamparts
    >>> client = SeshatAPI()
    >>> earth_ramparts = EarthRamparts(client)
    """
    ENDPOINT = "/wf/earth-ramparts"
    SINGLE_MODEL = EarthRampart


class Ditches(BaseAPICall):
    """
    A class for interacting with the ditches endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Ditches
    >>> client = SeshatAPI()
    >>> ditches = Ditches(client)
    """
    ENDPOINT = "/wf/ditches"
    SINGLE_MODEL = Ditch


class Moats(BaseAPICall):
    """
    A class for interacting with the moats endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Moats
    >>> client = SeshatAPI()
    >>> moats = Moats(client)
    """
    ENDPOINT = "/wf/moats"
    SINGLE_MODEL = Moat


class StoneWallsNonMortared(BaseAPICall):
    """
    A class for interacting with the stone walls non-mortared endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import StoneWallsNonMortared
    >>> client = SeshatAPI()
    >>> stone_walls_non_mortared = StoneWallsNonMortared(client)
    """
    ENDPOINT = "/wf/stone-walls-non-mortared"
    SINGLE_MODEL = StoneWallNonMortared


class StoneWallsMortared(BaseAPICall):
    """
    A class for interacting with the stone walls mortared endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import StoneWallsMortared
    >>> client = SeshatAPI()
    >>> stone_walls_mortared = StoneWallsMortared(client)
    """
    ENDPOINT = "/wf/stone-walls-mortared"
    SINGLE_MODEL = StoneWallMortared


class FortifiedCamps(BaseAPICall):
    """
    A class for interacting with the fortified camps endpoint of the Seshat
    API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import FortifiedCamps
    >>> client = SeshatAPI()
    >>> fortified_camps = FortifiedCamps(client)
    """
    ENDPOINT = "/wf/fortified-camps"
    SINGLE_MODEL = FortifiedCamp


class ComplexFortifications(BaseAPICall):
    """
    A class for interacting with the complex fortifications endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import ComplexFortifications
    >>> client = SeshatAPI()
    >>> complex_fortifications = ComplexFortifications(client)
    """
    ENDPOINT = "/wf/complex-fortifications"
    SINGLE_MODEL = ComplexFortification


class ModernFortifications(BaseAPICall):
    """
    A class for interacting with the modern fortifications endpoint of the
    Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import ModernFortifications
    >>> client = SeshatAPI()
    >>> modern_fortifications = ModernFortifications(client)
    """
    ENDPOINT = "/wf/modern-fortifications"
    SINGLE_MODEL = ModernFortification


class Chainmails(BaseAPICall):
    """
    A class for interacting with the chainmails endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.wf import Chainmails
    >>> client = SeshatAPI()
    >>> chainmails = Chainmails(client)
    """
    ENDPOINT = "/wf/chainmails"
    SINGLE_MODEL = Chainmail
