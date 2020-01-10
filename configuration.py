import argparse
import configparser
import logging
from writer import Writer

config = {
    "init_pos_limit": 10.0,
    "sheep_move_dist": 0.5,
    "wolf_move_dist": 1.0,
    "dir_to_save": "",
    "log": logging.WARNING,
    "rounds": 50,
    "sheep": 15,
    "wait": False
}


def create_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", metavar="FILE",
                        help="określa plik konfiguracyjny")
    parser.add_argument("-d", "--dir", metavar="DIR",
                        help="określa katalog, w którym mają zostać zapisane pliki pos.json, alive.csv oraz opcjonalnie chase.log")
    parser.add_argument("-l", "--log", metavar="LEVEL",
                        help="określa poziom zapisu zdarzeń do dziennika chase.log")
    parser.add_argument("-r", "--rounds", metavar="NUM",
                        help="określa określa liczbę tur")
    parser.add_argument("-s", "--sheep", metavar="NUM",
                        help="określa liczbę owiec")
    parser.add_argument("-w", "--wait", metavar="0-1",
                        help="określa czy program ma czekać na akcję użytkownika po każdej turze")
    args = parser.parse_args()
    set_config_args(args)


def set_config_args(args):
    if len(list(filter(lambda x: getattr(args, x), vars(args)))) != 0:
        if args.config:
            config_file_path = args.config
            cp = configparser.ConfigParser()
            cp.read(config_file_path)
            config["init_pos_limit"] = float(cp["Terrain"]["InitPosLimit"])
            config["sheep_move_dist"] = float(cp["Movement"]["SheepMoveDist"])
            config["wolf_move_dist"] = float(cp["Movement"]["WolfMoveDist"])

        if args.dir:
            config["dir_to_save"] = args.dir
            Writer.make_directory(config["dir_to_save"])

        if args.log:
            args.log = args.log.upper()
            if args.log == "DEBUG":
                config["log"] = logging.DEBUG
            elif args.log == "WARNING":
                config["log"] = logging.WARNING
            elif args.log == "INFO":
                config["log"] = logging.INFO
            elif args.log == "ERROR":
                config["log"] = logging.ERROR
            elif args.log == "CRITICAL":
                config["log"] = logging.CRITICAL
            else:
                config["log"] = "NOT_VALID"

        if args.rounds:
            config["rounds"] = int(args.rounds)

        if args.sheep:
            config["sheep"] = int(args.sheep)

        if args.wait == str(1):
            config["wait"] = True
