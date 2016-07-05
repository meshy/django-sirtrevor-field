# Django SirTrevor Field

[![Build Status][travis-status-img]][travis-build]

**Not ready for production!** Library in planning stage. No promises.

A django field based on ITV's [Sir Trevor JS][sirtrevor] rich content editor.

## TODO

- [x] Based on `django.contrib.postgres.postgres`'s `JSONField`.
- [x] 100% test coverage enforced by CI.
- [ ] `SirTrevorWidget`.
- [ ] Works with `django.forms.Form`.
- [ ] Works with `django.forms.ModelForm`.
- [ ] Works with django admin.
- [ ] On PyPI.
- [ ] Quickstart docs.
- [ ] API docs.
- [ ] CONTRIBUTING.md.

## Contribution
### Testing

We use [`tox`][tox] to run the tests, and [TravisCI][travis] for continuous
integration. To run the tests locally, install `tox`:

    pip install tox

... install phantomjs:

    # OS X
    brew install phantomjs

and then run:

    make test

### Style guide

The test suite includes `flake8` and `isort`. This is an attempt to make it
easier to follow the opinionated code style preferences of this project.


[sirtrevor]: https://madebymany.github.io/sir-trevor-js/
[tox]: https://pypi.python.org/pypi/tox
[travis-build]: https://travis-ci.org/meshy/django-sirtrevor-field
[travis-status-img]: https://travis-ci.org/meshy/django-sirtrevor-field.svg?branch=master
[travis]: https://travis-ci.org/
