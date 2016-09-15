def view_bmi(weight, height):
    bmi = (weight * 703)/(height*height)
    bmi = round(bmi, 1)
    bmi_dict = {}
    bmi_dict['bmi'] = bmi
    return bmi_dict
