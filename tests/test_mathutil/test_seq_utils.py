import unittest

from designtools.mathutil import (
    fmod_sequence,
    ratio_sequence,
    round_sequence,
    scale_sequence,
)

# ----------------------------------------------------------------------------
# Scale parameters mapped to expected output.
DATA_SCALE_SEQUENCE = {
    ((1, 2, 3, 4, 5), 6, 2): (2, 4, 6, 8, 10),
    ((1.0, 2.0, 3.0), 10.0, 0): (10.0, 20.0, 30.0),
    ((1, 2, 3, 4, 5), 0.5): (
        0.16666666666666666, 0.33333333333333331, 0.5, 0.66666666666666663,
        0.83333333333333326),
    ((0, 1, 2, 3, 4), 100, 0): (0, 1, 2, 3, 4)
}


class ScaleSequenceTest(unittest.TestCase):
    def test_scale_sequence(self):
        for params, expect in DATA_SCALE_SEQUENCE.items():
            with self.subTest(f"{params} -> {expect}"):
                self.assertSequenceEqual(scale_sequence(*params), expect)


# ----------------------------------------------------------------------------
# Ratio parameters mapped to expected output
DATA_RATIO_SEQUENCE = {
    (10, 2, 3): (1.25, 2.5, 5.0, 10, 20, 40, 80),
    (1, 1, 2): (1, 1, 1, 1, 1),
    (5, 5, 0): (5,),
    (5, 5, 1): (1, 5, 25)
}


class RatioSequenceTest(unittest.TestCase):
    def test_ratio_sequence(self):
        for params, expect in DATA_RATIO_SEQUENCE.items():
            with self.subTest(f"{params} -> {expect}"):
                self.assertSequenceEqual(ratio_sequence(*params), expect)


# ----------------------------------------------------------------------------
# Sequences mapped to expected rounded integer sequences
DATA_ROUND_INTS = {
    (5.1, 11.9, 3.5, 4.5): (5, 12, 4, 4),
    (-3.5, 0.0, 3.5): (-4, 0, 4),
    (1,): (1,),
    (2.5123, 6.2815, 43.1412, -0.2311): (3, 6, 43, 0)
}

# ----------------------------------------------------------------------------
# Sequences mapped to expected digit-rounded float sequences.
DATA_ROUND_DIGITS = {
    ((2.5123, 6.2815, 43.1412, -0.2311), 2): (2.51, 6.28, 43.14, -0.23),
    ((5.1123, 11.9412, 3.5572, 4.5), 2): (5.11, 11.94, 3.56, 4.5),
    ((5.1, 11.9, 3.5, 4.5), 0): (5, 12, 4, 4),
    ((1, 2, 3), 2): (1, 2, 3)
}


class RoundSequenceTest(unittest.TestCase):
    def test_round_seq_int(self):
        for seq, expect in DATA_ROUND_INTS.items():
            with self.subTest(f"{seq} -> {expect}"):
                self.assertSequenceEqual(round_sequence(seq), expect)

    def test_round_seq_digits(self):
        for params, expect in DATA_ROUND_DIGITS.items():
            with self.subTest(f"{params} -> {expect}"):
                self.assertSequenceEqual(round_sequence(*params), expect)


# ----------------------------------------------------------------------------
# Maps sequences to expected fmod sequence.
DATA_FMOD_SEQUENCE = {
    ((180.5, 45.32, 27, 382, 522), 360.0): (180.5, 45.32, 27.0, 22.0, 162.0),
    ((180, 45, 27, 382, 522), 360): (180, 45, 27, 22, 162),
    ((180.5, 45.32, 27), 360.0): (180.5, 45.32, 27),
    ((180, 45, 27), 360): (180, 45, 27)
}


class FmodSequenceTest(unittest.TestCase):
    def test_fmod_seq(self):
        for params, expect in DATA_FMOD_SEQUENCE.items():
            with self.subTest(f"{params} -> {expect}"):
                self.assertSequenceEqual(fmod_sequence(*params), expect)


if __name__ == "__main__":
    unittest.main()
