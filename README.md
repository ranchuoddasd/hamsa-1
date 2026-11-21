# Network Latency Visualizer

An interactive geographic visualization experiment for illustrating network paths, transit hubs, endpoints and latency annotations on a map.

**Status:** Prototype using synthetic coordinates and static latency values. It does not measure real network performance or collect live telemetry.

## Capabilities

- Display source, transit-hub and destination markers.
- Render multiple illustrative multi-hop paths.
- Animate path overlays with Folium's AntPath plugin.
- Annotate sample end-to-end latency values.
- Calculate approximate route distance across each displayed hop.
- Export the visualization as a standalone HTML file.

## Technology

- Python 3
- Folium
- Geopy

## Repository structure

```text
.
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── docs/
    ├── architecture.md
    └── prototype-notes.md
```

## Run locally

Use Python 3.10 or later:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# macOS / Linux:
source .venv/bin/activate

python -m pip install -r requirements.txt
python main.py
```

The script generates `latency_path_map.html` in the current directory. Open that file in a browser. The map uses online tile resources, so an internet connection may be needed to display the map background.

## Data model

The example topology is defined in `main.py`:

- `SOURCES`: synthetic source coordinates.
- `HUBS`: synthetic transit-hub coordinates.
- `DESTINATIONS`: synthetic destination coordinates.
- `PATHS`: route definitions, display colors and per-hop sample latency values.

Route distance is calculated by summing the geodesic distance of each displayed hop. Latency values remain illustrative inputs and are not inferred from geographic distance.

## Limitations

- Coordinates and latency values are static examples.
- The project is not traceroute, ping, path discovery or network telemetry.
- Geographic distance is not a substitute for actual routed path length.
- Multiple scenarios may intentionally share the same geographic path while displaying different illustrative latency values.
- No data ingestion API, persistence, authentication or automated test suite is included.

## Security and data handling

Use synthetic or anonymized locations and topology in public examples. Do not commit customer circuits, private network paths, internal hostnames, IP address allocations, credentials or confidential operational details.

## Roadmap

1. Add validated JSON/CSV input for topology and measurements.
2. Separate topology, measurement data and map rendering.
3. Add timestamps, measurement source and confidence metadata.
4. Distinguish measured latency from manually supplied estimates.
5. Add tests for route validation and hop-distance calculations.
6. Add optional live measurement adapters with explicit authorization.

## License

No license is currently provided. Until a license is added, reuse and redistribution are not granted by default.
