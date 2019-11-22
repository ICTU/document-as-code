"""
    work with labels
"""


class BaseLabeler(object):
    """
    create decorative labels for BirMeasures based on their status
    """

    STYLE_LABEL = "font-size:11px"

    # ---

    doc = None

    def __init__(self, doc):
        self.doc = doc

    # --- sorting ---

    def XXX_sort_key(self, XXX):
        """
        compute a sort key for a XXX
        :param XXX: the XXX
        :return: int
        """
        pass

    # --- label rendering ---

    def _measure_to_label_data(self, measure):
        """
        create a label for a measure
        both the label text and its visual level determined from the measure and its state
        :param measure: the measure
        :return: label text, visual level
        """
        if measure in self._label_data:
            return self._label_data[measure]

        if measure.done:
            return measure.identifier, self.COLOR_MEASURE_DONE

        return measure.identifier, self.COLOR_MEASURE_BUSY

    def measure_to_label(self, measure):
        """
        determine correct label presentation of a measure
        :param measure: the measures
        :return: list of labels (label text, visual level)
        """
        return self._make_label(*self._measure_to_label_data(measure), measure.url)

    def measures_to_labels(self, measures):
        """
        turn a collection of measures into a properly sorted list of formatted labels for those measures
        :param measures: the measures
        :return: list of formatted labels
        """
        return [self.measure_to_label(m) for m in sorted(measures, key=self.measure_sort_key)]

    # --- fragment ---

    def fragment_to_labels(self, fragment):
        """
        turn a document fragment into the proper set of labels to adorn it
        :param fragment: the document fragment
        :return: labels
        """
        bbn = self.bbn_to_labels(fragment.bbn) if hasattr(fragment, 'bbn') else None
        labels = self.measures_to_labels(fragment.bir_measures)

        if bbn:
            return bbn + [" &nbsp; "] + labels

        return labels

    # --- basic label creation ---

    def _make_label(self, text, level, url=None):
        """
        make a text label with a level indication
        :param text: text to put on the label
        :param level: level to indicate through the label
        :param url: reference to a (part of a) web page
        :return: a label
        """
        label = self.doc.label(text, level, style=self.STYLE_LABEL)
        if url is None:
            return label
        return self.doc.link(f"{label}", url=url)
