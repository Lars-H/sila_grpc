def temperature_unit(value):
    """
    Returns the string representation of a temperatur unit enum value
    :param value: Temperature enum value
    :return: String representation
    """
    if value == 0:
        return "Celcius"
    elif value == 1:
        return "Kelvin"
    elif value == 2:
        return "Fahrenheit"
    else:
        return "unknown"

def temperature_str(datapoint):
    """
    Returns the string representation of a temperature datapoint
    :param datapoint: datapoint
    :return: String representation
    """
    return str(datapoint.value) + " " + temperature_unit(datapoint.unit)