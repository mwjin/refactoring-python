class Shipment:
    def __init__(self, tracking_information):
        self._tracking_information = tracking_information

    @property
    def tracking_info(self):
        return self._tracking_information.display

    @property
    def tracking_information(self):
        return self._tracking_information

    @tracking_information.setter
    def tracking_information(self, tracking_information):
        self._tracking_information = tracking_information

    @property
    def tracking_number(self):
        return self._tracking_information.tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        self._tracking_information.tracking_number = tracking_number


class TrackingInformation:
    def __init__(self, shipping_company, tracking_number):
        self._shipping_company = shipping_company
        self._tracking_number = tracking_number

    @property
    def shipping_company(self):
        return self._shipping_company

    @shipping_company.setter
    def shipping_company(self, shipping_company):
        self._shipping_company = shipping_company

    @property
    def tracking_number(self):
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        self._tracking_number = tracking_number

    @property
    def display(self):
        return f"{self.shipping_company}: {self.tracking_number}"
