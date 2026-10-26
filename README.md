# Reevo Import Prep

Upload a HubSpot export of contacts and accounts and get back a file in Reevo's multi-object import format, plus a list of rows the customer needs to fix.

Built by Laksha Adalkha for the Reevo Product Operations case study (Prompt 2). Not an official Reevo product.

## How it works

- Columns are matched by header name, so column order and extra columns don't matter.
- Output uses the 11 import headers from the case study template, with the helper rows removed.
- Rows missing a required field (first name, last name, email or phone, company name, company domain) or repeating an earlier email are held back and listed for the customer.
- Files are read in the browser and never uploaded anywhere.

## Editing

Change `src/index.template.html`, then run `python3 build.py`. It writes `docs/index.html` (served by GitHub Pages) and `index.html` (the Claude artifact version).
