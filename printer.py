import logger


class Printer:

    @classmethod
    def print_simulation_results(self, simulation_results, wait=False):
        params = "simulation_results: {}, wait: {}".format(
            str(simulation_results), wait)
        logger.log_debug(__name__, "print_simulation_results", params, "brak")
        logger.log_info(__name__, "Wyswietlono wyniki symulacji")

        turn_info_template = "nr tury: {} pozycja wilka: ({:.3f}, {:.3f}) l. żywych owiec: {}"
        for i in range(len(simulation_results)):
            turn_result = simulation_results[i]
            turn_info = turn_info_template.format(
                turn_result.get("turn_no"),
                turn_result.get("wolf_pos")[0],
                turn_result.get("wolf_pos")[1],
                turn_result.get("alive_sheep_amount")
            )
            print(turn_info)
            if wait:
                input("Nacisnij ENTER, aby kontynuowac...")
