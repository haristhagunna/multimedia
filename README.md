# Multimedia and Application (BCA429CO): study site

Notes, class slides and practice questions, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Preview on your computer

```bash
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. The page reloads when you save a file.

## Publish on GitHub Pages

1. Create a GitHub repository and push this folder to its `main` branch.
2. In the repository, open **Settings → Pages** and set the source to the **`gh-pages` branch** (it appears after the first workflow run).
3. The workflow in `.github/workflows/deploy.yml` rebuilds and publishes the site on every push to `main`.
4. Optional: uncomment `site_url` and `repo_url` in `mkdocs.yml` and put in your GitHub username.

## Folder layout

```
docs/
  index.md, syllabus.md, course-map.md
  unit-NN/            notes, practice and slides page for each unit
  decks/unit-NN.html  the reveal.js slide decks (open on their own or inside the slides page)
  stylesheets/extra.css
mkdocs.yml            site settings and the sidebar menu
```

To add a page, create the `.md` file in the unit folder and add it under that unit in the `nav:` section of `mkdocs.yml`.

## Copyright

(c) 2026 Er. Harish Thagunna. All rights reserved. See LICENSE.

## Rebuilding the class slides

The decks in `docs/decks/` are generated from the topic notes and `tools/visuals.py`:

    python tools/build_decks.py        # all units
    python tools/build_decks.py 5 6    # selected units

Needs `markdown`, `pymdown-extensions`, `beautifulsoup4`, `matplotlib`, `numpy` and the Mermaid CLI (`mmdc`).
