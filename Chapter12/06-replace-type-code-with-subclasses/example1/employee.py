class Employee:
    def __init__(self, name, type) -> None:
        self._validate_type(type)
        self._name = name
        self._type = type

    def _validate_type(self, type):
        if type not in ["engineer", "manager", "salesperson"]:
            raise ValueError(f'There is no "{type}" employee type.')

    def __str__(self) -> str:
        return f"{self._name} ({self._type})"
