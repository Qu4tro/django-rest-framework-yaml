"""Helper classes for parsers."""
import decimal
import types
from collections import OrderedDict

import yaml
from django.utils.encoding import force_str
from rest_framework.relations import Hyperlink
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList


class SafeDumper(yaml.SafeDumper):
    """
    Dumper subclass that handles commonly used DRF types.

    These are the supported types:
    - Decimal is represented as a string.
    - OrderedDict is represented as a dict.
    - Hyperlink is represented as a string.
    - ReturnDict is represented as a dict.
    - ReturnList is represented as a list.
    - Generators are represented as a list.
    """

    def represent_decimal(self, data: decimal.Decimal) -> yaml.ScalarNode:
        """Represent decimal as a YAML string."""
        return self.represent_scalar("tag:yaml.org,2002:str", force_str(data))


SafeDumper.add_representer(decimal.Decimal, SafeDumper.represent_decimal)

SafeDumper.add_representer(OrderedDict, yaml.representer.SafeRepresenter.represent_dict)

SafeDumper.add_representer(Hyperlink, yaml.representer.SafeRepresenter.represent_str)

SafeDumper.add_representer(ReturnDict, yaml.representer.SafeRepresenter.represent_dict)

SafeDumper.add_representer(ReturnList, yaml.representer.SafeRepresenter.represent_list)

SafeDumper.add_representer(
    types.GeneratorType,
    yaml.representer.SafeRepresenter.represent_list,
)
