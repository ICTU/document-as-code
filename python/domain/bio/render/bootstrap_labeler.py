"""
    work with labels
"""
from .base_labeler import BaseLabeler


class BootstrapLabeler(BaseLabeler):
    """
    create decorative labels for BioMeasures based on their status
    """
    BOOTSTRAP_LABEL_COLOR_GREY = "default"
    BOOTSTRAP_LABEL_COLOR_RED = "danger"
    BOOTSTRAP_LABEL_COLOR_LIGHT_BLUE = "info"
    BOOTSTRAP_LABEL_COLOR_DARK_BLUE = "primary"
    BOOTSTRAP_LABEL_COLOR_ORANGE = "warning"
    BOOTSTRAP_LABEL_COLOR_GREEN = "success"

    COLOR_TODO = BOOTSTRAP_LABEL_COLOR_RED
    COLOR_EXPLAIN = BOOTSTRAP_LABEL_COLOR_LIGHT_BLUE
    COLOR_NA = BOOTSTRAP_LABEL_COLOR_GREY

    COLOR_MEASURE_BUSY = BOOTSTRAP_LABEL_COLOR_ORANGE
    COLOR_MEASURE_DONE = BOOTSTRAP_LABEL_COLOR_GREEN

    COLOR_BBN_UNKNOWN = BOOTSTRAP_LABEL_COLOR_RED
    COLOR_BBN_EXCLUDE = BOOTSTRAP_LABEL_COLOR_GREY
    COLOR_BBN_INCLUDE = BOOTSTRAP_LABEL_COLOR_DARK_BLUE
