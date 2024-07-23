import unittest
from check_limits import battery_is_ok
class TestBatteryLimits(unittest.TestCase):
        
        def test_temperature_out_of_range(self):
                assert(battery_is_ok(50, 70, 0.7) is False)
                assert(battery_is_ok(-1, 70, 0.7) is False)

        def test_temperature_in_range(self):
               assert(battery_is_ok(43, 70, 0.7) is True)
               assert(battery_is_ok(5, 70, 0.7) is True)

        def test_soc_out_of_range(self):
               assert(battery_is_ok(43, 19, 0.7) is False)
               assert(battery_is_ok(5, 99, 0.7) is False)
        
        def test_soc_in_range(self):
               assert(battery_is_ok(43, 20, 0.7) is True)
               assert(battery_is_ok(5, 70, 0.7) is True)

        def test_charge_rate_out_range(self):
               assert(battery_is_ok(43, 70, 0.9) is False)


        def test_charge_in_range(self):
               assert(battery_is_ok(43, 70, 0.7) is True)
               assert(battery_is_ok(5, 70, 0.1) is True)
                



if __name__ == '__main__':
    unittest.main()


