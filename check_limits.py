def battery_is_ok(temperature, soc, charge_rate):
  if (temperature < 0 or temperature > 45) or (soc < 20 or soc > 80) or (charge_rate > 0.8):
      return False
  else:
    return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
