def view_bmi(weight, height):
    bmi = (weight * 703)/(height*height)
    bmi = round(bmi, 1)
    return bmi
