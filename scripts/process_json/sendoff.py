import os
import subprocess

files = os.listdir("./")
print(files)
files = [f for f in files if f.endswith(".json")]
print(files)
files = [f for f in files if f.startswith("all-")]
print(files)
files.remove("all-0.json")
print(files)

for file in files:
    print(f"DAN!!! Processing {file}")
    thing = subprocess.run(
        ["python", "process_json.py", "--filepath", file, "--extract_metadata", "True"],
    )
    print(f"DAN!!! Finished processing {file}")
