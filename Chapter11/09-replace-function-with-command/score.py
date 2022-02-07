def score(candidate, medical_exam, scoring_guide):
    return Scorer(candidate, medical_exam, scoring_guide).execute()


class Scorer:
    def __init__(self, candidate, medical_exam, scoring_guide) -> None:
        self._candidate = candidate
        self._medical_exam = medical_exam
        self._scoring_guide = scoring_guide

    def execute(self):
        self._result = 0
        self._health_level = 0
        self._high_medical_risk_flag = False

        self.score_smoking()

        self._certification_grade = "regular"
        if self._scoring_guide.state_with_low_certification(
            self._candidate.origin_state
        ):
            self._certification_grade = "low"
            self._result -= 5

        # ...
        self._result -= max(self._health_level - 5, 0)
        return self._result

    def score_smoking(self):
        if self._medical_exam.is_smoker:
            self._health_level += 10
            self._high_medical_risk_flag = True
