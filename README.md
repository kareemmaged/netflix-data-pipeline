# Netflix Data Pipeline 🎬

A simple ETL (Extract, Transform, Load) pipeline that cleans and validates the Netflix titles dataset, turning a raw, messy catalog into a production-ready CSV.

## 📁 Project Structure
---
```text
netflix-data-pipeline/
│
├── data/
│ ├── raw/
│ │ └── netflix_titles.csv # Raw unstructured media catalog
│ │
│ └── processed/
│ └── netflix_clean.csv # Production-ready catalog dataset
│
├── src/
│ └── netflix_pipeline.py # Netflix Media ETL Engine
│
├── .gitignore
└── README.md
```

---

## ⚙️ What It Does

The pipeline runs in four stages:

1. **Extract** — Reads the raw CSV file (`netflix_titles.csv`) into a pandas DataFrame.
2. **Transform**
   - Strips whitespace from `title`, `type`, and `country`.
   - Fills missing `director`, `cast`, and `country` values with placeholders.
   - Drops rows missing critical metadata (`date_added`, `rating`, `duration`).
   - Parses and standardizes `date_added` into a proper datetime format.
   - Extracts `year_added` and `month_added` as new columns.
3. **Validate** — Runs sanity checks to catch bad data before it ships:
   - No missing `show_id` or `title` values.
   - `type` is restricted to `Movie` or `TV Show`.
   - `release_year` falls within a realistic range (1900–2027).
4. **Load** — Saves the cleaned dataset to `data/processed/`.

## 🚀 Usage

```bash
python src/netflix_pipeline.py
```

## 📦 Requirements

- Python 3.x
- pandas

Install dependencies:

```bash
pip install pandas
```

## 📝 Notes

- The raw dataset (`netflix_titles.csv`) is expected in Kaggle's [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) format.
- File paths are currently hardcoded for a local Windows environment — update the `file_path` in `extract()` and the output path in `load()` before running elsewhere.
- The `data/` folder is excluded from version control via `.gitignore` to avoid tracking large datasets.

## 📄 License

This project is for educational/portfolio purposes.
