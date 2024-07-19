from fastapi import Request
import logging, time, sys

logger = logging.getLogger()

formatter = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s - %(message)s',
)
stream_handler = logging.StreamHandler(sys.stdout)
logger.handlers = [stream_handler]
logger.setLevel(logging.INFO)

async def log_middleware(request: Request, call_next):
    start = time.time()
    process_time = time.time() - start
    log_dict = {
        'url': request.url.path,
        'method': request.method, 
        'response_time': process_time
    }
    logger.info(log_dict)

    response = await call_next(request)
    return response