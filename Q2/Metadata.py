
#https://reliabilitywhisperer.substack.com/p/practical-coding-interview-questions

# Problem: You are given a file (files.txt) where each line represents a file entry with its path, size in bytes, 
# and last modified timestamp (Unix epoch). 
# The format is comma-separated: filepath,size,modified_timestamp.`

from collections import defaultdict

def metadata():

    files = []
    with open("file.txt", "r") as file:
        for line in file:
            files.append((line.split(",")[0].strip(), int(line.split(",")[1].strip()), int(line.split(",")[2].strip())))
    
    dir_sizes = defaultdict(int)
    for path, size, _ in files:
        top_dir = "/" + path.strip("/").split("/")[0]
        dir_sizes[top_dir] += size

    print("✅ Total Size by Top-Level Directory:")
    for dir_, total in dir_sizes.items():
        print(f"{dir_:15} {total} bytes")

    ext_sizes = defaultdict(int)
    for path, size, _ in files:
        ext = path.split(".")[1] if "." in path else "no_ext"
        ext_sizes[ext] += size

    print("\n✅ Total Size by File Extension:")
    for ext, total in ext_sizes.items():
        print(f"{ext:8} {total} bytes")  

    sorted_by_time = sorted(files, key=lambda x: x[2], reverse=True)
    for path, _, time in sorted_by_time:
        print(f"{path:30} {time} bytes")



metadata()