

#                                """FALLING THROUGH THE RABBIT HOLE"""

# This is Stanford's Code in Place's final project written by Hendrik Hansen.
# Program is inspired by Lewis Carrol's Alice in Wonderland. If Alice falls through the Earth or another space object,
# how long will it take her to get to the other side? What is her maximum speed in this process? These calculations
# presume that the rabbit hole is the diameter of the planet and goes directly through the core.
# HAVE FUN!


#                                              ***



# THE UNIVERSAL GRAVITATIONAL CONSTANT("Big G")
# UNIT : m**3*kg**−1*s**−2
G =  6.67408*10**-11
ALICE_MASS = 45

import math
import os
import pandas as pd
#import qrcode


space_objects = ["jupiter", "venus", "pluto", "mercury", "mars", "earth", "moon", "sun", "neptune", "saturn", "titan"]

# creating dictionaries for space objects

jupiter = {"mass" : 1.898 * 10**27,
        "radius": 69911000,
        "gravitational_constant": 24.79,
        "density":1.33
         }

venus = {"mass" : 4.867 * 10**24,
        "radius":6051800,
        "gravitational_constant": 8.87,
        "density":5.24
         }

pluto = {"mass" : 1.309 * 10**22,
        "radius":1.1883 * 10**6,
        "gravitational_constant": 0.62,
        "density":1.88
         }

mercury = {"mass" : 3.285 * 10**23,
        "radius":2.4397 * 10**6,
        "gravitational_constant": 3.7,
        "density":5.43
         }

mars = {"mass" : 6.39 * 10**23,
        "radius":3.3895 * 10**6,
        "gravitational_constant": 3.721,
        "density":3.93
         }

earth = {"mass" : 5.9722 * 10**24 ,
        "radius":6371000,
        "gravitational_constant": 9.807,
        "density":5.51
         }

moon = {"mass" : 7.34767309 * 10**22,
        "radius":1.7371 * 10**6,
        "gravitational_constant": 1.62,
        "density":3.34
         }
sun = {"mass" : 1.989 * 10**30  ,
        "radius":696.34 * 10**6,
        "gravitational_constant": 274,
        "density":1.41
         }
neptune = {"mass" : 1.024 * 10**26  ,
        "radius":24.622 * 10**6,
        "gravitational_constant": 11.15,
        "density":1.64
         }
saturn = {"mass" : 5.683 * 10**26  ,
        "radius":58.232 * 10**6,
        "gravitational_constant": 10.44,
        "density":0.687
         }
titan = {"mass" : 1.024 * 10**26  ,
        "radius":2.5747 * 10**6,
        "gravitational_constant": 1.352,
        "density":1.88
         }


# Creating dictionaries for space objects' and particles' parameters,
# values in this dictionary are themselves dictionaries

parameters = { "mars": mars,
               "earth": earth,
               "moon": moon,
               "sun":sun,
               "jupiter": jupiter,
               "neptune":neptune,
               "pluto": pluto,
               "titan": titan,
               "saturn":saturn,
               "venus": venus,
               "mercury":mercury,
}

# creating dictionary for units
units = {"mass": "kg",
         "radius": "meters",
         "gravitational_constant": "N(m/kg)**2",
         "falling_time": "minutes"
         }


def period_of_oscillation(planet):
    # Calculates the time Alice's round-trip through the tunnel through planet using the formula
    # 2pi*sqrt(radius of planet/gravitational_constant)
    # to know the time for Alice to fall through the planet or particle, we need to divide the period by 2.
    # period unit will be in seconds, we will convert that to minutes
    # then we will round the number
    radius = planetdata(planet, "radius", "radius")
    gravitational_constant = planetdata(planet, "gravitational_constant", "gravitational_constant")
    time = 2*math.pi*math.sqrt(radius/gravitational_constant)
    # that's the round-trip time but we only need the time for a one way trip, so we divide by 2
    time = time/2
    # now converting time to minutes
    time = time/60
    # round the number
    time = round(time, 2)
    print("\nAlice falls through the", planet.capitalize(), "in"  ,time, units["falling_time"])

def time(planet):
    radius = planetdata(planet, "radius", "radius")
    gravitational_constant = planetdata(planet, "gravitational_constant", "gravitational_constant")
    time = 2*math.pi*math.sqrt(radius/gravitational_constant)
    time = time/2
    time = time/60
    time = round(time, 2)
    return time


def planetdata(planetname, parameter, unit):
    planetdata = parameters[planetname]
    data = planetdata[parameter]
    # print(planetname, "has a", parameter,  "of ", data, units[unit])
    return data


def gravitational_constant(planet):
    # calculates the the local gravitational field of the planet\particle(so called "small g") using
    # the formula g = (Big_G(THE UNIVERSAL GRAVITATIONAL CONSTANT) * Mass of planet/particle)
    small_g = (G*planetdata(planet, "mass", "mass"))/((planetdata(planet, "radius", "radius"))**2)
    small_g = round(small_g, 3)
    return small_g


