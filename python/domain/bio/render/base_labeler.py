"""
    work with labels
"""


class BaseLabeler(object):
    """
    create decorative labels for BioMeasures based on their status
    """
    LABEL_TODO = "todo"
    LABEL_EXPLAIN = "explain"
    LABEL_NA = "nvt"

    COLOR_TODO = None
    COLOR_EXPLAIN = None
    COLOR_NA = None

    COLOR_MEASURE_BUSY = None
    COLOR_MEASURE_DONE = None

    COLOR_BBN_UNKNOWN = None
    COLOR_BBN_EXCLUDE = None
    COLOR_BBN_INCLUDE = None

    SORT_TODO = 1
    SORT_EXPLAIN = 7
    SORT_NA = 9
    SORT_DEFAULT = 3

    STYLE_LABEL = "font-size:11px"

    # ---

    todo = None
    explain = None
    not_applicable = None

    _label_data = None
    _label_sort_order = None

    doc = None

    def __init__(self, doc, todo, explain, not_applicable):
        self.doc = doc
        self.todo = todo
        self.explain = explain
        self.not_applicable = not_applicable

        self._label_data = self.create_label_data()
        self._bbn_label_data = self.create_bbn_labels()

        self._label_sort_order = self.create_sort_order()

    # ---

    def create_label_data(self):
        return {
            self.todo:           (self.LABEL_TODO, self.COLOR_TODO),
            self.explain:        (self.LABEL_EXPLAIN, self.COLOR_EXPLAIN),
            self.not_applicable: (self.LABEL_NA, self.COLOR_NA),
        }

    def create_bbn_labels(self):
        return [
            (('?', self.COLOR_BBN_UNKNOWN), ('?', self.COLOR_BBN_UNKNOWN), ('?', self.COLOR_BBN_UNKNOWN)),
            (('1', self.COLOR_BBN_INCLUDE), ('2', self.COLOR_BBN_INCLUDE), ('3', self.COLOR_BBN_INCLUDE)),
            (('-', self.COLOR_BBN_EXCLUDE), ('2', self.COLOR_BBN_INCLUDE), ('3', self.COLOR_BBN_INCLUDE)),
            (('-', self.COLOR_BBN_EXCLUDE), ('-', self.COLOR_BBN_EXCLUDE), ('3', self.COLOR_BBN_INCLUDE)),
        ]

    # ---

    def create_sort_order(self):
        return {
            self.todo:           self.SORT_TODO,
            self.explain:        self.SORT_EXPLAIN,
            self.not_applicable: self.SORT_NA,
        }

    # --- sorting ---

    def measure_sort_key(self, measure):
        """
        compute a sort key for a measure
        :param measure: the measure
        :return: int
        """
        return self._label_sort_order.get(measure, self.SORT_DEFAULT), measure.identifier

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

    # --- protection level label ---

    def bbn_to_labels(self, bbn):
        """
        turns a basic protection level (BBN) into a formatted label
        :param bbn: basic protection level
        :return: formatted label
        """
        if not bbn:
            return []

        bbn_labels = self._bbn_label_data[bbn if 1 <= bbn <= 3 else 0]
        return [self._make_label(x, lvl) for x, lvl in bbn_labels]

    # --- fragment ---

    def fragment_to_labels(self, fragment):
        """
        turn a document fragment into the proper set of labels to adorn it
        :param fragment: the document fragment
        :return: labels
        """
        bbn = self.bbn_to_labels(fragment.bbn) if hasattr(fragment, 'bbn') else None
        labels = self.measures_to_labels(fragment.bio_measures)

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
        return self.doc.link("{label}", url=url).format(label=label)
