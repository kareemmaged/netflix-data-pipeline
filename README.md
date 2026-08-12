# Secure E-Commerce & Netflix ETL Pipelines

[![Python](https://shields.io)](https://python.org)
[![Pandas](https://shields.io)](https://pydata.org)
[![License](https://shields.io)](LICENSE)

A robust Data Engineering project containing modular, enterprise-ready **ETL (Extract, Transform, Load)** pipelines built with Python and Pandas. This repository showcases automated data ingestion, cleaning strategies for missing values, advanced feature engineering, and a strict asset validation layer to prevent data corruption.

---

## 🛠️ Tech Stack & Skills
* **Languages & Core:** Python (Type Hinting, Object Handling)
* **Data Manipulation:** Pandas, NumPy
* **Methodologies:** Data Quality Gates, Exception Handling, Defensive Programming
* **Domain Strengths:** Secure Pipeline Design, Data Profiling, Access Security Control

---

## 📂 Project Architecture
```text
ecommerce-data-pipeline/
│
├── data/
│   ├── raw/
│   │   └── netflix_titles.csv      # Raw unstructured media catalog
│   │
│   └── processed/
│       └── netflix_clean.csv       # Production-ready catalog dataset
│
├── src/
│   └── netflix_pipeline.py         # Netflix Media ETL Engine
│
├── .gitignore                      # Prevents tracking large datasets
└── README.md                       # Documentation
```

---

## 🚀 The Data Pipelines

### 1. E-Commerce Financial Pipeline (`pipeline.py`)
Processes over **540,000+ rows** of transaction logs, resolving special encoding issues (`windows-1252`) caused by international currency symbols (£, €).
* **Extraction:** Ingests raw sales streams safely across varying character encodings.
* **Transformation:** Filters cancelations/returns (negative quantities) and zero-price adjustments. Drops null records without descriptions. Automatically engineer `Revenue` ($Qty \times UnitPrice$) alongside time-series date columns (`Year`, `Month`, `Date`).
* **Quality Gate (Validation):** Employs strict assertions ensuring no critical transactional entries are missing or structurally corrupted before pipeline execution ends.

### 2. Netflix Catalog Metadata Pipeline (`netflix_pipeline.py`)
Processes unstructured media listings, focusing heavily on strategic imputation to preserve data density.
* **Extraction:** Ingests media catalogs in standard UTF-8.
* **Transformation:** Fills sparse, high-volume string columns (`director`, `cast`, `country`) with `"Unknown"` placeholders to retain overall content metrics. Drops row listings with missing timeline data (`date_added`, `rating`, `duration`). Extracts normalized temporal dimensions.
* **Quality Gate (Validation):** Implements a global data-integrity matrix verification (`df.isna().sum().sum() == 0`), crashing execution instantly if any illegal null spaces seep past the transformations.

---

## 💻 How to Get Started

### 1. Clone the repository
```bash
git clone https://github.com
cd ecommerce-data-pipeline
```

### 2. Set up your local workspace
```bash
# Install the necessary analysis tools
pip install pandas
```

### 3. Run the engines
```bash
# Run the E-Commerce pipeline
python src/pipeline.py

# Run the Netflix pipeline
python src/netflix_pipeline.py
```

---

## 🛡️ Secure Engineering & Core Philosophy
As a Data Engineer with a strong foundation in **Frontend Architecture** and experience as a **Junior Penetration Tester**, I approach infrastructure build-outs with a security-first mindset:
* **Defensive Pipeline Design:** Incorporating programmatic assertions ensures pipelines crash gracefully on corrupted datasets rather than leaking dirty records down into operational databases.
* **Data Leak Mitigation:** Ensuring large data payloads are explicitly excluded via `.gitignore` configurations, ensuring zero regulatory or proprietary breaches occur during Git version control syncing.
* **Readable Architecture:** Utilizing my background in modular UI design, I prioritize formatting clean, human-readable scripts that promote rapid team onboarding and easy debugging.

---

