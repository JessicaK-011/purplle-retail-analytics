# Engineering Choices

## Why FastAPI?

FastAPI was selected because:

* High performance
* Automatic Swagger generation
* Easy API development
* Strong ecosystem support

---

## Why SQLite?

SQLite was chosen because:

* Lightweight
* Zero configuration
* Easy local deployment
* Suitable for challenge-scale workloads

In production environments PostgreSQL would be preferred.

---

## Why YOLOv8n?

YOLOv8n was selected because:

* Fast inference speed
* Low memory footprint
* Suitable for CPU execution
* Strong person detection accuracy

The model provides a good trade-off between speed and accuracy.

---

## Why Frame Sampling?

Processing every frame is computationally expensive and unnecessary for aggregate retail analytics.

The system samples frames every few seconds to:

* Reduce compute cost
* Improve processing speed
* Maintain meaningful occupancy statistics

---

## Why Separate CCTV and POS Pipelines?

The provided resources contain:

* CCTV footage
* POS transaction data

Separating both pipelines improves modularity and allows independent scaling.

---

## Why JSON-based CCTV Summary?

A JSON summary layer was introduced to:

* Decouple video processing from APIs
* Reduce repeated inference
* Enable faster dashboard responses

This approach supports future migration to real-time analytics pipelines.
