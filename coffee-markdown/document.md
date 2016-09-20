
# Sources

In this chapter we define the sources.

    Source = Model
      identifier: 'Identifier'
      title: 'Title'
      version: 'Version'

    @S1 = Source 'S1', 'This is source 1', '1.0'
    @S2 = Source 'S2', 'This is source 2', '1.1'

    table [@S1, @S2]

# Deliverables

In this chapter we define the deliverables.

    Deliverable = Model
      identifier: 'Identifier'
      title: 'Title'

    @D1 = Deliverable 'D1', 'Deliverable 1'
    @D2 = Deliverable 'D2', 'Deliverable 2'
    @D3 = Deliverable 'D3', 'Deliverable 3'

    table [@D1, @D2, @D3]

# Requirements

In this chapter we define the requirements

    Requirement = Model
      identifier: 'Identifier'
      description: 'Description'
      sources: 'Sources'

    @R1 = Requirement 'R1', 'This is requirement 1', [@S1]
    @R2 = Requirement 'R2', 'This is requirement 2', [@S1, @S2]

    table [@R1, @R2]


# Measures

In this chapter we define the measures.
