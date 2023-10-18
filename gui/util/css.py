from io import StringIO

    
def build_css_string(class_name, **kwargs):
 
    try: 
        outputExprBuffer = StringIO()
        outputExprBuffer.write(f"{class_name} {{\n")
        
        for key, value in kwargs.items():
            modified_key = key.replace("_", "-")
            css_str = (f"\t{modified_key}: {value};\n")
            outputExprBuffer.write(css_str)
            
            
        outputExprBuffer.write("}")
        out_expr = outputExprBuffer.getvalue()

    finally:
        outputExprBuffer.close()

    return out_expr  