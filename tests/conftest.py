"""
Pytest configuration file.

This file is automatically loaded by pytest when running tests.
See https://docs.pytest.org/en/latest/reference.html#configuration-options
for more information.
"""


def pytest_configure() -> None:
    """Configure Django settings before tests run."""
    from django.conf import settings

    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            },
        },
    )

    try:
        import django

        django.setup()
    except AttributeError:
        pass
