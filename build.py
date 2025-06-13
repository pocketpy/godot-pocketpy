import os

def run(cmd: str):
    print(cmd)
    code = os.system(cmd)
    assert code == 0

run("cmake -B build -DCMAKE_BUILD_TYPE=Release")
run("cmake --build build --config Release")