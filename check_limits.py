

def check_temp_limits(temperature):
     if temperature < 0 or temperature > 45:
        return False
     return True
     
def check_soc_limits(soc):
  if soc < 20 or soc > 80:
      return False
  return True
  
def check_charge_rate (charge_rate):
  if charge_rate > 0.8:
      return False
  return True
  
def battery_is_ok(temperature, soc, charge_rate):
  return check_temp_limits(temperature) and check_soc_limits(soc) and check_charge_rate(charge_rate)
   

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
