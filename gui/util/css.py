from io import StringIO
from typing import Dict

from gui.enums.styles import COLORS

def build_css_string(component_name, **kwargs: Dict[str, str]) -> str:
 
    try: 
        outputExprBuffer = StringIO()
        outputExprBuffer.write(f"{component_name} {{\n")
        
        for key, value in kwargs.items():
            modified_key = key.replace("_", "-")
            css_str = (f"\t{modified_key}: {value};\n")
            outputExprBuffer.write(css_str)
            
            
        outputExprBuffer.write("}")
        out_expr = outputExprBuffer.getvalue()

    finally:
        outputExprBuffer.close()

    return out_expr  

def component_dark_grey(component_name, **kwargs: Dict[str, str]) -> str:
    
    return build_css_string(
        component_name, 
        background_color = COLORS.DARK_GREY.value,
        color = COLORS.WHITE.value,
        border_radius = "2px",
        **kwargs
    )

def component_light_grey(component_name, **kwargs: Dict[str, str]) -> str:

    return build_css_string(
        component_name, 
        background_color= COLORS.LIGHT_GREY.value, 
        color= COLORS.WHITE.value, 
        border_radius="2px",
        **kwargs
    )

def component_blue(component_name, **kwargs: Dict[str, str]) -> str:

    return build_css_string(
        component_name, 
        background_color= COLORS.BLUE.value, 
        color= COLORS.WHITE.value, 
        border_radius="2px",
        **kwargs
    )

def component_red(component_name, **kwargs: Dict[str, str]) -> str:

    return build_css_string(
        component_name, 
        background_color= COLORS.RED.value, 
        color=COLORS.WHITE.value, 
        border_radius="2px",
        **kwargs
    )

def component_pale_gray(component_name, **kwargs: Dict[str, str]) -> str:

    return build_css_string(
        component_name, 
        background_color= COLORS.PALE_GRAY.value, 
        color=COLORS.BLACK.value, 
        border_radius="15px",
        font_size = "17px",
        **kwargs
    )

def component_black(component_name, **kwargs: Dict[str, str]) -> str:

    return build_css_string(
        component_name, 
        background_color= COLORS.BLACK.value, 
        color=COLORS.WHITE.value, 
        border_radius="15px",

        font_size = "17px",
        **kwargs
    )
    
def component_nav_gray(component_name, **kwargs: Dict[str, str]) -> str:

    return build_css_string(
        component_name, 
        background_color= COLORS.NAV_GRAY.value, 
        color=COLORS.WHITE.value, 
        font_size = "14px",
        **kwargs
    )