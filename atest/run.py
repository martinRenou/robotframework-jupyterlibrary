import sys
import subprocess
import os

# import for PATH side-effect. yuck.
import chromedriver_binary  # noqa

here = os.path.dirname(__file__)
out = os.path.join(here, "..", "_artifacts", "test_output")
tests = os.path.join(here, "acceptance")


def run_tests(*robot_args):
    proc = subprocess.Popen([
        "python", "-m", "robot", "-d", out,
        ] + list(robot_args) + [
            tests,
        ], cwd=here)

    try:
        return proc.wait()
    except KeyboardInterrupt:
        proc.kill()
        return proc.wait()


if __name__ == "__main__":
    sys.exit(run_tests(*sys.argv[1:]))
