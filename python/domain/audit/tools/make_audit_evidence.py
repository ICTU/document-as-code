import pathlib
import contextlib

from domain.audit.model import audit_programme


def preamble():
    """
    stuff required to make audit evidence work
    """
    print("import domain.audit.model.audit_evidence as audit_evidence")


def evidence_template_for_audit_programme(ap):
    """
    evidence template for a single audit programme
    :param ap: audit programme to generate template for
    """
    print(f'# audit programme {ap.title}, identifier: {ap.identifier}')
    for item in ap.items:
        print(f'')
        print(f'AuditEvidence(')
        print(f'    "{item.identifier}",  # used for matching, do not change')
        print(f'    "{item.title}",')
        print(f'     set_up=(')
        print(f'         ("detail", "reference"),')
        print(f'     ),')
        print(f'     existence=(')
        print(f'         ("detail", "reference"),')
        print(f'     ),')
        print(f'     operation=(')
        print(f'         ("detail", "reference"),')
        print(f'     ),')
        print(f')')


def evidence_template():
    """
    evidence template for the current audit programme(s)
    """
    for current_audit_programme in audit_programme.AuditProgramme.all:
        print("")
        print("")
        evidence_template_for_audit_programme(current_audit_programme)


def final():
    """
    stuff to complete the audit evidence
    """
    print("")


def make_evidence_template():
    """
    create evidence template for the audit programme(s)
    """
    preamble()
    evidence_template()
    final()


def make_evidence_template_file(output, exists_ok=False):
    """
    create an evidence template file for the audit programme(s)
    :param output: path to the file
    :param exists_ok: allow to overwrite existing file
    """
    path = pathlib.Path(output)
    if path.exists() and not exists_ok:
        raise IOError(f"{path} already exists")

    with path.open("w",) as fout:
        with contextlib.redirect_stdout(fout):
            make_evidence_template()


if __name__ == "__main__":
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
    make_evidence_template()
