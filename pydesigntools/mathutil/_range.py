"""Provides a range that can handle floating point values.
"""
from ._types import Numeric


class Range:
    """Provides a simple representation of a range that can test for a number
    value on that range.

    By default, the range includes the minimum value and excludes the maximum
    value when testing for inclusion: [minimum, maximum). This behavior can be
    changed via constructor parameters.

    Args:
        min_value: The minimum value for this range.
        max_value: The maximum value for this range.
        min_inclusive: If ``True`` (default), the minimum value will be
            included when testing if a value is present on the range.
        max_inclusive: If ``False`` (default), the maximum value will be
            excluded when testing if a value is present on the range.

    Raises:
        ValueError: If ``min_value`` is not less than ``max_value``
    """

    __slots__ = ("_min", "_max", "_min_inclusive", "_max_inclusive")

    def __init__(
        self,
        min_value: Numeric,
        max_value: Numeric,
        min_inclusive: bool = True,
        max_inclusive: bool = False,
    ):
        self._min = min_value
        self._max = max_value

        if max_value <= min_value:
            raise ValueError("Maximum must be greater than minimum")

        self._min_inclusive = min_inclusive
        self._max_inclusive = max_inclusive

    @property
    def min(self) -> Numeric:
        """The minimum value for this range."""
        return self._min

    @property
    def max(self) -> Numeric:
        """The maximum value for this range."""
        return self._max

    @property
    def min_inclusive(self) -> bool:
        """Whether the minimum value will be included when testing if a value
        is present on the range."""
        return self._min_inclusive

    @property
    def max_inclusive(self) -> bool:
        """Whether the maximum value will be included when testing if a value
        is present on the range."""
        return self._max_inclusive

    def __contains__(self, value: Numeric) -> bool:
        """Tests if the given value is present in this range.

        Args:
            value: The value to test.

        Returns:
            ``True`` if ``value`` is within this range, ``False`` if it is not.
        """
        upper = self.min <= value if self.min_inclusive else self.min < value
        lower = value <= self.max if self.max_inclusive else value < self.max

        return upper and lower

    def __repr__(self) -> str:
        return (
            f"Range({self.min}, {self.max}, {self.min_inclusive}, {self.max_inclusive})"
        )

    def __str__(self) -> str:
        lower = "[" if self.min_inclusive else "("
        upper = "]" if self.max_inclusive else ")"

        return f"Range {lower}{self.min}, {self.max}{upper}"
