from infcommon import logger
import functools

GREEN = '\033[92m'
CYAN = '\033[95m'
BLUE = '\033[94m'
ENDC = '\033[0m'


def _process_args(args):
    processed_args = []
    for arg in args:
        if 'object' in str(arg):
            processed_args.append(arg.__dict__)
        else:
            processed_args.append(arg)
    return processed_args

def mylogger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        processed_args = _process_args(list(args)[1:])
        processed_kwargs = _process_args(list(kwargs))
        logger.info("Method name: {}{}{} and input: {}{}{}{}".format(CYAN,
                                                                   func.__name__,
                                                                   ENDC,
                                                                   GREEN,
                                                                   processed_args,
                                                                   processed_kwargs,
                                                                   ENDC))
        result = func(*args, **kwargs)
        logger.info("Output: {}{}{}".format(BLUE, result, ENDC))
        return result
    return wrapper


