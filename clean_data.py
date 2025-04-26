import pandas as pd
import isodate
from datetime import datetime

def clean_data(df):
    # Convert to numeric
    for col in ['views', 'likes', 'comments']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    # Parse ISO 8601 durations to minutes
    df['duration_minutes'] = df['duration'].apply(
        lambda x: isodate.parse_duration(x).total_seconds() / 60 if pd.notnull(x) else None
    )

    # Convert published_at to datetime
    df['published_at'] = pd.to_datetime(df['published_at'], errors='coerce')

    # Extract year and month
    df['year'] = df['published_at'].dt.year
    df['month'] = df['published_at'].dt.month_name()

    # Drop ISO duration column
    df.drop(columns=['duration'], inplace=True)

    return df

if __name__ == "__main__":
    # Load raw CSV
    df = pd.read_csv("youtube_channel_data.csv")

    # Clean it
    df = clean_data(df)

    df = df[df['year'].between(2000, 2030)]  # Filter valid years
    df = df.dropna(subset=['title', 'views'])  # Drop rows with missing titles/views
    df = df.drop_duplicates(subset=['video_id']) # Drop duplicate video IDs

    # Save cleaned data
    df.to_csv("youtube_cleaned_data_0.csv", index=False)
    print("Cleaned data saved to 'youtube_channel_cleaned_data_0.csv'")
