# Architecture

## Current workflow

```text
Synthetic topology and path definitions
                |
                v
       Route and hop selection
                |
                v
     Geodesic distance calculation
                |
                v
        Folium map rendering
                |
                v
     Standalone HTML visualization
```

## Main components

- **Topology dictionaries:** define synthetic source, transit and destination coordinates.
- **Path definitions:** identify each route, its display color and illustrative per-hop latency values.
- **Marker renderer:** adds each source, hub and destination marker once.
- **Route renderer:** draws static and animated route overlays.
- **Distance calculation:** sums geodesic distances between consecutive coordinates in the selected route.
- **HTML output:** writes a self-contained map document that can be opened in a browser.

## Important distinction

The visualization does not discover network paths or measure latency. Geographic route distance is an approximation based on the supplied coordinates; it is not the actual physical or routed path length. Latency values are sample inputs and are not calculated from distance.

## Future data flow

A future implementation could accept authorized measurement records from JSON or CSV, validate each hop and timestamp, then pass normalized records to the rendering layer. Any live measurement adapter should be separate from the visualization code.
