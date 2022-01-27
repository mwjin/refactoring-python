from candidate import Candidate
from medical_exam import MedicalExam
from score import score
from scoring_guide import ScoringGuide


def test_score():
    assert score(Candidate("Healthy"), MedicalExam(True), ScoringGuide()) == -5
    assert (
        score(Candidate("Unhealthy"), MedicalExam(True), ScoringGuide()) == -5
    )
    assert score(Candidate("Healthy"), MedicalExam(False), ScoringGuide()) == 0
    assert (
        score(Candidate("Unhealthy"), MedicalExam(False), ScoringGuide()) == 0
    )

