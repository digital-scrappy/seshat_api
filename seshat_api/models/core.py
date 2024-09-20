from ._base import BaseModel

__all__ = [
    "Polity",
    "PrivateComment",
    "PrivateCommentPart",
    "MacroRegion",
    "Region",
    "NGA",
    "Polity",
    "Capital",
    "NGAPolityRelation",
    "Country",
    "Section",
    "Subsection",
    "VariableHierarchy",
    "Reference",
    "Citation",
    "Comment",
    "CommentPart",
    "CommentPartThroughCitation",
    "Religion",
    "CliopatriaShapefile",
    "GADMShapefile",
    "GADMCountry",
    "GADMProvince",
]


class Polity(BaseModel):
    """
    A class representing a single Polity object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class PrivateComment(BaseModel):
    """
    A class representing a single Private Comment object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class PrivateCommentPart(BaseModel):
    """
    A class representing a single Private Comment Part object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class MacroRegion(BaseModel):
    """
    A class representing a single Macro Region object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Region(BaseModel):
    """
    A class representing a single Region object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class NGA(BaseModel):
    """
    A class representing a single NGA (Natural Geographic Area) object in the
    Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Polity(BaseModel):
    """
    A class representing a single Polity object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Capital(BaseModel):
    """
    A class representing a single Capital object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class NGAPolityRelation(BaseModel):
    """
    A class representing a single NGA–polity relation (relations between a
    Natural Geographic Area, NGA, and a polity) object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Country(BaseModel):
    """
    A class representing a single Country object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Section(BaseModel):
    """
    A class representing a single Section object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Subsection(BaseModel):
    """
    A class representing a single Subsection object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class VariableHierarchy(BaseModel):
    """
    A class representing a single Variable Hierarchy object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Reference(BaseModel):
    """
    A class representing a single Reference object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Citation(BaseModel):
    """
    A class representing a single Citation object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Comment(BaseModel):
    """
    A class representing a single Comment object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class CommentPart(BaseModel):
    """
    A class representing a single Comment Part object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class CommentPartThroughCitation(BaseModel):
    """
    A class representing a single Comment Part Through Citation object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class Religion(BaseModel):
    """
    A class representing a single Religion object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class CliopatriaShapefile(BaseModel):
    """
    A class representing a single Cliopatria Shapefile object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class GADMShapefile(BaseModel):
    """
    A class representing a single GADM Shapefile object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class GADMCountry(BaseModel):
    """
    A class representing a single GADM Country object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass


class GADMProvince(BaseModel):
    """
    A class representing a single GADM Province object in the Seshat API.

    Parameters
    ----------
    data : dict
        The data to use in the model.
    count : int, optional
        The total count of items in the API.
    name : str, optional
        The name of the API.

    ..
        TODO: Add an example of how to create the object
    """
    pass
