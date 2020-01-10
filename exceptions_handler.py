import configuration
import logger


def raise_exceptions():
    logger.log_debug(__name__, "raise_exceptions", "brak", "brak")
    check_if_non_positive_variable_exists()
    check_if_non_int_variable_exists()


def handle_exceptions(message):
    logger.log_debug(__name__, "handle_exceptions", "brak", "brak")
    logger.log_error(__name__, "Wyjatek: {}".format(message))
    print(message)


def check_if_non_positive_variable_exists():
    logger.log_debug(
        __name__, "check_if_non_positive_variable_exists", "brak", "brak")
    non_positive_variables = get_non_positive_variables()
    if len(non_positive_variables) > 0:
        message = "Wartosc zmiennej {} nie jest liczba dodatnia."
        if len(non_positive_variables) > 1:
            message = "Wartosci zmiennych {} nie sa liczbami dodatnimi."
        raise ValueError(message.format(non_positive_variables))


def check_if_non_int_variable_exists():
    logger.log_debug(
        __name__, "check_if_non_int_variable_exists", "brak", "brak")
    non_int_variables = get_non_int_variables()
    if len(non_int_variables) > 0:
        message = "Wartosc zmiennej {} nie jest liczba calkowita."
        if len(non_int_variables) > 1:
            message = "Wartosci zmiennych {} nie sa liczbami calkowitymi."
        raise ValueError(message.format(non_int_variables))


def get_non_positive_variables():
    logger.log_debug(
        __name__, "get_non_positive_variables", "brak", "brak")
    non_positive_variables = []
    if configuration.config["init_pos_limit"] <= 0.0:
        non_positive_variables.append("init_pos_limit")
    if configuration.config["sheep_move_dist"] <= 0.0:
        non_positive_variables.append("sheep_move_dist")
    if configuration.config["wolf_move_dist"] <= 0.0:
        non_positive_variables.append("wolf_move_dist")
    if configuration.config["rounds"] <= 0.0:
        non_positive_variables.append("rounds")
    if configuration.config["sheep"] <= 0.0:
        non_positive_variables.append("sheep")
    return non_positive_variables


def get_non_int_variables():
    logger.log_debug(
        __name__, "get_non_int_variables", "brak", "brak")
    non_int_variables = []
    if type(configuration.config["rounds"]) != int:
        non_int_variables.append("rounds")
    if type(configuration.config["sheep"]) != int:
        non_int_variables.append("sheep")
    return non_int_variables
