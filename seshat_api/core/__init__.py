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


class PrivateComments(BaseAPICall):
    ENDPOINT = "/core/private-comments"
    SINGLE_MODEL = PrivateComment


class PrivateCommentParts(BaseAPICall):
    ENDPOINT = "/core/private-comments-parts"
    SINGLE_MODEL = PrivateCommentPart


class MacroRegions(BaseAPICall):
    ENDPOINT = "/core/macro-regions"
    SINGLE_MODEL = MacroRegion


class Regions(BaseAPICall):
    ENDPOINT = "/core/regions"
    SINGLE_MODEL = Region


class NGAs(BaseAPICall):
    ENDPOINT = "/core/ngas"
    SINGLE_MODEL = NGA


class Polities(BaseAPICall):
    ENDPOINT = "/core/polities"
    SINGLE_MODEL = Polity


class Capitals(BaseAPICall):
    ENDPOINT = "/core/capitals"
    SINGLE_MODEL = Capital


class NGAPolityRelations(BaseAPICall):
    ENDPOINT = "/core/nga-polity-relations"
    SINGLE_MODEL = NGAPolityRelation


class Countries(BaseAPICall):
    ENDPOINT = "/core/countries"
    SINGLE_MODEL = Country


class Sections(BaseAPICall):
    ENDPOINT = "/core/sections"
    SINGLE_MODEL = Section


class Subsections(BaseAPICall):
    ENDPOINT = "/core/subsections"
    SINGLE_MODEL = Subsection


class VariableHierarchies(BaseAPICall):
    ENDPOINT = "/core/variable-hierarchies"
    SINGLE_MODEL = VariableHierarchy


class References(BaseAPICall):
    ENDPOINT = "/core/references"
    SINGLE_MODEL = Reference


class Citations(BaseAPICall):
    ENDPOINT = "/core/citations"
    SINGLE_MODEL = Citation


class Comments(BaseAPICall):
    ENDPOINT = "/core/comments"
    SINGLE_MODEL = Comment


class CommentParts(BaseAPICall):
    ENDPOINT = "/core/comment-parts"
    SINGLE_MODEL = CommentPart


class CommentPartsThroughCitations(BaseAPICall):
    ENDPOINT = "/core/comment-parts-through-citations"
    SINGLE_MODEL = CommentPartThroughCitation


class Religions(BaseAPICall):
    ENDPOINT = "/core/religions"
    SINGLE_MODEL = Religion


class VideoShapefiles(BaseAPICall):
    ENDPOINT = "/core/video-shapefiles"
    SINGLE_MODEL = VideoShapefile


class GADMShapefiles(BaseAPICall):
    ENDPOINT = "/core/gadm-shapefiles"
    SINGLE_MODEL = GADMShapefile


class GADMCountries(BaseAPICall):
    ENDPOINT = "/core/gadm-countries"
    SINGLE_MODEL = GADMCountry


class GADMProvinces(BaseAPICall):
    ENDPOINT = "/core/gadm-provinces"
    SINGLE_MODEL = GADMProvince
