# Django SirTrevor Field

**Not ready for production!** Library in planning stage. No promises.

A django field based on ITV's [Sir Trevor JS][sirtrevor] rich content editor.

## Contribution
### Testing

We use [`tox`][tox] to run the tests, and [TravisCI][travis] for continuous
integration. To run the tests locally, install `tox`:

    pip install tox

and then run:

    make test

### Style guide

The test suite includes `flake8` and `isort`. This is an attempt to make it
easier to follow the opinionated code style preferences of this project.


[sirtrevor]: https://madebymany.github.io/sir-trevor-js/
[tox]: https://pypi.python.org/pypi/tox
[travis]: https://travis-ci.org/
