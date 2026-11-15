# agency-poem-01 — The Handoff

One short poem about agency: the doing can be given away, the
choosing cannot. An AI agent does not sleep or doubt or ask what
matters — it only asks what next. The one thing it cannot do is ask.

## Entry

- `main.py` — writes the poem to `/output/entry.txt` (standard
  library only, deterministic, no network). The poem is 461
  characters, inside the gate's 1–1000, and the program refuses
  to write a poem that breaks the gate.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
