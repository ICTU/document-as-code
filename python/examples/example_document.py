"""
    example document - demonstrate how 'Document as Code' works
"""
import pathlib

from yattag import indent

from domain.quality_plan import model, content
from format.bootstrap import BootstrapDoc


doc, tag, text = BootstrapDoc().tagtext()


with tag('html'):

    doc.head(content.title)

    with tag('body'):

        with tag('div', klass='container'):

            doc.h1(content.title, content.version + ', ' + content.date)
            doc.p(content.intro, klass='lead')
            doc.p(content.reading_guide)

            doc.h2('Sources', doc.badge(model.Source.all))
            doc.p(content.intro_sources)
            doc.table(
                ('Id', 'Title', 'Version', 'Requirements'),
                [
                    (
                        doc.bookmark(source.identifier),
                        source.title,
                        source.version,
                        [doc.link(requirement.identifier) for requirement in model.Requirement.from_source(source)]
                    )
                    for source in model.Source.all
                ]
            )

            doc.h2('Requirements', doc.badge(model.Requirement.all))
            doc.p(content.intro_requirements)
            doc.table(
                ('Id', 'Description', 'Sources', 'Measures', 'Status'),
                [
                    (
                        doc.bookmark(requirement.identifier),
                        requirement.description,
                        [doc.link(source.identifier) for source in requirement.sources],
                        [doc.link(measure.identifier) for measure in model.Measure.for_requirement(requirement)],
                        doc.label('Completed', 'success')
                            if model.Measure.all_completed_for_requirement(requirement)
                            else doc.label('No measures', 'warning')
                                if not model.Measure.for_requirement(requirement)
                                else ''
                    )
                    for requirement in model.Requirement.all
                ]
            )

            doc.h2('Measures', doc.badge(model.Measure.all))
            doc.p(content.intro_measures)
            doc.table(
                ('Id', 'Description', 'Requirements', 'Deliverables', 'Status'),
                [
                    (
                        doc.bookmark(measure.identifier),
                        measure.description,
                        [doc.link(requirement.identifier) for requirement in measure.requirements],
                        [doc.link(deliverable.identifier) for deliverable in measure.deliverables],
                        doc.label('Completed', 'success') if measure.done else ''
                    )
                    for measure in model.Measure.all
                ]
            )

            doc.h2('Deliverables', doc.badge(model.Deliverable.all))
            doc.p(content.intro_deliverables)
            doc.table(
                ('Id', 'title', 'Measures', 'Status'),
                [
                    (
                        doc.bookmark(deliverable.identifier),
                        deliverable.title,
                        [doc.link(measure.identifier) for measure in model.Measure.for_deliverable(deliverable)],
                        doc.label('Completed', 'success')
                            if model.Measure.all_completed_for_deliverable(deliverable)
                            else ''
                    )
                    for deliverable in model.Deliverable.all
                ]
            )

# create it
file_path = pathlib.Path(__file__).resolve()
project_home_dir = file_path.resolve().parent.parent.parent
report_dir = project_home_dir / "report"
report_dir.mkdir(parents=True, exist_ok=True)
report_file = report_dir / file_path.with_suffix(".html").name

report_file.write_text(indent(doc.getvalue()))
print(f"Output in {report_file}")
