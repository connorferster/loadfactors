"""
Package for claculation of structural load combinations as per NBCC2020
"""

__version__ = "0.1.0"

from loadfactors.loadfactors import (Load, alias_to_service_loads, factor_load,
                                     factored_max, factored_max_trace,
                                     factored_min, factored_min_trace,
                                     get_factored_matrix,
                                     open_load_combinations)
