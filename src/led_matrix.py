from rgbmatrix import RGBMatrix, RGBMatrixOptions


class LEDMatrix:
    def __init__(self, config):
        options = RGBMatrixOptions()
        options.rows = int(config["MATRIX"]["Width"])
        options.cols = int(config["MATRIX"]["Height"])
        options.brightness = 70
        options.limit_refresh_rate_hz = 60
        options.hardware_mapping = config["MATRIX"]["Mapping"]

        # This line is essential to make credential caching work
        #   See https://github.com/hzeller/rpi-rgb-led-matrix/issues/371
        options.drop_privileges = False

        self.matrix = RGBMatrix(options=options)

    def display_image(self, image):
        self.matrix.SetImage(image)
    
    def display_frame(self, frame):
        self.matrix.SwapOnVSync(frame)

    def clear(self):
        self.matrix.Clear()

    def create_blank_frame(self):
        return self.matrix.CreateFrameCanvas()
