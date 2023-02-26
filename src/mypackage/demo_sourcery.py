import dataclasses
from typing import List


@dataclasses.dataclass
class Sample:
    id: str
    value: int


def get_samples() -> List[Sample]:
    # sourcery example: convert for loop into list comprehension
    samples: List[Sample] = _create_samples()
    selected_samples: List[Sample] = []
    for sample in samples:
        if sample.value > 3:
            selected_samples.append(sample)
    return selected_samples


def _create_samples() -> List[Sample]:
    samples: List[Sample]
    samples = [
        Sample("first", 1),
        Sample("second", 2),
        Sample("third", 3),
        Sample("fourth", 4),
        Sample("fifth", 5),
        Sample("sixth", 6),
    ]
    return samples
