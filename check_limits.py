from battery_management_system import BatteryManagementSystem
battery_check_lang_en = BatteryManagementSystem(language='en')
print(battery_check_lang_en.monitor_battery(soc=50, temperature=25, charge_rate=0.4))
