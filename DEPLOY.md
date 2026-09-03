# Deploy — add only

Nothing in this file deletes a page, hop, Stripe link, Finder, or Worker.

## Domain is not a backend

A domain is a name. DNS points that name at a host.

| Host | What it is | You already have |
| --- | --- | --- |
| Vercel | Front (HTML) + optional serverless `/api` | `hour-one-dual-audit` project |
| Cloudflare Worker | Edge backend + can serve `public/` | `sovereign-helix-production` |
| Stripe | Money backend | $70 / $80 / $250 links |
| Supabase | Auth/DB if you need accounts later | parked |
| Python CLI on iPhone (a-Shell / Pyto) | Talks *to* Vercel/Cloudflare. Not the public site. | your workflow |

Static pages (`index.html`, `/hop-a`, `/archive`) do **not** need a backend. Checkout does not live on Vercel — it lives on Stripe / Digistore.

`thesovereignhelix.com` should stay on Cloudflare when the checklist is done. Do not move the Worker domain onto this Vercel project.

## How Vercel deploys *this* desk

1. Repo: `CashflowNchill510/hour-one-dual-audit`
2. Project: `prj_N3sNtbfGfOQH7jenetMWecue5f45` (ignore `finder-pulse`)
3. Link GitHub app with write access → every push to `main` publishes.
4. `vercel.json` keeps `cleanUrls` so `/archive` maps to `archive.html`.
5. Optional Python: files under `api/` become `https://YOUR-ALIAS/api/name`.

Until Git is linked, push still saves GitHub; the public alias stays stale.

## How Python talks to Vercel (CLI, not a second app)

On Mac/Linux or a machine with Node:

```bash
npm i -g vercel
vercel login
vercel link --yes --project hour-one-dual-audit --scope foreverfoward510-4414s-projects
vercel --prod
```

On iPhone (a-Shell / Pyto) you usually cannot run `vercel` cleanly. Use Python only to:

- write/edit HTML
- `git push` to `main` (then Vercel builds, once linked)
- call your own `/api/health` after it is live

Example check after deploy:

```python
import urllib.request
print(urllib.request.urlopen("https://hour-one-dual-audit-foreverfoward510-4414s-projects.vercel.app/api/health").read())
```

Do not use Python to mint another project.

## How the AI uses this

Grok / your agents:

- **Add** HTML or `api/*.py` in this repo
- **Push** `main`
- Never delete Finder, hops, Stripe buttons, WORKFLOW, or Worker files
- High-ticket still needs `CONFIRM LICENSE`

Quetzalcoatl / Lattice stay on Cloudflare Workers. This Vercel project is the public desk + hops + archive.

## Attach a custom domain later (optional)

Vercel → Project → Settings → Domains → add host → put the DNS records at the registrar.

That is still not a backend. It is a name on the same files.
