import unittest
from battery_management_system import BatteryManagementSystem


class TestBatteryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.battery_check_lang_en = BatteryManagementSystem(language='en')
        self.battery_check_lang_de = BatteryManagementSystem(language='de')

    def test_soc_within_limits(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=25, charge_rate=0.4)[0], "All parameters are within the limits.")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=25, charge_rate=0.4)[0], "Alle Parameter sind innerhalb der Grenzen.")

    def test_soc_warning_approaching_discharge(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=22, temperature=25, charge_rate=0.4)[0], "Warning: Approaching discharge")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=22, temperature=25, charge_rate=0.4)[0], "Warnung: Annäherung an die Entladung")

    def test_soc_warning_approaching_charge_peak(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=78, temperature=25, charge_rate=0.4)[0], "Warning: Approaching charge-peak")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=78, temperature=25, charge_rate=0.4)[0], "Warnung: Annäherung an die Ladungsspitze")

    def test_soc_error(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=19, temperature=25, charge_rate=0.4)[0], "Error: State of Charge out of bounds!")
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=81, temperature=25, charge_rate=0.4)[0], "Error: State of Charge out of bounds!")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=19, temperature=25, charge_rate=0.4)[0], "Fehler: Ladezustand außerhalb der Grenzen!")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=81, temperature=25, charge_rate=0.4)[0], "Fehler: Ladezustand außerhalb der Grenzen!")

    def test_temperature_within_limits(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=25, charge_rate=0.4)[1], "All parameters are within the limits.")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=25, charge_rate=0.4)[1], "Alle Parameter sind innerhalb der Grenzen.")

    def test_temperature_warning_low(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=2, charge_rate=0.4)[1], "Warning: Approaching lower temperature limit")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=2, charge_rate=0.4)[1], "Warnung: Annäherung an die untere Temperaturgrenze")

    def test_temperature_warning_high(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=43, charge_rate=0.4)[1], "Warning: Approaching upper temperature limit")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=43, charge_rate=0.4)[1], "Warnung: Annäherung an die obere Temperaturgrenze")

    def test_temperature_error(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=-1, charge_rate=0.4)[1], "Error: Temperature out of bounds!")
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=46, charge_rate=0.4)[1], "Error: Temperature out of bounds!")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=-1, charge_rate=0.4)[1], "Fehler: Temperatur außerhalb der Grenzen!")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=46, charge_rate=0.4)[1], "Fehler: Temperatur außerhalb der Grenzen!")

    def test_charge_rate_within_limits(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=25, charge_rate=0.4)[2], "All parameters are within the limits.")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=25, charge_rate=0.4)[2], "Alle Parameter sind innerhalb der Grenzen.")

    def test_charge_rate_warning(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=25, charge_rate=0.77)[2], "Warning: Approaching charge-peak")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=25, charge_rate=0.77)[2], "Warnung: Annäherung an die Ladungsspitze")

    def test_charge_rate_error(self):
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=25, charge_rate=0.81)[2], "Error: Charge Rate out of bounds!")
        self.assertEqual(self.battery_check_lang_en.monitor_battery(soc=50, temperature=25, charge_rate=-0.01)[2], "Error: Charge Rate out of bounds!")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=25, charge_rate=0.81)[2], "Fehler: Ladegeschwindigkeit außerhalb der Grenzen!")
        self.assertEqual(self.battery_check_lang_de.monitor_battery(soc=50, temperature=25, charge_rate=-0.01)[2], "Fehler: Ladegeschwindigkeit außerhalb der Grenzen!")

if __name__ == '__main__':
    unittest.main()
