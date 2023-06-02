# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.0.1]

### Fixed

- All DRF fields.

### Removed

- `.flake8` file
- `requirements` file

## [3.0.0] - 2023-06-02

### Added

- Test / Support for `Python>=3.8`
- Test / Support for `Django>=3.2`
- Test / Support for `DRF>=3.2`
- Support for `DRF==3.14`
- Test coverage.
- Integration with `mkdocs-material` with `mike` support for versioned docs.
- Typing annotations.
- Added string styles.
- Added representers for UUID, Time, TimeDelta, ErrorDetail and SafeString.

### Changed

- Replace `setuptools` with `poetry`.
- Replace `isort` and `flake8` by ruff.

### Removed

- Support for `Python<3.8`
- Support for `Django<3.2`
- Support for `DRF==3.14`

## [2.0.0] - 2020-04-27

### Changed

- Update test/support matrix: `Python 3.5+`, `Django 2.2+`, `DRF 3.11+`.

### Removed

- Support for Python 2.


[unreleased]: https://github.com/Qu4tro/django-rest-framework-yaml/compare/3.0.0...HEAD
[3.0.0]: https://github.com/Qu4tro/django-rest-framework-yaml/releases/tag/3.0.0
[2.0.0]: https://github.com/jpadilla/django-rest-framework-yaml/releases/tag/2.0.0

