class CustomVar:
    
    def __init__(self, value1, value2):
        self.x = value1
        self.y = value2
        
    def __repr__(self):  # developer-friendly representation
        "returns a string that would ideally recreate the object, used mainly for debugging and logging"
        return f"CustomVar(x={self.x}, y={self.y})"
    
    # def __str__(self): # user-friendly representation
    #     return f"x={self.x}, y={self.y}"
    
a = CustomVar(1, 2)
print(a)