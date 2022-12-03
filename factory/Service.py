import config
from service.CardDetection import CardDetection
from service.CardDetectionKeras import CardDetectionKeras


class Service:

    def __init__(self):
        self.service_type = config.SERVICE_TYPE

    def get_service(self):
        if self.service_type == "ML":
            return CardDetection()
        else:
            return CardDetectionKeras()
