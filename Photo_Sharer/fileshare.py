class FileSharer:
    def __init__(self, filepath, api_Key="AViVpq7suSQWWEdrl6hf9z"):
        self.filepath = filepath
        self.api_Key = api_Key

    def share(self):
        #client = Client(self.api_Key)
        #new_fileLink = client.upload(filepath = self.filepath)
        return self.filepath