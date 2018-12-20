"""
audit evidence - document evidence in an audit

AuditEvidence consists of elements found during research.
Grouped together the evidence elements are the evidence of the set-up, existence, or operation
of an audit topic.

combined_use = AuditEvidenceElement(
    "EXTERNAL AUDITOR 007",
    "Trusty Audit Report YYYY",
    "secret stash on 4th floor"
)

AuditEvidence(
    "ID0001",
    "Procedure to xxxxx",
    set_up=(
        combined_use,
        ("procedure documentation", "http://intranet/procedures/xxxxx"),
    ),
    existence=(
        combined_use,
    ),
    operation=(
        ("log files", "/logs/xxxxx on archive host"),
        combined_use,
    )
)
"""

from domain import base


class AuditEvidenceElement(base.Base):
    """
    An element of evidence
    """
    detail = None
    reference = None

    def __init__(self, identifier, detail, reference):
        """
        an element of evidence
        :param identifier: unique identifier for this evidence element
        :param detail: subject detail of the evidence
        :param reference: where evidence can be found
        """
        super().__init__(identifier)
        self.detail = detail
        self.reference = reference


class AuditEvidence(base.Base):
    """
    All evidence about a topic
    """
    subject = None
    set_up = None
    existence = None
    operation = None
    set_up_required = None
    existence_required = None
    operation_required = None

    def __init__(self, identifier, subject, *, set_up=None, existence=None, operation=None,
                 set_up_required=True, existence_required=True, operation_required=True):
        """
        register a piece of evidence
        :param identifier: unique identifier for this piece of evidence
        :param subject: subject of the evidence
        :param set_up: elements supporting set-up
        :param existence: elements supporting existence
        :param operation: elements supporting operation
        """
        super().__init__(identifier)
        self.subject = subject
        self.set_up = []
        self.existence = []
        self.operation = []
        self.set_up_required = set_up_required
        self.existence_required = existence_required
        self.operation_required = operation_required

        if set_up:
            self.add_setup(*set_up)
        if existence:
            self.add_existence(*existence)
        if operation:
            self.add_operation(*operation)

    def add_setup(self, *items):
        self._convert_add_evidence_elements(self.set_up, "S", *items)

    def add_existence(self, *items):
        self._convert_add_evidence_elements(self.existence, "X", *items)

    def add_operation(self, *items):
        self._convert_add_evidence_elements(self.operation, "O", *items)

    def _convert_add_evidence_elements(self, evidence_elements, key, *items):
        """
        convert parameters to true EvidenceElements
        :param evidence_elements: list of EvidenceElements
        :param key: kind of evidence
        :param items: collection of EvidenceElements, EvidenceElement identifiers or EvidenceElement parameters
        """
        identifier_maker = f"{self.identifier}_{key}_{{:04d}}"

        for nr, item in enumerate(items, len(evidence_elements)+1):
            if isinstance(item, AuditEvidenceElement):
                converted = item
            elif isinstance(item, str):
                converted = AuditEvidenceElement.find_instance(item)
                if converted is None:
                    raise ValueError(f"no AuditItem with identifier '{identifier}'")
            elif len(item) == 2:
                identifier = identifier_maker.format(nr)
                converted = AuditEvidenceElement(identifier, *item)
            else:
                raise ValueError(f"unable to convert {item!r}")

            evidence_elements.append(converted)

    @property
    def is_covered(self):
        """
        are set-up, existence, and operation covered?
        :return:
        """
        return len(self.set_up) > 0 and len(self.existence) > 0 and len(self.operation) > 0
