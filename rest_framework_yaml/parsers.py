"""Provides YAML parsing support."""

from typing import IO, Any, Dict, Mapping, Optional

import yaml
from django.conf import settings
from django.utils.encoding import force_str
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser


class YAMLParser(BaseParser):
    """Parse YAML-serialized data."""

    media_type = "application/yaml"

    # ruff: noqa: ARG002
    def parse(
        self,
        stream: IO[Any],
        media_type: Optional[str] = None,
        parser_context: Optional[Mapping[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Parse the incoming bytestream as YAML and returns the resulting data."""
        parser_context = parser_context or {}
        encoding = parser_context.get("encoding", settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            parsed_data = yaml.safe_load(data)

        except (ValueError, yaml.parser.ParserError) as exc:
            raise ParseError("YAML parse error - %s" % force_str(exc)) from exc

        if not isinstance(parsed_data, dict):
            raise ParseError("Expected dict, got %s" % type(parsed_data))

        return parsed_data
