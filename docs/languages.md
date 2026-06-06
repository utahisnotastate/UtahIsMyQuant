# Documentation languages

Each language lives on **its own pages**. Pick one tree and stay in it — no mixed-language clutter on a single screen.

| Language | Hub (start here) |
|----------|------------------|
| **English** (default) | [README.md](README.md) |
| **Русский** | [i18n/ru/README.md](i18n/ru/README.md) |
| **Eesti** | [i18n/et/README.md](i18n/et/README.md) |
| **Suomi** | [i18n/fi/README.md](i18n/fi/README.md) |
| **日本語** | [i18n/ja/README.md](i18n/ja/README.md) |

## Full translation per locale

Each locale under `docs/i18n/<locale>/` mirrors the English `docs/` tree:

- Hub, quickstart, paying Utah, glossary, audience guides
- API reference, technical architecture, Omni, Utahrbitrage, prediction markets
- Golden Master guides (01–04)
- Guides, migration playbooks, tutorials (01–10), code recipes
- Project overview (translated from root README)

**Code blocks, shell commands, and Python identifiers stay in English** in every locale.

## LaTeX preprint

The academic preprint remains a single shared source file:

[papers/utahrbitrage-theorem.tex](papers/utahrbitrage-theorem.tex)

Each locale has a short note at `i18n/<locale>/papers/README.md`.

## Contributing translations

See [CONTRIBUTING.md](../CONTRIBUTING.md). Edit files under `docs/i18n/<locale>/` only — never embed multiple languages on one page.
