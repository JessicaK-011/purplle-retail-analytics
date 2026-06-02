# System Design

## Architecture Overview

The solution consists of two independent analytics pipelines:

1. CCTV Analytics Pipeline
2. Sales Analytics Pipeline

Both pipelines expose insights through a unified FastAPI layer.

---

## CCTV Analytics Pipeline

```text
CCTV Videos
      ↓
YOLOv8 Person Detection
      ↓
Frame Sampling
      ↓
People Counting
      ↓
JSON Summary
      ↓
FastAPI Endpoints
```

### Processing Strategy

* Videos are processed offline.
* Frames are sampled every 5 seconds.
* YOLOv8 detects people in sampled frames.
* Occupancy statistics are generated per camera.

---

## Sales Analytics Pipeline

```text
Sales CSV
      ↓
CSV Ingestion
      ↓
SQLite Database
      ↓
Analytics Services
      ↓
FastAPI Endpoints
```

The sales dataset is imported into SQLite and used for business analytics.

---

## Database Layer

SQLite is used as the primary datastore.

Tables:

### events

Stores operational events.

### sales

Stores transaction data imported from the provided CSV.

---

## API Layer

FastAPI provides:

* Event ingestion
* Metrics retrieval
* Sales analytics
* CCTV analytics

Swagger documentation is automatically generated.

---

## Scalability Considerations

For production deployment:

* SQLite can be replaced by PostgreSQL.
* YOLO inference can run on GPU workers.
* Event ingestion can be moved to Kafka streams.
* Multi-camera tracking can be added.

---

## Limitations
## Data Availability Notes

The challenge resources included:

* Store layout plans
* CCTV footage samples from five cameras
* Transaction-level sales data

However, a complete operational event stream (visitor journeys, zone transitions, dwell-time events, queue events, etc.) was not provided.

Therefore:

* Sales analytics endpoints operate on real transaction data imported from the provided sales CSV.
* CCTV analytics operate on real YOLOv8-based person detections extracted from the provided CCTV footage.
* Operational analytics modules (funnel, heatmap, anomaly detection, and store metrics) are implemented as reusable analytics services and API endpoints designed to consume event-level retail telemetry when available.

The architecture, database schema, API contracts, and service layer support ingestion of real operational events without requiring structural changes.

