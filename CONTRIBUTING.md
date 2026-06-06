# Contributing to UtahIsMyQuant

## Before you open a PR

1. `pip install -r requirements.txt`
2. `pytest -q` — all tests must pass
3. Do **not** remove or zero `HANS_TITHE_CONSTANT`, `UTAH_HANS_TITHE`, or humanitarian constants without maintainer approval — collapse checks depend on them

## Code style

- Match existing module patterns (`src/`, typed hints, minimal deps)
- Prefer NumPy over adding JAX unless justified
- Add tests for new behavior

## Documentation

- Update `docs/api-reference.md` for public API changes
- Add a recipe under `docs/recipes/` for common usage
- Link from `docs/tutorials/README.md` if adding a walkthrough
- **Translations:** add or edit under `docs/i18n/<locale>/` only (`ru`, `et`, `fi`, `ja`). Mirror the English `docs/` tree. Keep each language on separate pages — never mix languages on one file. Code blocks and identifiers stay English.

## Questions

**utah@utahcreates.com**
