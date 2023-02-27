import dataclasses
from typing import List


@dataclasses.dataclass
class Sample:
    id: str
    value: float


def select_samples() -> List[Sample]:
    # sourcery example: convert for loop into list comprehension
    samples: List[Sample] = _create_samples()
    samples_selected: List[Sample] = [sample for sample in samples if sample.value > 3]
    return samples_selected


def _create_samples() -> List[Sample]:
    samples: List[Sample]
    samples = [
        Sample("first", 1.0),
        Sample("second", 2.0),
        Sample("third", 3.0),
        Sample("fourth", 4.0),
        Sample("fifth", 5.0),
        Sample("sixth", 6.0),
    ]
    return samples
