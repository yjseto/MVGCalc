from lib.enums.base import BaseEnum,UnitEnum

class Measure(BaseEnum):
    LENGTH      = (1, "Length")
    WEIGHT      = (2, "Weight")
    TEMP        = (3, "Temp")

class Length(UnitEnum):
    METER       = (1,"meter", 1,"m")
    KILOMETER   = (2,"kilometer",1000,"km")
    CENTIMETER  = (3,"centimeter",0.01,"cm")
    MILIMETER   = (4,"milimeter",0.001,"mm")
    MICROMETER  = (5,"micrometer",0.000001,"mic m")
    NANOMETER   = (6,"nanometer",0.0000000001,"nm")
    MILE        = (7,"mile",1609.35,"mile")
    YARD        = (8,"yard",0.9144,"yd")
    FOOT        = (9,"foot",0.3048,"ft")
    INCH        = (10,"inch",0.0254,"in")

class Weight(UnitEnum):
    KILOGRAM        = (1,"kilogram",1,"kg")
    GRAM            = (2,"gram",1000,"g")
    MILIGRAM        = (3, "miligram",1000000,"mg")
    METRIC_TON      = (4,"metric ton",0.001,"mt")
    POUND           = (5,"pound",2.2046,"lbs")
    OUNCE           = (6,"ounce",35.2739,"oz")
    CARAT           = (7,"carat",5000,"cts")


'''
{'kilogram' : 1, 'gram' : 1000, 'miligram': 1000000,
                           'metric ton': 0.001, 'long ton': 0.0009842,
                           'short ton' : 0.0011, 'pound' : 2.2046,
                           'ounce' : 35.2739, 'carat' : 5000}
 '''       

'''
{'meter': 1, 'kilometer' : 1000, 
                           'centimeter' : 0.01, 'milimeter' : 0.001,
                           'micrometer' : 0.000001, 'nanometer' : 0.0000000001,
                           'mile' : 1609.35, 'yard' : 0.9144, 'foot' : 0.3048,
                           'inch' : 0.0254}
'''