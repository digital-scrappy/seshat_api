from typing import Optional


class BaseModel:
    def __init__(
        self,
        data: dict,
        count: Optional[int] = None,
        name: Optional[str] = None,
    ):
        for key, value in data.items():
            if isinstance(value, dict):
                value = BaseModel(value)

            setattr(self, key, value)
        self._model_count = count
        self._model_name = name

    def __str__(self):
        if self._model_name and self._model_count:
            return f"<{self._model_name}: {self._model_count}>"
        elif self._model_name:
            return f"<{self._model_name}>"

        return f"<{self.__class__.__name__}>"

    def get_properties(self):
        """
        Get all properties of the model.

        Returns
        -------
        list
            A list of all properties of the model.
        """
        return [
            x
            for x in self.__dir__()
            if not x.startswith("_") and x not in ["get_properties"]
        ]
