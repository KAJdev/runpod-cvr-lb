import time
import runpod
import subprocess


def handler(job):
    """get CUDA version"""

    # sleep for 10 seconds to simulate a long running job
    time.sleep(10)

    print("this is a log that should be captured by sls-local-server")

    output = subprocess.check_output(["nvcc", "--version"]).decode("utf-8")
    print(output)
    return output.split("\n")[3]


# asedfkmeaklwfm

runpod.serverless.start({"handler": handler})
