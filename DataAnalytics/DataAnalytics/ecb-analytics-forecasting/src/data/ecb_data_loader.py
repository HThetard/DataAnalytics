import pandas as pd


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        import pandas as pd
        self.data = pd.read_csv(self.file_path)
        return self.data

    def preprocess_data(self):
        if self.data is not None:
            # Example preprocessing steps
            self.data.dropna(inplace=True)
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            self.data.set_index('Date', inplace=True)
            return self.data
        else:
            raise ValueError("Data not loaded. Please load data first.")