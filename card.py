class card:
    #colors = ["red", "green", "blue"]
    colors = ["red"]
    fillings = ["empty", "filled", "striped"]
    numbers = [1,2,3]
    shapes = ["snake"]
    #shapes = ["snake", "oval", "diamond"]
    def __init__(self, color: str, filling: str, number:int, shape:str) -> None:
        
        if color not in ["red", "green", "blue"]:
            raise ValueError("Color has to be red, green or blue")
        if filling not in ["empty", "filled", "striped"]:
            raise ValueError("Filling has to be empty, filled or striped")
        if number not in range(1,4):
            raise ValueError("The number has to be between 1 and 3")
        if shape not in ["snake", "oval", "diamond"]:
            raise ValueError("Shape has to be snake, oval or diamond")
        self.color = card.colors.index(color)
        self.filling = card.fillings.index(filling)
        self.number = number-1
        self.shape = card.shapes.index(shape)

    def get_number(self):
        return self.number+1

    def get_filling(self):
        return card.fillings[self.filling]
    
    def get_color(self):
        return card.colors[self.color]
    
    def get_shape(self):
        return card.shapes[self.shape]
    
    def __str__(self) -> str:
        return f"card with {self.get_number()} {self.get_color()} {self.get_shape()} with {self.get_filling()} filling"
    
    def __eq__(self, value: object) -> bool:
        if self.color == value.color and self.shape == value.shape and self.number == value.number and self.filling == value.filling:
            return True
        return False
    
    def complete_attribute(self, att1, att2):
        return (3-att1-att2)%3
    
    def get_setting_card(self, second_card):
        color = card.colors[self.complete_attribute(self.color, second_card.color)]
        shape = card.shapes[self.complete_attribute(self.shape, second_card.shape)]
        number = card.numbers[self.complete_attribute(self.number, second_card.number)]
        filling = card.fillings[self.complete_attribute(self.filling, second_card.filling)]
        return card(color, filling, number, shape)