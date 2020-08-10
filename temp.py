import pandas as pd
import os


def read_from_desktop(path: str) -> pd.DataFrame:
    file_type = path.split('.')[-1]

    if file_type == 'xlsx':
        return pd.read_excel(path)
    elif file_type == 'csv':
        return pd.read_csv(path)


def upload_to_drive() -> None:
    # https://www.lieben.nu/liebensraum/2019/04/uploading-a-file-to-onedrive-for-business-with-python/
    pass


def main(path: str) -> None:
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        df = read_from_desktop(file_path)

        # delete from disk
        os.remove(file_path)

        # delete from memory
        df = None


if __name__ == '__main__':
    path: str = 'C:/Users/Mike/Downloads/downloads/'
    main(path)

    print('complete')
