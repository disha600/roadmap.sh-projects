from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def length():
    return render_template("length.html")

@app.route("/weight")
def weight():
    return render_template("weight.html")

@app.route("/temp")
def temp():
    return render_template("temp.html")

@app.route("/result" ,methods=["POST","GET"])
def result():
    if request.method=="POST":
        try:
            value=float(request.form.get("value"))
            unit_from=request.form.get("convert_from")
            unit_to=request.form.get("convert_to")

            if(unit_from in ('mm','cm','m','km','foot','yard','mile','inch','mg','g','kg','ounce','pound')):
                answer=convert(value,unit_from,unit_to)
            
            else:
                answer=convert_temp(value,unit_from,unit_to)

            return render_template("result.html",answer=answer)
        except(ValueError):
            return(render_template("result.html",error="ERROR: Invalid Input Given!!!"))



#base unit logic
base_unit={
    "mm":0.001,
    "cm":0.01,
    "m":1,
    "km":1000,
    "inch":0.0254,
    "foot":0.3048 ,
    "yard":0.9144,
    "mile":1609.344,
    "mg":0.000001,
    "g":0.001,
    "kg":1,
    "ounce":0.0283495231,
    "pound":0.45359237,
}

#function for unit conversion (length,weight)
def convert(value,unit_from,unit_to):

    #convert to base unit(m)
    base_value=value*base_unit[unit_from]

    return (base_value/base_unit[unit_to])


#function for temperature conversion
def convert_temp(value_temp,unit_from,unit_to):
    if(unit_from=='kelvin'):
        if(unit_from==unit_to):
            return value_temp
        elif(unit_to=='celsius'):
            return(value_temp-273.15)
        else:
            return((value_temp-273.15)*9/5+32)
        
    elif(unit_from=='celsius'):
        if(unit_from==unit_to):
            return value_temp
        elif(unit_to=='kelvin'):
            return(value_temp+273.15)
        else:
            return(value_temp*9/5+32)
    
    else:
        if(unit_from==unit_to):
            return value_temp
        elif(unit_to=='kelvin'):
            return((value_temp-32)*5/9+273.15)
        else:
            return((value_temp-32)*5/9)




app.run(debug=True)