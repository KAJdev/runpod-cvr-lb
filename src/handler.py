import time
import runpod


def handler(job):
    # sleep for 10 seconds to simulate a long running job
    time.sleep(10)

    # return some bytes to test what happens when the output is not a string
    return bytes(b"asedfkmeaklwfm")


runpod.serverless.start({"handler": handler})
