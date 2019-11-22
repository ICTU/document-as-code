import datetime

from yattag import indent
from format.bootstrap import BootstrapDoc

from domain.audit.model import audit_report

from . import base_labeler


class HtmlRenderer(object):

    doc = None
    tag = None
    txt = None

    def __init__(self):
        super().__init__()
        self.doc, self.tag, self.txt = BootstrapDoc().tagtext()

    def __getattr__(self, item):
        for src in (self.doc, self.tag, self.txt):
            if hasattr(src, item):
                return getattr(src, item)
        raise AttributeError(f"{self.__class__.__name__} has no attribute '{item}'")

    def getvalue(self):
        return indent(self.doc.getvalue())


class AuditReportRenderer(object):

    renderer = None
    labeler = None
    doc = None

    def __init__(self, renderer, labeler_class=None):
        super().__init__()
        self.renderer = renderer
        self.labeler_class = labeler_class if labeler_class is not None else base_labeler.BaseLabeler

    def create_labeler(self, doc):
        if not issubclass(self.labeler_class, base_labeler.BaseLabeler):
            raise TypeError(f"labeler should be a BaseLabeler, not {self.labeler_class.__name__}")
        return self.labeler_class(doc)

    # --- document rendering ---

    def render_audit_items(self, audit_items):
        with self.renderer.tag('table', klass="table"):
            for audit_item in audit_items:
                with self.renderer.tag('tr'):
                    with self.renderer.tag('td'):
                        self.renderer.p(audit_item.title)
                    with self.renderer.tag('td'):
                        self.renderer.p(audit_item.summary)

    def render_audit_evidence_items(self, evidence_items):
        def check_mark(item, required):
            return "V" if item else ("X" if required else "-")

        with self.renderer.tag('table', klass="table"):
            for evidence in evidence_items:
                with self.renderer.tag('tr'):
                    with self.renderer.tag('td'):
                        self.renderer.p(evidence.subject)
                    with self.renderer.tag('td'):
                        self.renderer.p(check_mark(evidence.set_up, evidence.set_up_required))
                    with self.renderer.tag('td'):
                        self.renderer.p(check_mark(evidence.existence, evidence.existence_required))
                    with self.renderer.tag('td'):
                        self.renderer.p(check_mark(evidence.operation, evidence.operation_required))

    def render_finding(self, finding):
        self.renderer.h3("title")
        self.renderer.p(finding.title)
        self.renderer.h3("description")
        self.renderer.p(finding.description)
        self.renderer.h3("audit item(s)")
        self.render_audit_items(finding.audit_items)
        self.renderer.h3("evidence")
        self.render_audit_evidence_items(finding.evidence)
        self.renderer.h3("risk")
        self.renderer.p(finding.risk)
        self.renderer.h3("recommendation")
        self.renderer.p(finding.recommendation)

    def render_audit_items_full(self, findings):
        all_audit_items_in_report = set()
        for finding in findings:
            all_audit_items_in_report.update(finding.audit_items)

        for audit_item in sorted(all_audit_items_in_report, key=lambda i: i.title.lower()):
            self.renderer.h2(audit_item.title)
            with self.renderer.tag('table', klass="table"):
                with self.renderer.tag('tr'):
                    with self.renderer.tag('td'):
                        self.renderer.p(audit_item.summary)
                    with self.renderer.tag('td'):
                        self.renderer.p(audit_item.description)

    def _render_evidence_elements(self, label, evidence_elements, required):
        self.renderer.h3(label)
        if not required:
            self.renderer.p("no evidence required")
        elif not evidence_elements:
            self.renderer.p("no evidence registered")

        if not evidence_elements:
            return

        with self.renderer.tag('table', klass="table"):
            for element in evidence_elements:
                with self.renderer.tag('tr'):
                    with self.renderer.tag('td'):
                        self.renderer.p(element.detail)
                    with self.renderer.tag('td'):
                        self.renderer.p(element.reference)

    def render_audit_evidence_full(self, findings):
        all_audit_evidence_in_report = set()
        for finding in findings:
            all_audit_evidence_in_report.update(finding.evidence)

        for evidence in sorted(all_audit_evidence_in_report, key=lambda i: i.subject.lower()):
            self.renderer.h2(evidence.subject)
            self._render_evidence_elements("set-up", evidence.set_up, evidence.set_up_required)
            self._render_evidence_elements("existence", evidence.existence, evidence.existence_required)
            self._render_evidence_elements("operation", evidence.operation, evidence.operation_required)

    def render_audit_report(self, ar):
        """
        output for a single audit report
        :param ar: audit report
        """
        with self.renderer.tag('html'):
            self.renderer.head("Audit Report")

            with self.renderer.tag('body'):
                self.renderer.p(f"# audit report {ar.title}, identifier: {ar.identifier}")
                with self.renderer.tag('div', klass='container'):
                    self.renderer.h1(f"{ar.title}")
                    self.renderer.h2(f"summary")
                    self.renderer.p(f"{ar.summary}")
                    self.renderer.h2(f"description")
                    self.renderer.p(f"{ar.description}")
                    self.renderer.h2(f"findings")
                    for finding in ar.findings:
                        self.render_finding(finding)
                with self.renderer.tag('div', klass='container'):
                    self.renderer.h1("Appendix A - Audit Items")
                    self.render_audit_items_full(ar.findings)
                with self.renderer.tag('div', klass='container'):
                    self.renderer.h1("Appendix B - Findings")
                    self.render_audit_evidence_full(ar.findings)
                self.renderer.p(f"# rendered on {datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")
