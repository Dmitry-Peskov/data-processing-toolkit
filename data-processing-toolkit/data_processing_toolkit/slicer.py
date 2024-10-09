from typing import Any, TypeAlias
from copy import deepcopy

from math import ceil


Listing: TypeAlias = list | tuple[Any] | str | set


def cut_into_slices(sequence: Listing, slice_size: int) -> list[Any]:
    """
    Нарезать последовательность на "ломтики" заданного размера.

    :param sequence: Последовательность, которую необходимо нарезать.
    :param slice_size: Размер каждого ломтика (количество элементов, которые будут включены в один "ломтик").
    :return: Список, содержащий ломтики заданного размера, нарезанные из переданной последовательности.
    """
    result_sequence = []
    processing_sequence = deepcopy(sequence)
    count_elements = len(sequence)
    count_slice = ceil(count_elements / slice_size)
    for _ in range(count_slice):
        result_sequence.append(processing_sequence[:slice_size])
        processing_sequence = processing_sequence[slice_size:]
    return result_sequence
