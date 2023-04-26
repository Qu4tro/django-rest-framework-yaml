"""Provides YAML rendering support."""

from typing import Any, Mapping, Optional

import yaml
from rest_framework.renderers import BaseRenderer

from .encoders import SafeDumper


class YAMLRenderer(BaseRenderer):
    """Renderer which serializes to YAML."""

    media_type = "application/yaml"
    format = "yaml"
    encoder = SafeDumper
    charset = "utf-8"
    ensure_ascii = False
    default_flow_style = False
    sort_keys = False

    def render(
        self,
        data: Any,
        _accepted_media_type: Optional[str] = None,
        _renderer_context: Optional[Mapping[str, Any]] = None,
    ) -> Any:
        """Render `data` into serialized YAML."""
        if data is None:
            return ""

        return yaml.dump(
            data,
            sort_keys=self.sort_keys,
            stream=None,
            encoding=self.charset,
            Dumper=self.encoder,
            allow_unicode=not self.ensure_ascii,
            default_flow_style=self.default_flow_style,
        )
