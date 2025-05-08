import time
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--suite-timeout",
        action="store",
        type=int,
        default=None,
        help="Fail all tests if the suite runtime exceeds this timeout in seconds.",
    )


def pytest_configure(config):
    timeout = config.getoption("suite_timeout")
    if timeout:
        config.suite_timeout = timeout
        config.suite_start_time = time.time()
        config.suite_timed_out = False


def pytest_runtest_setup(item):
    config = item.config
    timeout = getattr(config, "suite_timeout", None)
    start_time = getattr(config, "suite_start_time", None)
    if timeout and start_time:
        elapsed = time.time() - start_time
        if elapsed > timeout:
            config.suite_timed_out = True
            pytest.fail(
                f"Test suite exceeded the timeout of {timeout} seconds "
                f"(Elapsed: {int(elapsed)}s)",
                pytrace=False,
            )
