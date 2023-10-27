from io import StringIO
from typing import Dict

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
        background_color = "#242933",
        color = "#CBE1FF",
        border_radius = "2px",
        font_family = "roboto",
        font_size = "28px",
        **kwargs
    )

def component_light_grey(component_name, **kwargs: Dict[str, str]) -> str:

    return build_css_string(
        component_name, 
        background_color="#363E4D", 
        color="#CBE1FF", 
        border_radius="2px",
        font_family = "roboto", 
        font_size = "28px",
        **kwargs
    )

def component_blue(component_name, **kwargs: Dict[str, str]) -> str:

    return build_css_string(
        component_name, 
        background_color="#0060E5", 
        color="#CBE1FF", 
        border_radius="2px",
        font_family = "roboto", 
        font_size = "28px",
        **kwargs
    )

def component_red(component_name, **kwargs: Dict[str, str]) -> str:

    return build_css_string(
        component_name, 
        background_color="#FF3F46", 
        color="#CBE1FF", 
        border_radius="2px",
        font_family = "roboto", 
        font_size = "28px",
        **kwargs
    )