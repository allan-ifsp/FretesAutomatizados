class Package:

    def __init__(self, height, width, length, weight, price):
        self.__height = height
        self.__width = width
        self.__length = length
        self.__weight = weight
        self.__price = price

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def get_weight(self):
        return self.__weight

    def get_price(self):
        return self.__price
