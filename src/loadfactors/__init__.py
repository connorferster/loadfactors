"""
Package for claculation of structural load combinations as per NBCC2020
"""

__version__ = "0.1.0"

from loadfactors.loadfactors import (
    Load,
    open_load_combinations,
    factored_max,
    factored_min,
    factored_max_trace,
    factored_min_trace,
    get_factored_matrix,
    factor_load,
    alias_to_service_loads
)