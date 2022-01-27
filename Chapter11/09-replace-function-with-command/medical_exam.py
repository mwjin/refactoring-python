class MedicalExam:
    def __init__(self, is_smoker) -> None:
        self._is_smoker = is_smoker

    @property
    def is_smoker(self):
        return self._is_smoker
