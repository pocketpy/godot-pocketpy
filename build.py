import os

def run(cmd: str):
    print(cmd)
    code = os.system(cmd)
    assert code == 0

config = 'Debug'

run(f"cmake -B build -DCMAKE_BUILD_TYPE={config}")
run(f"cmake --build build --config {config}")