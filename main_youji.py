from gui.util.css import build_css_string


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
testObj = build_css_string("QPushButton", background_color="#0060E5", color="#CBE1FF", border_radius="2px",
                           border_top_right_radius = "8px", font_family = "roboto", font_size = "38px" )

print(testObj)
