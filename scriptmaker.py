import math

with open("script", "w") as fd:

    end = ""
    for i in range(0, 72):
        end += "clear\n"
        end += "sphere\n%f 0 %f 30\n"%(200*math.cos(i*5*math.pi/180), 200*math.sin(i*5*math.pi/180))
        end += "torus\n0 0 0 80 200\n"
        end += "ident\n"
        end += "rotate\n y 20\n"
        end += "rotate\n z 20\n"
        end += "rotate\n x %f\n"%(i*5)
        end += "apply\n"
        end += "sphere\n0 0 0 80\n"
        end += "ident\n"
        end += "move\n 250 250 0\n"
        end += "apply\n"
        if i < 10:
            end += "save\n anim/00%d.png\n"%(i)
        else:
            end += "save\n anim/0%d.png\n"%(i)
    print end
