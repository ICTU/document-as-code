# Document-as-code example

    Requirement = Model
      identifier: 'Identifier'
      description: 'Description'
      sources: 'Sources'

    Source = Model
      identifier: 'Identifier'
      title: 'Title'
      version: 'Version'

    Deliverable = Model
      identifier: 'Identifier'
      title: 'Title'

    Measure = Model
      identifier: 'Identifier'
      description: 'Description'
      requirements: 'Requirements'
      deliverables: 'Deliverables'
      done: 'Done'

    @S1 = Source 'S1', 'This is source 1', '1.0'
    @S2 = Source 'S2', 'This is source 2', '1.1'

    @R1 = Requirement 'R1', 'This is requirement 1', [@S1]
    @R2 = Requirement 'R2', 'This is requirement 2', [@S1, @S2]
    @R3 = Requirement 'R3', 'This is requirement 3', [@S2]

    @D1 = Deliverable 'D1', 'Deliverable 1'
    @D2 = Deliverable 'D2', 'Deliverable 2'
    @D3 = Deliverable 'D3', 'Deliverable 3'

    @M1 = Measure 'M1', 'This is measure one, it is marked as done',
      [@R1, @R3], [@D1], true
    @M2 = Measure 'M2', 'This measure has no deliverable defined',
      [@R1], [], false

This is an example of a document created to illustrate the document-as-code principle. Instead of writing structured documents using a text processor or spreadsheet, the document is generated from a simple program written within a Markdown document. With the help of a generator program the Markdown document is transformed into another valid Markdown document.
The domain model and the contents of the domain are written in Markdown and coffeescript.
The generator replaces the coffeescript in the Markdown document with its corresponding
output.


## Sources

This section lists the example sources for the requirements of the Document-as-code project.

    table [@S1, @S2]

## Requirements

This section lists the example requirements applicable to the Document-as-code project. Each requirement refers back to the source it originates from and refers forward to the measures defined to implement or support the requirement.

    table [@R1, @R2, @R3]

## Deliverables

This section contains the example deliverables that contain or implement the measures.


    table [@D1, @D2, @D3]

## Measures

This section contains the example measures defined to implement or support the requirements of the project.

    table [@M1, @M2]
