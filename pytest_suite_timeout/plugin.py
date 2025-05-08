import time
import pytest

# Key to store suite timeout expiration in pytest config stash
suite_timeout_stash = pytest.StashKey[float]()


def pytest_addoption(parser):
    group = parser.getgroup("custom suite timeout")
    group.addoption(
        "--suite-timeout",
        action="store",
        type=float,
        default=None,
        dest="suite_timeout_value",
        metavar="SECONDS",
        help="⏱️ Set a timeout (in seconds) for the entire test suite. If the timeout is reached,"
        " the test session will fail. Does not stop tests already in progress.",
    )


def pytest_configure(config):
    timeout_seconds = config.getoption("suite_timeout_value")
    if timeout_seconds is not None:
        deadline = time.time() + timeout_seconds
        print(f"⏰ [suite-timeout] Suite timeout set to {timeout_seconds:.2f} seconds")
    else:
        deadline = 0.0
        print("⚙️ [suite-timeout] No suite timeout configured")
    config.stash[suite_timeout_stash] = deadline


def pytest_runtest_makereport(item, call):
    config = item.config
    deadline = config.stash.get(suite_timeout_stash, 0.0)
    current_time = time.time()

    if deadline and current_time > deadline:
        timeout_value = config.getoption("suite_timeout_value")
        item.session.shouldfail = (
            f"💥 suite-timeout: exceeded {timeout_value:.2f} seconds ⛔"
        )
