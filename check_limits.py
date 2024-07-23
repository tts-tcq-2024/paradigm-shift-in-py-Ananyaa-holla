

def evaluate_and_alert_warning_levels(value, min_value, max_value,warning_msg):
    if value in range(int(min_value), int(max_value)):
        print(warning_msg)   

def check_temp_limits(temperature):
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
        return False
    else:
        evaluate_and_alert_warning_levels(temperature, 0, 2.25,"Warning: Approaching discharge")
        evaluate_and_alert_warning_levels(temperature, 43.2,46,"Warning: Approaching charge-peak")
        return True
     
def check_soc_limits(soc):
  if soc < 20 or soc > 80:
      print('State of Charge is out of range!')
      return False
  else:
        evaluate_and_alert_warning_levels(soc, 20, 24,"Warning: Approaching discharge")
        evaluate_and_alert_warning_levels(soc, 76, 81,"Warning: Approaching charge-peak")
        return True
  
def check_charge_rate (charge_rate):
  if charge_rate > 0.8:
      print('Charge rate is out of range!')
      return False
  else:
      evaluate_and_alert_warning_levels(charge_rate, 0.76, 0.81,"Warning: Approaching charge-peak")
      return True
  
def battery_is_ok(temperature, soc, charge_rate):
  return check_temp_limits(temperature) and check_soc_limits(soc) and check_charge_rate(charge_rate)
   
