from rgbmatrix import RGBMatrix, RGBMatrixOptions


class LEDMatrix:
    def __init__(self, config):
        options = RGBMatrixOptions()
        options.rows = int(config["MATRIX"]["Width"])
        options.cols = int(config["MATRIX"]["Height"])
        options.brightness = 70
        options.limit_refresh_rate_hz = 60

        # This line is essential to make credential caching work
        #   See https://github.com/hzeller/rpi-rgb-led-matrix/issues/371
        options.drop_privileges = False

        self.matrix = RGBMatrix(options=options)

    def display_image(self, image):
        self.matrix.SetImage(image)

    def clear(self):
        self.matrix.Clear()
