class ScoringGuide:
    @staticmethod
    def state_with_low_certification(state):
        if state == "unhealthy":
            return True
        return False
