
from typing import List
from config import DIM
from nada_dsl import Output, SecretInteger
import nada_numpy as na


def nada_main() -> List[Output]:

    parties = na.parties(3)

    a = na.array(DIM, parties[0], "A", SecretInteger)

    b = na.array(DIM, parties[1], "B", SecretInteger)

    result = a @ b

    return result.output(parties[2], "my_output")
