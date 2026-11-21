# Design Notes

## Data flow
Static path definitions (source, transit hub, destination, latency values) are mapped to coordinates. The renderer builds a Folium map, adds polylines and animated path overlays, attaches markers with distance/latency popups, and saves an HTML artifact.

## Metric interpretation
Latency values are example segment values; the script displays their sum. Geodesic distance is computed between source and destination coordinates and is not a route distance.

## Future improvements
- Define a validated schema for paths and points.
- Remove duplicate/overlapping sample paths or clearly label intentional comparisons.
- Support CSV/JSON input and optional live measurement integrations.
- Add tests for distance and latency aggregation.
- Add data freshness and source metadata for measured values.
