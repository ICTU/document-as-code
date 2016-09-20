# Document-as-code example

This is an example of a document created to illustrate the document-as-code principle. Instead of writing structured documents using a text processor or spreadsheet, the document is generated from a simple program written within a Markdown document. With the help of a generator program the Markdown document is transformed into another valid Markdown document.
The domain model and the contents of the domain are written in Markdown and coffeescript.
The generator replaces the coffeescript in the Markdown document with it's corresponding
output.

## Sources

This section lists the example sources for the requirements of the Document-as-code project.

| identifier | title | version |
| ---------- | ----- | ------- |
| <a name="S1"></a>S1 | This is source 1 | 1.0 |
| <a name="S2"></a>S2 | This is source 2 | 1.1 |

## Requirements

This section lists the example requirements applicable to the Document-as-code project. Each requirement refers back to the source it originates from and refers forward to the measures defined to implement or support the requirement.

| identifier | description | sources |
| ---------- | ----------- | ------- |
| <a name="R1"></a>R1 | This is requirement 1 | <a href="#S1">S1</a> |
| <a name="R2"></a>R2 | This is requirement 2 | <a href="#S1">S1</a>, <a href="#S2">S2</a> |
| <a name="R3"></a>R3 | This is requirement 3 | <a href="#S2">S2</a> |

## Deliverables

This section contains the example deliverables that contain or implement the measures.

| identifier | title |
| ---------- | ----- |
| <a name="D1"></a>D1 | Deliverable 1 |
| <a name="D2"></a>D2 | Deliverable 2 |
| <a name="D3"></a>D3 | Deliverable 3 |

## Measures

This section contains the example measures defined to implement or support the requirements of the project.

| identifier | description | requirements | deliverables | done |
| ---------- | ----------- | ------------ | ------------ | ---- |
| <a name="M1"></a>M1 | This is measure one, it is marked as done | <a href="#R1">R1</a>, <a href="#R3">R3</a> | <a href="#D1">D1</a> | true |
| <a name="M2"></a>M2 | This measure has no deliverable defined | <a href="#R1">R1</a> |  | false |


