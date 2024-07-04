from ..base_model import BaseAPICall
from ..models import (
    Polity,
    PrivateComment,
    PrivateCommentPart,
    MacroRegion,
    Region,
    NGA,
    Polity,
    Capital,
    NGAPolityRelation,
    Country,
    Section,
    Subsection,
    VariableHierarchy,
    Reference,
    Citation,
    Comment,
    CommentPart,
    CommentPartThroughCitation,
    Religion,
    VideoShapefile,
    GADMShapefile,
    GADMCountry,
    GADMProvince,
)

__all__ = [
    "Polities",
    "PrivateComments",
    "PrivateCommentParts",
    "MacroRegions",
    "Regions",
    "NGAs",
    "Polities",
    "Capitals",
    "NGAPolityRelations",
    "Countries",
    "Sections",
    "Subsections",
    "VariableHierarchies",
    "References",
    "Citations",
    "Comments",
    "CommentParts",
    "CommentPartsThroughCitations",
    "Religions",
    "VideoShapefiles",
    "GADMShapefiles",
    "GADMCountries",
    "GADMProvinces",
]


class PrivateComments(BaseAPICall):
    """
    A class for interacting with the private comments endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import PrivateComments
    >>> client = SeshatAPI()
    >>> private_comments = PrivateComments(client)
    """
    ENDPOINT = "/core/private-comments"
    SINGLE_MODEL = PrivateComment


class PrivateCommentParts(BaseAPICall):
    """
    A class for interacting with the private comment parts endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import PrivateCommentParts
    >>> client = SeshatAPI()
    >>> private_comment_parts = PrivateCommentParts(client)
    """
    ENDPOINT = "/core/private-comments-parts"
    SINGLE_MODEL = PrivateCommentPart


class MacroRegions(BaseAPICall):
    """
    A class for interacting with the macro regions endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import MacroRegions
    >>> client = SeshatAPI()
    >>> macro_regions = MacroRegions(client)
    """
    ENDPOINT = "/core/macro-regions"
    SINGLE_MODEL = MacroRegion


class Regions(BaseAPICall):
    """
    A class for interacting with the regions endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Regions
    >>> client = SeshatAPI()
    >>> regions = Regions(client)
    """
    ENDPOINT = "/core/regions"
    SINGLE_MODEL = Region


class NGAs(BaseAPICall):
    """
    A class for interacting with the NGAs endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import NGAs
    >>> client = SeshatAPI()
    >>> ngas = NGAs(client)
    """
    ENDPOINT = "/core/ngas"
    SINGLE_MODEL = NGA


class Polities(BaseAPICall):
    """
    A class for interacting with the polities endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Polities
    >>> client = SeshatAPI()
    >>> polities = Polities(client)
    """
    ENDPOINT = "/core/polities"
    SINGLE_MODEL = Polity


class Capitals(BaseAPICall):
    """
    A class for interacting with the capitals endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Capitals
    >>> client = SeshatAPI()
    >>> capitals = Capitals(client)
    """
    ENDPOINT = "/core/capitals"
    SINGLE_MODEL = Capital


class NGAPolityRelations(BaseAPICall):
    """
    A class for interacting with the NGA polity relations endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import NGAPolityRelations
    >>> client = SeshatAPI()
    >>> nga_polity_relations = NGAPolityRelations(client)
    """
    ENDPOINT = "/core/nga-polity-relations"
    SINGLE_MODEL = NGAPolityRelation


class Countries(BaseAPICall):
    """
    A class for interacting with the countries endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Countries
    >>> client = SeshatAPI()
    >>> countries = Countries(client)
    """
    ENDPOINT = "/core/countries"
    SINGLE_MODEL = Country


class Sections(BaseAPICall):
    """
    A class for interacting with the sections endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Sections
    >>> client = SeshatAPI()
    >>> sections = Sections(client)
    """
    ENDPOINT = "/core/sections"
    SINGLE_MODEL = Section


class Subsections(BaseAPICall):
    """
    A class for interacting with the subsections endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Subsections
    >>> client = SeshatAPI()
    >>> subsections = Subsections(client)
    """
    ENDPOINT = "/core/subsections"
    SINGLE_MODEL = Subsection


class VariableHierarchies(BaseAPICall):
    """
    A class for interacting with the variable hierarchies endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import VariableHierarchies
    >>> client = SeshatAPI()
    >>> variable_hierarchies = VariableHierarchies(client)
    """
    ENDPOINT = "/core/variable-hierarchies"
    SINGLE_MODEL = VariableHierarchy


class References(BaseAPICall):
    """
    A class for interacting with the references endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import References
    >>> client = SeshatAPI()
    >>> references = References(client)
    """
    ENDPOINT = "/core/references"
    SINGLE_MODEL = Reference


class Citations(BaseAPICall):
    """
    A class for interacting with the citations endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Citations
    >>> client = SeshatAPI()
    >>> citations = Citations(client)
    """
    ENDPOINT = "/core/citations"
    SINGLE_MODEL = Citation


class Comments(BaseAPICall):
    """
    A class for interacting with the comments endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Comments
    >>> client = SeshatAPI()
    >>> comments = Comments(client)
    """
    ENDPOINT = "/core/comments"
    SINGLE_MODEL = Comment


class CommentParts(BaseAPICall):
    """
    A class for interacting with the comment parts endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import CommentParts
    >>> client = SeshatAPI()
    >>> comment_parts = CommentParts(client)
    """
    ENDPOINT = "/core/comment-parts"
    SINGLE_MODEL = CommentPart


class CommentPartsThroughCitations(BaseAPICall):
    """
    A class for interacting with the comment parts through citations endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import CommentPartsThroughCitations
    >>> client = SeshatAPI()
    >>> comment_parts_through_citations = CommentPartsThroughCitations(client)
    """
    ENDPOINT = "/core/comment-parts-through-citations"
    SINGLE_MODEL = CommentPartThroughCitation


class Religions(BaseAPICall):
    """
    A class for interacting with the religions endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import Religions
    >>> client = SeshatAPI()
    >>> religions = Religions(client)
    """
    ENDPOINT = "/core/religions"
    SINGLE_MODEL = Religion


class VideoShapefiles(BaseAPICall):
    """
    A class for interacting with the video shapefiles endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import VideoShapefiles
    >>> client = SeshatAPI()
    >>> video_shapefiles = VideoShapefiles(client)
    """
    ENDPOINT = "/core/video-shapefiles"
    SINGLE_MODEL = VideoShapefile


class GADMShapefiles(BaseAPICall):
    """
    A class for interacting with the GADM shapefiles endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import GADMShapefiles
    >>> client = SeshatAPI()
    >>> gadm_shapefiles = GADMShapefiles(client)
    """
    ENDPOINT = "/core/gadm-shapefiles"
    SINGLE_MODEL = GADMShapefile


class GADMCountries(BaseAPICall):
    """
    A class for interacting with the GADM countries endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import GADMCountries
    >>> client = SeshatAPI()
    >>> gadm_countries = GADMCountries(client)
    """
    ENDPOINT = "/core/gadm-countries"
    SINGLE_MODEL = GADMCountry


class GADMProvinces(BaseAPICall):
    """
    A class for interacting with the GADM provinces endpoint of the Seshat API.

    Parameters
    ----------
    client : SeshatAPI
        The API client to use for requests.

    Example
    -------
    >>> from seshat_api import SeshatAPI
    >>> from seshat_api.core import GADMProvinces
    >>> client = SeshatAPI()
    >>> gadm_provinces = GADMProvinces(client)
    """
    ENDPOINT = "/core/gadm-provinces"
    SINGLE_MODEL = GADMProvince
