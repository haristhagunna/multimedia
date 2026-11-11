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

## Custom domain (optional)

1. Buy a domain (for example `multimedia.example.com`) and add a `CNAME` DNS record pointing to `thagunnaharish1-netizen.github.io`.
2. In the GitHub repository open **Settings → Pages → Custom domain**, enter the domain and tick **Enforce HTTPS**.
3. Put the same domain in `site_url` in `mkdocs.yml` (the share image and canonical links use it) and push.

## Regenerating generated content

```bash
python3 tools/build_cheatsheets.py   # revision/cheat-sheets.md
python3 tools/build_instructor.py    # instructor pages and question-bank.csv
python3 tools/build_labs.py          # lab pages (embeds tested code)
python3 tools/build_assets.py        # share image and favicon
python3 tools/build_decks.py         # class decks
```
