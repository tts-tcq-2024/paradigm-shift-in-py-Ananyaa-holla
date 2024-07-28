class BatteryManagementSystem:
    def __init__(self, language='en'):
        self.language = language
        self.messages = {
            'en': {
                'ok': "All parameters are within the limits.",
                'warning_discharge': "Warning: Approaching discharge",
                'warning_charge_peak': "Warning: Approaching charge-peak",
                'warning_temp_low': "Warning: Approaching lower temperature limit",
                'warning_temp_high': "Warning: Approaching upper temperature limit",
                'error_soc': "Error: State of Charge out of bounds!",
                'error_temp': "Error: Temperature out of bounds!",
                'error_charge_rate': "Error: Charge Rate out of bounds!"
            },
            'de': {
                'ok': "Alle Parameter sind innerhalb der Grenzen.",
                'warning_discharge': "Warnung: Annäherung an die Entladung",
                'warning_charge_peak': "Warnung: Annäherung an die Ladungsspitze",
                'warning_temp_low': "Warnung: Annäherung an die untere Temperaturgrenze",
                'warning_temp_high': "Warnung: Annäherung an die obere Temperaturgrenze",
                'error_soc': "Fehler: Ladezustand außerhalb der Grenzen!",
                'error_temp': "Fehler: Temperatur außerhalb der Grenzen!",
                'error_charge_rate': "Fehler: Ladegeschwindigkeit außerhalb der Grenzen!"
            }
        }
        self.min_temp = 0
        self.max_temp = 45

        self.min_soc = 20
        self.max_soc = 80

        self.min_charge_rate = 0
        self.max_charge_rate = 0.8

    def get_range(self, value, lower_limit, upper_limit, warning_range, low_warning_msg, high_warning_msg, error_msg):
        """
       Check if the input lies within range/limits and return the corresponding message
        """
        if value < lower_limit:
            return self.messages[self.language][error_msg]
        elif value < lower_limit + warning_range:
            return self.messages[self.language][low_warning_msg]
        elif value > upper_limit:
            return self.messages[self.language][error_msg]
        elif value > upper_limit - warning_range:
            return self.messages[self.language][high_warning_msg]
        else:
            return self.messages[self.language]['ok']

    def monitor_battery(self, soc, temperature, charge_rate):
        """
        Monitor the battery status based on the given input from the user
        """
        # Calculate Tollerance value
        soc_warning_range = 0.05 * self.max_soc
        temp_warning_range = 0.05 * self.max_temp
        charge_rate_warning_range = 0.05 * self.max_charge_rate
        
        soc_status = self.get_range(soc, 20, 80, soc_warning_range, 'warning_discharge', 'warning_charge_peak', 'error_soc')
        temp_status = self.get_range(temperature, 0, 45, temp_warning_range, 'warning_temp_low', 'warning_temp_high', 'error_temp')
        charge_rate_status = self.get_range(charge_rate, 0, 0.8, charge_rate_warning_range, 'warning_discharge', 'warning_charge_peak', 'error_charge_rate')
        
        return soc_status, temp_status, charge_rate_status
