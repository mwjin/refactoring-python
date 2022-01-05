from production_plan import ProductionPlan
from adjustment import Adjustment


def test_production():
    production_plan = ProductionPlan()
    production_plan.apply_adjustment(Adjustment(100))
    production_plan.apply_adjustment(Adjustment(250))
    production_plan.apply_adjustment(Adjustment(300))
    assert production_plan.production == 650
