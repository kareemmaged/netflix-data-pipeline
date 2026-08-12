import pandas as pd

file_path = r"D:\Data Engineering\projects\netflix-data-pipeline\data\raw\netflix_titles.csv"

def extract():
    df = pd.read_csv(file_path, encoding='latin-1')
    return df

def transform(df):
    # Text clean up
    df['title'] = df['title'].str.strip()
    df['type'] = df['type'].str.strip()
    df['country'] = df['country'].str.strip()

    # Handling missing values
    df['director'] = df["director"].fillna('Unknown Director')
    df["cast"] = df["cast"].fillna('Unknown Cast')
    df["country"] = df["country"].fillna('Unknown Country')

    # Dropping rows only if they completely lack essential metadata
    df = df.dropna(subset=["date_added", "rating", "duration"])

    # 4. Standardize Date Formats
    df["date_added"] = df["date_added"].str.strip()
    df["date_added"] = pd.to_datetime(df["date_added"], format="%B %d, %Y", errors='coerce')

    # In case any dates fail parsing, drop those rows too
    df = df.dropna(subset=["date_added"])
    
    # 5. Extracting temporal features for data analysts
    df["year_added"] = df["date_added"].dt.year
    df["month_added"] = df["date_added"].dt.month

    return df

def validate(df):
    
    assert df["show_id"].notna().all(), "Error: Found rows with missing show IDs!"
    assert df["title"].notna().all(), "Error: Found rows with missing titles!"
    assert df["type"].isin(["Movie", "TV Show"]).all(), "Error: Invalid content type detected!"
    
    # Check that numeric release years look realistic
    assert df["release_year"].between(1900, 2027).all(), "Error: Unrealistic release year detected!"
    
    print("✅ Validation passed! The data is clean.")

def load(df):
    
    df.to_csv(r"D:\Data Engineering\projects\netflix-data-pipeline\data\processed\netflix_titles_cleaned.csv", index=False)

def main():
    df = extract()
    print(f"📥 Extracted {len(df)} entries from the Netflix catalog.")

    df = transform(df)
    print(f"🛠️ Transformed dataset down to {len(df)} finalized records.")

    validate(df)
    load(df)
    print("🚀 Pipeline completed successfully!")

if __name__ == "__main__":
    main()