import logging


def create_basic_config(config):
    logging.basicConfig(
        filename='./' + config["dir_to_save"] + '/chase.log'
        if config["dir_to_save"] else 'chase.log',
        filemode="w+", level=config["log"])


debug_template = "::m={}; p={}; w={}"


def log_debug(module_name, method_name, params, output):
    logger = logging.getLogger(module_name)
    logger.debug(debug_template.format(method_name, params, output))


def log_info(module_name, message):
    logger = logging.getLogger(module_name)
    logger.info(message)


def log_warning(module_name, message):
    logger = logging.getLogger(module_name)
    logger.warning(message)


def log_error(module_name, message):
    logger = logging.getLogger(module_name)
    logger.error(message)


def log_critical(module_name, message):
    logger = logging.getLogger(module_name)
    logger.critical(message)