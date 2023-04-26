"""Tests for the YAML Renderer."""

from decimal import Decimal
from io import BytesIO

from django.test import TestCase
from rest_framework.relations import Hyperlink

from rest_framework_yaml.parsers import YAMLParser
from rest_framework_yaml.renderers import YAMLRenderer


class _YAMLRendererTests(TestCase):
    """Tests specific to the YAML Renderer."""

    def test_render(self) -> None:
        """
        Rendering test.

        Given:
            - A simple dict with a list of strings
            - The YAML representation of that dict as a string
        Do:
            - Render the dict to YAML
        Expect:
            - The YAML string to be the same as the original YAML string
        """
        _yaml_repr = "foo:\n- bar\n- baz\n"

        obj = {"foo": ["bar", "baz"]}

        renderer = YAMLRenderer()
        content = renderer.render(obj, "application/yaml")

        self.assertEqual(content.decode("utf-8"), _yaml_repr)

    def test_render_and_parse(self) -> None:
        """
        Rendering and parsing test.

        Given:
            - A simple dict with a list of strings
        Do:
            - Render the dict to YAML
            - Parse the YAML back to a dict
        Expect:
            - The parsed dict to be the same as the original dict
        """
        obj = {"foo": ["bar", "baz"]}

        renderer = YAMLRenderer()
        parser = YAMLParser()

        content = renderer.render(obj, "application/yaml")
        data = parser.parse(BytesIO(content))
        self.assertEqual(obj, data)

    def test_render_decimal(self) -> None:
        """
        YAML decimal rendering test.

        Given:
            - A dict with a decimal
        Do:
            - Render the dict to YAML
        Expect:
            - The YAML string to contain the decimal as a string
        """
        renderer = YAMLRenderer()
        content = renderer.render(
            {"field": Decimal("111.2")},
            "application/yaml",
        )
        self.assertIn("field: '111.2'", content.decode("utf-8"))

    def test_render_hyperlink(self) -> None:
        """
        YAML Hyperlink rendering test.

        Given:
            - A dict with a Hyperlink
        Do:
            - Render the dict to YAML
        Expect:
            - The YAML string to contain the Hyperlink as a string
        """
        renderer = YAMLRenderer()
        content = renderer.render(
            {"field": Hyperlink("http://pépé.com?great-answer=42", "test")},
            "application/yaml",
        )
        self.assertIn(
            "field: http://pépé.com?great-answer=42",
            content.decode("utf-8"),
        )

    def test_proper_encoding(self) -> None:
        """
        YAML encoding test.

        Given:
            - A dict with a list of strings with non-ascii characters
        Do:
            - Render the dict to YAML
        Expect:
            - The YAML string to be the same as the original YAML string.
            - The YAML string to be encoded in utf-8 and
              contain the non-ascii characters.

        """
        _yaml_repr = "countries:\n- United Kingdom\n- France\n- España"
        obj = {"countries": ["United Kingdom", "France", "España"]}
        renderer = YAMLRenderer()
        content = renderer.render(obj, "application/yaml")
        self.assertEqual(content.strip(), _yaml_repr.encode("utf-8"))
