from .constants import BASE_URL, TOKEN_ENDPOINT
from .exceptions import SeshatAPIException
# from .core import Polities

import requests

from typing import Optional
from json import JSONDecodeError


class SeshatAPI:
    """
    A class for interacting with the Seshat API.

    Parameters
    ----------
    username : str, optional
        The username to use for authentication.
    password : str, optional
        The password to use for authentication.
    base_url : str, optional
        The base URL of the API. Default is BASE_URL (found in
        seshat_api.constants).
    """

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        self.base_url = base_url or BASE_URL
        self.username = username
        self.__token = None
        if self.username and password:
            self.__get_token(username, password)

    def __get_token(self, username: str, password: str) -> str:
        """
        Get a token for the API.

        Parameters
        ----------
        username : str
            The username to use for authentication.
        password : str
            The password to use for authentication.

        Returns
        -------
        str
            The token to use for authentication.
        """
        if not self.__token:
            response = requests.post(
                f"{self.base_url}/{TOKEN_ENDPOINT}",
                data={"username": username, "password": password},
            )
            response.raise_for_status()
            self.__token = response.json()["token"]

        return self.__token

    def __createException(
        self,
        request: str,
        response: requests.Response,
        message: Optional[str] = None,
    ) -> SeshatAPIException:
        """
        Create an exception from a response.

        Parameters
        ----------
        request : str
            The request that was made.
        response : requests.Response
            The response from the request.
        message : str, optional
            The message to include in the exception.

        Returns
        -------
        SeshatAPIException
            The exception created from the response.
        """
        try:
            data = response.json()
        except JSONDecodeError:
            data = response.text

        return SeshatAPIException(
            response.status_code, data, response.headers, message
        )

    def get(self, endpoint: str, params: dict = None) -> dict:
        """
        Get data from the API.

        Parameters
        ----------
        endpoint : str
            The endpoint to get data from.
        params : dict, optional
            The parameters to use in the request.

        Returns
        -------
        dict
            The data returned from the API.
        """
        url = f"{self.base_url}{endpoint}"
        auth_headers = {}
        message = None

        # Set authentication headers if token is present
        if self.__token:
            auth_headers = {"Authorization": f"Token {self.__token}"}

        try:
            response = requests.get(
                url,
                params=params,
                headers=auth_headers,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                message = "User is not logged in. Did you pass a username and "
                message += "password to the client?"

            if e.response.status_code == 404:
                message = "API endpoint not found"

            if e.response.status_code == 429:
                message = "API rate limit exceeded"

            raise self.__createException(endpoint, e.response, message) from None

        # Return JSON-coded data
        return response.json()

    def count(self, endpoint: str, params: Optional[dict] = None) -> int:
        """
        Get the count of items in the API.

        Parameters
        ----------
        endpoint : str
            The endpoint to get the count from.
        params : dict, optional
            The parameters to use in the request.

        Returns
        -------
        int
            The count of items in the API.
        """
        return self.get(endpoint, params)["count"]
