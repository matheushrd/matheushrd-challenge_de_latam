import os
import io
import json
import pandas as pd
import pandasql as psql
import zipfile
import regex
from collections import Counter
from typing import List, Tuple
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account

class DataAnalyzer:
    """A class for analyzing data from a file downloaded from Google Drive and performing various analyses."""

    def __init__(self):
        """
        Initializes the DataAnalyzer with the necessary credentials, file ID, and filename.
        Downloads the file from Google Drive, converts it to a parquet format, and loads it into a DataFrame.
        
        Parameters:
        - creds_path: Path to the JSON file containing Google service account credentials.
        - file_id: ID of the file to be downloaded from Google Drive.
        - filename: Name to be used for the downloaded and processed files.
        """
        self.creds_path = os.getenv('CREDS_PATH')
        self.file_id = os.getenv('FILE_ID')
        self.filename = os.getenv('FILENAME')
        self.df = None
        self.load_credentials()
        self.download_file()
        self.convert_to_parquet()
        self.load_dataframe()

    def load_credentials(self):
        """Loads the service account credentials from the specified JSON file."""
        with open(self.creds_path, 'r') as file:
            self.credz = json.load(file)

    def download_file(self):
        """Downloads the file from Google Drive using the service account credentials."""
        if os.path.exists(f'{self.filename}.zip'):
            print(f"The file {self.filename}.zip already exists.")
        else:
            credentials = service_account.Credentials.from_service_account_info(self.credz)
            drive_service = build('drive', 'v3', credentials=credentials)

            request = drive_service.files().get_media(fileId=self.file_id)
            fh = io.FileIO(f'{self.filename}.zip', 'wb')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                _, done = downloader.next_chunk()

    def convert_to_parquet(self):
        """
        Converts the downloaded ZIP file into a parquet file.
        Assumes there is only one file within the ZIP archive.
        """
        with zipfile.ZipFile(f'{self.filename}.zip', 'r') as z:
            file_in_zip = z.namelist()[0]
            with z.open(file_in_zip) as f:
                df = pd.read_json(f, lines=True)
        df.to_parquet(f'{self.filename}.parquet')

    def load_dataframe(self):
        """Loads the parquet file into a pandas DataFrame."""
        self.df = pd.read_parquet(f'{self.filename}.parquet')

    def q1(self) -> List[Tuple[str, str]]:
        """
        Performs a SQL query to find the top 10 dates with the most posts and the user who posted the most on each of those dates.

        Returns:
        A list of tuples, each containing a date and the username of the top poster for that date.
        """
        df_selected = self.df.copy()
        df_selected['date'] = pd.to_datetime(df_selected['date']).dt.date
        df_selected['username'] = df_selected['user'].apply(lambda x: x.get('username', 'unknown') if isinstance(x, dict) else 'unknown')
        columns = ["date", "username"]
        df_selected = df_selected[columns]
        query = """
        SELECT date, username, COUNT(*) as post_count
        FROM df_selected
        GROUP BY date, username
        ORDER BY date DESC, post_count DESC
        LIMIT 10
        """
        result = psql.sqldf(query)
        return [(row.date, row.username) for row in result.itertuples(index=False)]


    @staticmethod
    def count_emojis(text: str) -> List[str]:
        """
        Finds all emojis in a given text.

        Parameters:
        - text: The text to search for emojis.

        Returns:
        A list of found emojis.
        """
        emoji_pattern = regex.compile("["
            "\U0001F1E0-\U0001F1FF"  # Flags
            "\U0001F300-\U0001F5FF"  # Symbols & Pictograms
            "\U0001F600-\U0001F64F"  # Emoticons
            "\U0001F680-\U0001F6FF"  # Transport & Maps
            "\U0001F700-\U0001F77F"  # Alchemical Symbols
            "\U0001F780-\U0001F7FF"  # Geometric Shapes
            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictograms
            "\U0001FA00-\U0001FA6F"  # Chess Symbols
            "\U0001FA70-\U0001FAFF"  # Extended-A Symbols and Pictograms
            "\U00002702-\U000027B0"  # Dingbats
            "\U000024C2-\U0001F251"  # Enclosed Characters
            "]+", flags=regex.UNICODE)
        return emoji_pattern.findall(text)

    def q2(self) -> List[Tuple[str, int]]:
        """
        Finds the top 10 most used emojis in the 'content' column of the DataFrame.

        Returns:
        A list of tuples, each containing an emoji and its count.
        """
        emoji_list = [emoji for text in self.df['content'].dropna() for emoji in self.count_emojis(text)]
        return Counter(emoji_list).most_common(10)

    def q3(self) -> List[Tuple[str, int]]:
        """
        Finds the top 10 most mentioned users in the 'content' column of the DataFrame.

        Returns:
        A list of tuples, each containing a username mention and its count.
        """
        user_mention_regexp = regex.compile(r'@(\w+)', regex.UNICODE)
        mentions_counter = Counter([mention for text in self.df['content'].dropna() for mention in user_mention_regexp.findall(text)])
        return mentions_counter.most_common(10)
