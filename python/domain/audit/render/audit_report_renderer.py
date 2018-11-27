import pathlib
import contextlib

from domain.audit.model import audit_programme
from domain.audit.model import audit_evidence
from domain.audit.model import audit_report


def render_audit_item(audit_item):
    print(f'  - {audit_item.title}')
    print(f'    {audit_item.summary}')


def render_audit_evidence(evidence):
    def check_mark(item):
        return "V" if item else "X"
    set_up = check_mark(evidence.set_up)
    existence = check_mark(evidence.existence)
    operation = check_mark(evidence.operation)
    print(f'  - {evidence.subject}: {set_up}/{existence}/{operation}')


def render_finding(finding):
    print(f'+ title')
    print(f'    {finding.title}')
    print(f'  description')
    print(f'    {finding.description}')
    print(f'  audit item(s)')
    for audit_item in finding.audit_items:
        render_audit_item(audit_item)
    print(f'  evidence')
    for evidence in finding.evidence:
        render_audit_evidence(evidence)
    print(f'  risk')
    print(f'    {finding.risk}')
    print(f'  recommendation')
    print(f'    {finding.recommendation}')


def render_audit_report(ar):
    print(f'# audit report {ar.title}, identifier: {ar.identifier}')
    print(f'{ar.title}')
    print(f'')
    print(f'summary')
    print(f'  {ar.summary}')
    print(f'')
    print(f'description')
    print(f'  {ar.description}')
    print(f'')
    print(f'findings')
    for finding in ar.findings:
        render_finding(finding)


def render_all_audit_reports():
    """
    output for the current audit report(s)
    """
    for current_audit_report in audit_report.AuditReport.all:
        print("")
        print("")
        render_audit_report(current_audit_report)


def render_audit_report_to_file(output, exists_ok=False):
    """
    create an output file for the audit report(s)
    :param output: path to the file
    :param exists_ok: allow to overwrite existing file
    """
    path = pathlib.Path(output)
    if path.exists() and not exists_ok:
        raise IOError(f"{path} already exists")

    with path.open("w",) as fout:
        with contextlib.redirect_stdout(fout):
            render_all_audit_reports()


if __name__ == "__main__":
    # audit programme
    ai = audit_programme.AuditItem(
        "By Object",
        "Title by object",
        "Summary by object",
        "Description by object",
    )
    audit_programme.AuditItem(
        "By ID",
        "Title #2 by id",
        "Summary #2 by id",
        "Description #2 by id",
    )
    ap = audit_programme.AuditProgramme(
        "AuditProgrammeID",
        "TITLE of AuditProgramme",
        "TOPIC of AuditProgramme",
        "SUMMARY of AuditProgramme",
        "DESCRIPTION of AuditProgramme",
        ("Title in-line", "Summary in-line", "Description in-line"),
        ai,
        "By ID",
    )
    # audit evidence
    audit_evidence.AuditEvidenceElement(
        "SharedAuditEvidenceElementID",
        "DETAIL of AuditEvidenceElement",
        "REFERENCE of AuditEvidenceElement"
    )
    audit_evidence.AuditEvidence(
        "EvidenceID",
        "SUBJECT of evidence",
        set_up=(
            "SharedAuditEvidenceElementID",
            ("SET-UP detail", "SET-UP reference"),
        ),
        existence=(
            "SharedAuditEvidenceElementID",
            ("EXISTENCE detail", "EXISTENCE reference"),
        ),
        operation=(
            ("OPERATION detail", "OPERATION reference"),
            "SharedAuditEvidenceElementID",
        )
    )
    audit_evidence.AuditEvidence(
        "AnotherPieceOfEvidence",
        "Total absence of traces",
    )
    # audit report
    audit_report.AuditFinding(
        "FINDING 0001",
        "TITLE FINDING 0001",
        "DESCRIPTION FINDING 0001",
        risk="RISK FINDING 0001",
        recommendation="RECOMMENDATION FINDING 0001",
        audit_items=(
            ai,
            "By ID",
        ),
        evidence=(
            "EvidenceID",
            "AnotherPieceOfEvidence",
        )
    )
    audit_report.AuditReport(
        "AUDIT REPORT",
        "TITLE of the AUDIT REPORT",
        "SUMMARY of the AUDIT REPORT",
        "DESCRIPTION of the AUDIT REPORT",
        findings=(
            "FINDING 0001",
        )
    )
    # create it
    render_all_audit_reports()
