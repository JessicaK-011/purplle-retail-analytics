# Assumptions

## Dataset Assumptions

* The provided CCTV clips are representative samples of store activity.
* The provided sales CSV is considered accurate transaction data.
* The provided store layout reflects the actual store structure.

---

## Video Analytics Assumptions

* YOLOv8 detections are used as a proxy for visitor presence.
* Frame sampling is sufficient for occupancy estimation.
* Person count approximates footfall activity.
* Staff and visitors are not explicitly separated.
* Cross-camera re-identification is outside the scope of this implementation.

---

## Zone Analytics Assumptions

Based on the provided store layout, the following operational zones are assumed:

* Entrance Area
* Nail Unit
* Makeup Section
* Skincare Section
* Billing Counter

Zone-level analytics are inferred using camera coverage.

---

## Retail Analytics Assumptions

* Sales data represents completed transactions.
* Revenue calculations are based on total_amount.
* Salesperson performance is measured using attributed revenue.

---

## System Assumptions

* APIs are consumed internally by retail operations teams.
* Batch processing is acceptable for challenge-scale workloads.
* SQLite storage is sufficient for provided data volumes.

---

## Future Scope

* Visitor tracking across cameras
* Real-time processing
* Queue analytics
* Dwell time estimation
* Shelf engagement analytics
* Store layout optimization recommendations