def alice_weight(planet):
    # calculate how much Alice weighs on different planets = (weight on earth / 9,81 m/s**2)*planet's gravity
    # weigh_on_planet = ((45)/9,81)*(planet's gravity)
    # return weigh_on_planet

    planetgravity = planetdata(planet, "gravitational_constant", "gravitational_constant")
    alice_weight_on_planet = ((45/9.807)*(planetgravity))
    alice_weight_on_planet = round(alice_weight_on_planet, 2)
    return alice_weight_on_planet


def angular_frequency(planetname):
    # Calculates angular frequency to calculate Alice's maximum speed
    planetdata = parameters[planetname]
    density = planetdata["density"]*10**3
    planetdata = parameters[planetname]
    radius = planetdata["radius"]
    #print(density)
    #print(radius)
    ang = math.sqrt((4*math.pi*G*density)/3)
    #print(ang)
    return ang


def max_speed(planetname):
    # Calculates Alice's maximum speed
    ang = angular_frequency(planetname)
    planetdata = parameters[planetname]
    radius = planetdata["radius"]
    maxspeed = ang*radius*10**-3
    maxspeed = round(maxspeed,2)
    #print(maxspeed)
    return maxspeed

def main():

    print("This is Stanford's Code in Place's final project written by Hendrik Hansen."
          " \nProgram is inspired by Lewis Carrol's Alice in Wonderland. \nIf Alice falls through the Earth "
          "or another space object,"
      " \nhow long will it take her to get to the other side? \nWhat is her maximum speed in this process")


    # Printing out space objects 

    print("\nSpace objects:  ", end="")
    for i in range(len(space_objects)-1):
        print(space_objects[i].capitalize(), end=", ")
    print(space_objects[-1].capitalize()+".")



    get_planet_name = input(
            "\nChoose a space object from the list above to calculate Alice's weight on a planet or a star"
            "(Try the Sun): ").lower()
    if get_planet_name in space_objects:

        print("\n\nOn Earth Alice weighs 45 kg.")
    else:
        while get_planet_name not in space_objects:
            print("Your entered object is not in list. Please choose an object from the list above.")
            get_planet_name = input(
                "\nChoose a space object from the list above to calculate Alice's weight on a planet or a star"
                "(Try the Sun): ").lower()


    alice_weight_on_planet = alice_weight(get_planet_name)
    if alice_weight_on_planet == 45:
         pass
    else:
          print("\nOn", get_planet_name.capitalize(), "Alice weighs",alice_weight_on_planet, units["mass"]+".\n")

    if alice_weight_on_planet<45:
          mass = ALICE_MASS / alice_weight_on_planet
          mass = round(mass, 2)
          print(f"That's about {mass}th of Alice's Earth weight. She feels like a fairy!")
    elif alice_weight_on_planet>45:
          mass = alice_weight_on_planet / ALICE_MASS
          mass = round(mass, 2)
          print(f"That's the weight of {mass} Earth Alices! She feels shes made of solid iron - Iron Alice!")
    else:
        pass

    print(f"\nAlice finds a rabbit hole on the {(get_planet_name).capitalize()} and decides to jump in!\n. \nThis turns "
             f"out to be a tunnel to the other side of the {(get_planet_name).capitalize()}. ")

    period_of_oscillation(get_planet_name)
    print(f"\nRight in the middle of the {get_planet_name.capitalize()} her speed is an incredible"
        f" {max_speed(get_planet_name)} km per second.")
    print("\nHere are the values for all space objects:\n")

        # Creating a table with all the values
    data = {}
    spaceob = list(map(lambda x: x.capitalize(), space_objects))
    data["Space object"] = spaceob

    times = []
    for object in space_objects:
        times.append(time(object))
    data["Time min"] = times

    maxspeed = []
    for object in space_objects:
        maxspeed.append(max_speed(object))
    data["Maximum speed km/s"] = maxspeed

    alicew = []
    for object in space_objects:
        alicew.append(alice_weight(object))
    data["Alice's weight kg"] = alicew

    index = []
    for i in range(1, 12):
        index.append(i)

    df = pd.DataFrame(data, index)
    print(df)


# Next lines of code give users the ability to use their phones to view a clip from Youtube from a movie "
# Alice in Wonderland"
'''
        ans = input("\nWould you like to see Alice falling through Earth on your phone(open camera please)?(Type y or n)  ")
        if ans == "y":

            img = qrcode.make("https://www.youtube.com/watch?v=gftRJdhhEVs")
            img.save("qr.png", "PNG")
            os.system("start qr.png
            ")
        else:
            pass
'''


if __name__ == '__main__':
        main()
