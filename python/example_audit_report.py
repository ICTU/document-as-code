import pathlib

from domain.audit.model import audit_programme
from domain.audit.model import audit_evidence
from domain.audit.model import audit_report

from domain.audit.render import audit_report_renderer


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
        ),
        operation_required = False,
    )
    audit_evidence.AuditEvidence(
        "AnotherPieceOfEvidence",
        "Total absence of traces",
        operation_required=False,
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
    ar = audit_report.AuditReport(
        "AUDIT REPORT",
        "TITLE of the AUDIT REPORT",
        "SUMMARY of the AUDIT REPORT",
        "DESCRIPTION of the AUDIT REPORT",
        findings=(
            "FINDING 0001",
        )
    )

    # create it
    path = pathlib.Path(__file__).resolve().with_suffix(".html")

    renderer = audit_report_renderer.HtmlRenderer()
    audit_report_renderer.AuditReportRenderer(renderer).render_audit_report(ar)
    report = renderer.getvalue()

    path.write_text(report)
    print(report)
