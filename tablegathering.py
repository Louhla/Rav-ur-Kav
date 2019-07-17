"""Gathers all data to dataframes"""

import pandas as pd
from history import a
import numpy as np
from user_generator import UserRandomizer

user_generator = UserRandomizer(a)
passenger = user_generator.generate_passenger()

