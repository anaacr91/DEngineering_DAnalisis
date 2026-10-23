february = {
    "Madrid": {"temperature": 13, "humidity": 6, "rainfall": 0},
    "Tenerife": {"temperature": 17, "humidity": 21, "rainfall": 15},
    "Benidorm": {"temperature": 16, "humidity": 11, "rainfall": 5},
}


def print_climate_report(location, month_dict):
    t = month_dict["temperature"]
    h = month_dict["humidity"]
    r = month_dict["rainfall"]
    ratio = h / r
    print("Instrument World " + location + " has:")
    print(str(t) + " degrees")
    print(str(h) + " humidity percent")
    print("The ratio of humidity and rainfall percent is " + str(ratio))


if __name__ == "__main__":
    for location, data_dict in february.items():
        try:
            print_climate_report(location, data_dict)
        except Exception:
            print("Could not print report for " + location)
