from domain import Measure
from requirements import *
from deliverables import *


M1 = Measure(
    identifier="M1",
    description="This is measure 1. It is marked as done. ",
    requirements=[R1, R3],
    deliverables=[D1],
    done=True)

M2 = Measure(
    identifier="M2",
    description="This is measure 2. It has no deliverable defined.",
    requirements=[R1]
)

M3 = Measure(
    identifier="M3",
    description="This is measure 3",
    requirements=[R2],
    deliverables=[D2])

M4 = Measure(
    identifier="M4",
    description="This is measure 4. It helps implement two requirements and affects two deliverables.",
    requirements=[R1, R2],
    deliverables=[D1, D2])

M5 = Measure(
    identifier="M5",
    description="This is measure 4. It is marked completed. It is the only measure for requirement 3. Therefor making "
                "requirement 3 completed. It is also the only measure that affects deliverable 3, thereby completing "
                "that deliverable as well.",
    requirements=[R3],
    deliverables=[D3],
    done=True)
