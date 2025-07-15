import json
import argparse


def update_version(json_file_path, version_data):
    with open(json_file_path, "r+") as f:
        data = json.load(f)
        data["apps"][0]["versions"].insert(0, version_data)
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Update apps.json with a new version entry")

    parser.add_argument("--file", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--buildVersion", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--localizedDescription", required=True)
    parser.add_argument("--downloadURL", required=True)
    parser.add_argument("--minOSVersion", required=True)
    parser.add_argument("--size", type=int, required=True)

    args = parser.parse_args()

    new_version = {
        "version": args.version,
        "buildVersion": args.buildVersion,
        "date": args.date,
        "localizedDescription": args.localizedDescription,
        "downloadURL": args.downloadURL,
        "minOSVersion": args.minOSVersion,
        "size": args.size,
    }

    update_version(args.file, new_version)


if __name__ == "__main__":
    main()
