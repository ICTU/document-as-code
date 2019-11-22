"""
audit report - reports results of an audit
"""

from domain import base
from . import audit_evidence
from . import audit_programme


class AuditFinding(base.Base):
    """
    An audit finding
    """

    title = None
    description = None
    risk = None
    recommendation = None
    audit_items = None
    evidence = None

    def __init__(self, identifier, title, description, *, risk, recommendation, audit_items=None, evidence=None):
        """
        a finding and its consequences
        :param identifier: unique identifier for this finding
        :param title: subject of the finding
        :param description: text for the finding
        :param risk: risk associated with the finding
        :param recommendation: how to resolve the issue
        :param audit_items: collection of audit items in the audit programme
        :param evidence: where evidence can be found
        """
        super().__init__(identifier)

        self.title = title
        self.description = description
        self.risk = risk
        self.recommendation = recommendation
        self.audit_items = []
        self.evidence = []
        if audit_items:
            self.add_audit_items(*audit_items)
        if evidence:
            self.add_evidence(*evidence)

    def add_audit_items(self, *audit_items):
        """
        add AuditItems to the audit finding
        :param audit_items: collection of AuditItems, or AuditItem identifiers
        """
        for item in audit_items:
            if isinstance(item, audit_programme.AuditItem):
                converted = item
            elif isinstance(item, str):
                converted = audit_programme.AuditItem.find_instance(item)
                if converted is None:
                    raise ValueError(f"no AuditItem with identifier '{item}'")
            else:
                raise ValueError(f"unable to convert {item!r}")

            self.audit_items.append(converted)

    def add_evidence(self, *evidence):
        """
        add AuditEvidence to the audit finding
        :param evidence: collection of AuditEvidences, or AuditEvidence identifiers
        """
        for item in evidence:
            if isinstance(item, audit_evidence.AuditEvidence):
                converted = item
            elif isinstance(item, str):
                converted = audit_evidence.AuditEvidence.find_instance(item)
                if converted is None:
                    raise ValueError(f"no AuditItem with identifier '{item}'")
            else:
                raise ValueError(f"unable to convert {item!r}")

            self.evidence.append(converted)


class AuditReport(base.Base):
    """
    an audit report
    """

    title = None
    summary = None
    description = None
    findings = None

    def __init__(self, identifier, title, summary, description, *, findings):
        """
        an audit report
        :param identifier: unique identifier for this report
        :param title: subject of the report
        :param summary: for those who do not read
        :param description: text for the report
        :param findings: elements of the report
        """
        super().__init__(identifier)

        self.title = title
        self.summary = summary
        self.description = description
        self.findings = []
        self.add_findings(*findings)

    def add_findings(self, *findings):
        """
        add AuditFindings to the audit report
        :param findings: collection of AuditFindings, or AuditFinding identifiers
        """
        for item in findings:
            if isinstance(item, AuditFinding):
                converted = item
            elif isinstance(item, str):
                converted = AuditFinding.find_instance(item)
                if converted is None:
                    raise ValueError(f"no AuditFinding with identifier '{item}'")
            else:
                raise ValueError(f"unable to convert {item!r}")

            self.findings.append(converted)
