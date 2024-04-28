import argparse
import asyncio
from aiopath import AsyncPath
from pathlib import Path
from aioshutil import copyfile


def get_args():
    parser = argparse.ArgumentParser(description="Sort files by extension")
    parser.add_argument(
        "-s", "--source", default="fake_folder", help="Source folder"
    )
    parser.add_argument(
        "-t", "--target", default="target", help="Target folder"
    )
    args = parser.parse_args()
    return args


async def read_folder(source: AsyncPath):
    all_files = []
    async for path in source.iterdir():
        if await path.is_file():
            all_files.append(path)
        else:
            all_files.extend(await read_folder(path))
    return all_files


async def copy_file(files, target: AsyncPath):
    for file in files:
        new_path = AsyncPath(target, file.suffix, file.name)
        await new_path.parent.mkdir(parents=True, exist_ok=True)
        await copyfile(file, new_path)


async def main():
    args = get_args()
    source = AsyncPath(args.source)
    target = AsyncPath(args.target)
    files = await read_folder(source)
    await copy_file(files, target)


if __name__ == "__main__":
    asyncio.run(main())
