import asyncio
import logging
import os
import signal
import sys
import threading
from types import FrameType
from typing import Optional

# If uvloop is installed, use it to run async loop
try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:  # pragma: no cover
    pass

# Signals that should be handled by application
if sys.platform != "win32":
    HANDLED_SIGNALS = (
        signal.SIGINT,  # Unix signal 2. Sent by Ctrl+C .
        signal.SIGTERM,  # Unix signal 15. Sent by `kill <pid>`.
        signal.SIGHUP,
    )
if sys.platform == "win32":
    # Windows signal 21. Sent by Ctrl+Break.
    HANDLED_SIGNALS = (
        signal.SIGINT,  # Unix signal 2. Sent by Ctrl+C.
        signal.SIGTERM,  # Unix signal 15. Sent by `kill <pid>`.
        signal.SIGBREAK,
    )

# setup loggers
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


async def run_application() -> None:
    logger.info("Starting application...")
    while True:
        await asyncio.sleep(1)
        logger.info("Application is running...")


def main() -> None:
    logger.info("Starting... PID: %s", os.getpid())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    def handle_exit(signal_number: int, frame: Optional[FrameType]) -> None:
        logger.info(
            "Received signal %s. Sending stop signal to application...",
            signal.Signals(signal_number).name,
        )

    # Prepare signal handlers
    if threading.current_thread() is not threading.main_thread():
        logger.warning("Cannot install signal handlers from non-main thread")
        return

    try:
        for sig in HANDLED_SIGNALS:
            if sig is not None:
                signal.signal(sig, handle_exit)
        logger.info("Signal handlers installed")
    except NotImplementedError:  # pragma: no cover
        logger.warning("Signals are not supported. Possible on Windows")
        # Windows
        for sig in HANDLED_SIGNALS:
            if sig is not None:
                signal.signal(sig, handle_exit)
        logger.info("Signal handlers installed")

    # Start application loop
    main_task = loop.create_task(run_application())

    try:
        loop.run_until_complete(main_task)
    except KeyboardInterrupt:
        main_task.cancel()
        loop.run_until_complete(main_task)
        main_task.exception()
    finally:
        loop.close()


if __name__ == "__main__":
    main()
