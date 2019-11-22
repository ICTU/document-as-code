"""
audit programme

A collection of items to be audited

"""

from domain import base


class AuditItem(base.Base):
    """
    a single item to be audited
    """

    title = None
    summary = None
    description = None

    def __init__(self, identifier, title, summary, description):
        """
        create an audit item
        :param identifier: unique identifier among AuditItems
        :param title: what the audit item is about
        :param summary: short description of the audit item
        :param description: full story of the audit item
        """
        super().__init__(identifier)

        self.title = title
        self.summary = summary
        self.description = description


class AuditProgramme(base.Base):
    """
    a complete audit programme
    """

    title = None
    topic = None
    summary = None
    description = None
    items = None

    def __init__(self, identifier, title, topic, summary, description, *items):
        """
        create an audit programme
        :param title: the audit programme name
        :param topic: what the audit programme is about
        :param summary: short description of the audit programme
        :param description: full story of the audit programme
        :param identifier: unique identifier among AuditProgrammes
        """
        super().__init__(identifier)

        self.title = title
        self.topic = topic
        self.summary = summary
        self.description = description
        self.items = []
        self.add_audit_item(*items)

    def add_audit_item(self, *items):
        """
        convert items to AuditItems and add them to the audit programme
        :param items: collection of AuditItems, AuditItem identifiers or AuditItem parameters
        """
        for nr, item in enumerate(items, len(self.items)+1):
            if isinstance(item, AuditItem):
                converted = item
            elif isinstance(item, str):
                converted = AuditItem.find_instance(item)
                if converted is None:
                    raise ValueError(f"no AuditItem with identifier '{item}'")
            elif len(item) == 3:
                identifier = f"{self.identifier}_{nr:04d}"
                converted = AuditItem(identifier, *item)
            else:
                raise ValueError(f"unable to convert {item!r}")

            self.items.append(converted)
