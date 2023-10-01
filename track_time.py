import argparse
import datetime
from pathlib import Path
from pprint import pprint

DATA_DIR = Path("./user-data")
DATA_DIR.mkdir(exist_ok=True)


def main(f_name, **kwargs):
    start_time = datetime.datetime.now()
    try:
        while True:
            pass
    except KeyboardInterrupt as e:
        end_time = datetime.datetime.now()

        data = {
            "start_time": str(start_time),
            "end_time": str(end_time),
            "duration": str(end_time - start_time),
            "task": kwargs.get("task"),
        }
        pprint(data)
        with open(f_name, "a") as f:
            f.write(str(data) + "\n")


def manual(f_name, **kwargs):
    assert kwargs["duration"] is not None
    assert type(kwargs["duration"]) is int

    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(hours=kwargs["duration"])
    data = {
        "start_time": str(start_time),
        "end_time": str(end_time),
        "duration": str(end_time - start_time),
        "task": kwargs.get("task"),
    }

    pprint(data)
    with open(f_name, "a") as f:
        f.write(str(data) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("task", nargs="?", default="poly-ai", type=str)
    parser.add_argument("--duration", type=int)
    args = parser.parse_args()

    month = datetime.date.today().strftime("%m-%Y")
    month_dir = DATA_DIR / month
    month_dir.mkdir(exist_ok=True)

    date = datetime.date.today().strftime("%d-%m-%Y")
    f_name = month_dir / f"{date}.txt"

    if args.duration is not None:
        print("Adding task in a manual mode")
        manual(f_name, **args.__dict__)
        exit()
    main(f_name, **args.__dict__)
