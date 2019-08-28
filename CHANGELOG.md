# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0.2] 2019-08-28
### Added
- Add full build tests to travis

### Fixed
- Fix parsing version in setup.py
- Fix version constraint regex in setup.py

## [0.3.0.1] 2019-08-28
### Fixed
- Fix parsing requirements.txt during deployment

## [0.3.0] 2019-08-28
### Added
- Add a changelog to track project changes
- Separate conversation storage with `Conversation` objects
- Allow errors to propagate as custom exceptions
- Wrap replies in a `Response` object for ease of use
- Allow the API url to be configured as a class parameter

### Fixed
- Allow non-strict JSON parsing of responses

### Removed
- Removed Python 3.4 support

## [0.2.3.6] 2017-06-18
Undocumented changes

[Unreleased]: https://github.com/snoonetIRC/cleverwrap.py/compare/v0.3.0.2..HEAD
[0.3.0.2]: https://github.com/snoonetIRC/cleverwrap.py/compare/v0.3.0.1..v0.3.0.2
[0.3.0.1]: https://github.com/snoonetIRC/cleverwrap.py/compare/v0.3.0..v0.3.0.1
[0.3.0]: https://github.com/snoonetIRC/cleverwrap.py/compare/v0.2.3.6..v0.3.0
[0.2.3.6]: https://github.com/snoonetIRC/cleverwrap.py/releases/tag/v0.2.3.6
