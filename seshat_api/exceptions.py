from typing import Dict, Any, Optional
import json


class SeshatAPIException(Exception):
    """
    Based on PyGithub's error handling.

    This class is the base of all exceptions raised by the API library

    Some other types of exceptions might be raised by underlying libraries,
    for example for network-related issues.

    Parameters
    ----------
    status : int
        The status code.
    data : Any, optional
        The (decoded) data returned by the Seshat API.
    headers : dict, optional
        The headers returned by the Seshat API.
    message : str, optional
        The message to include in the exception.
    """

    def __init__(
        self,
        status: int,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        message: Optional[str] = None,
    ):
        super().__init__()
        self.status = status
        self.data = data
        self.headers = headers
        self.message = message
        self.args = (status, data, headers, message)

    def __repr__(self) -> str:
        """
        Return a string representation of the exception.

        Returns
        -------
        str
            The string representation of the exception.
        """
        return f"{self.__class__.__name__}({self.__str__()})"

    def __str__(self) -> str:
        """
        Return a string representation of the exception.

        Returns
        -------
        str
            The string representation of the exception.
        """
        if self.message:
            msg = f"{self.message}: {self.status}"
        else:
            msg = f"{self.status}"

        if self.data is not None and isinstance(self.data, str):
            msg += " " + json.dumps(self.data)

        return msg
