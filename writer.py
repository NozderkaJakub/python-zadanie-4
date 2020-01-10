import os
import csv
import json
import logger


class Writer:

    @classmethod
    def make_directory(cls, directory):
        logger.log_debug(__name__, "make_directory", directory, "brak")

        if directory:
            if not os.path.exists(directory):
                os.mkdir(directory)

    @classmethod
    def write_to_csv(cls, simulation_results=[], csv_file_name="alive.csv", directory=""):
        params = "simulation_results: {}, csv_file_name: {}, directory: {}".format(
            str(simulation_results), csv_file_name, directory)
        logger.log_debug(__name__, "write_to_csv", params, "brak")

        with open((csv_file_name if directory == "" else "./" + directory + "/" + csv_file_name), "w+") as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerow(["turn_no", "alive_sheep_amount"])
            for i in range(len(simulation_results)):
                turn_result = simulation_results[i]
                row = [turn_result["turn_no"], turn_result["alive_sheep_amount"]]
                csv_writer.writerow(row)

    @classmethod
    def write_to_json(cls, simulation_results=[], json_file_name="pos.json", directory=""):
        params = "simulation_results: {}, json_file_name: {}, directory: {}".format(
            str(simulation_results), json_file_name, directory)
        logger.log_debug(__name__, "write_to_json", params, "brak")

        with open((json_file_name if directory == "" else "./" + directory + "/" + json_file_name), "w+") as save_file:
            pos_list_json = json.dumps(simulation_results, indent=4)
            save_file.write(pos_list_json)
