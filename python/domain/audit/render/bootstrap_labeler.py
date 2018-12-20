"""
    work with labels
"""
from .base_labeler import BaseLabeler


class BootstrapLabeler(BaseLabeler):
    """
    create decorative labels for BirMeasures based on their status
    """
    BOOTSTRAP_LABEL_COLOR_GREY = "default"
    BOOTSTRAP_LABEL_COLOR_RED = "danger"
    BOOTSTRAP_LABEL_COLOR_LIGHT_BLUE = "info"
    BOOTSTRAP_LABEL_COLOR_DARK_BLUE = "primary"
    BOOTSTRAP_LABEL_COLOR_ORANGE = "warning"
    BOOTSTRAP_LABEL_COLOR_GREEN = "success"
