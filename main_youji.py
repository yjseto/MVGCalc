class ClearInputButton():
    def __init__(self, **kwargs):

        self.kwargs = kwargs

        #tempString match string below
        #replace underscore with - in key value
        # for key, value in kwargs.items():
        #         print(f"{key}: {value}")  

    def build_css_string(self):
        return self.kwargs

#expected
print(
    """
    QPushButton {
        background-color: #0060E5;
        color: #CBE1FF;
        border-radius: 2px;
        border-top-right-radius: 8px;
        font-family: roboto;
        font-size: 38px;
    }
    """
)   

#actual
testObj = ClearInputButton(background_color="value1", arg2="value2", arg3="value3")

print(testObj.build_css_string())
