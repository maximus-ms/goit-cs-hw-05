from pathlib import Path
from faker import Faker
from random import randint, choice

fake = Faker()

extensions = [
    ".txt",
    ".csv",
    ".py",
    ".xlsx",
    ".docx",
    ".zip",
    ".rar",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".mp3",
    ".wav",
    ".mp4",
    ".avi",
    ".exe",
    ".pdf",
]


def create_fake_file(path):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "wb") as file:
        file.truncate(randint(100, 10000))


def generate_fake_files(
    path, ext_list=extensions, depth=3, files_per_folder=10
):
    for _ in range(depth):
        folders = [fake.word() for _ in range(randint(1, 5))]
        for folder in folders:
            folder_path = Path(path, folder)
            for _ in range(randint(files_per_folder // 2, files_per_folder)):
                create_fake_file(
                    Path(folder_path, fake.word() + choice(ext_list))
                )
            generate_fake_files(
                folder_path,
                ext_list=ext_list,
                depth=randint(0, depth - 1),
                files_per_folder=randint(
                    files_per_folder // 2, files_per_folder
                ),
            )


if __name__ == "__main__":
    generate_fake_files(
        "./fake_folder", depth=3, files_per_folder=randint(10, 20)
    )
