import decimal

class SensorValue:
    _TEMPLATE = '/path/to/sensor{num}'  # шаблон шляху до датчика
    
    def __init__(self, sensor_num=0, *, _tpl=None):
        sensor_num = int(sensor_num)

        tpl = self._TEMPLATE if _tpl is None else _tpl
        self.sensor = tpl.format(num=sensor_num)

    @classmethod
    def convert_value(cls, value):
        value = int(value)
        dec = decimal.Decimal(str(value))
        return dec

    def get_raw_value(self):
        with open(self.sensor, 'r') as file:
            val = file.readline().strip()

        return val

    def get_value(self):
        val = self.get_raw_value()
        return self.convert_value(val)


class LoudnessSensor(SensorValue):
    _TEMPLATE = '/path/to/microphone{num}'  # шаблон шляху до мікрофона

    def __init__(self, sensor_num=0, *, _tpl=None):
        super().__init__(sensor_num, _tpl=_tpl)

    def get_loudness(self):
        return self.get_value()


class CameraSensor(SensorValue):
    _TEMPLATE = '/path/to/camera{num}'  # шаблон шляху до веб-камери

    def __init__(self, sensor_num=0, *, _tpl=None):
        super().__init__(sensor_num, _tpl=_tpl)

    def get_color(self):
      
        return self.get_value()


if __name__ == '__main__':
    loudness_sensor = LoudnessSensor()
    loudness_value = loudness_sensor.get_loudness()
    print(f"Loudness: {loudness_value}")

    camera_sensor = CameraSensor()
    color_value = camera_sensor.get_color()
    print(f"Color: {color_value}")
