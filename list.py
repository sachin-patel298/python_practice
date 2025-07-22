Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
game_varities = ["BGMI" , "FF", "Extreme Car" , "COD"]
print(game_varities)
['BGMI', 'FF', 'Extreme Car', 'COD']
print(game_varities[1])
FF
print(game_varities[-1])
COD
print(game_varities[1:2])
['FF']
print(game_varities[1:3])
['FF', 'Extreme Car']
game_varities[3:4] = ["GTA V5","Ashphalt"]
print(game_varities)
['BGMI', 'FF', 'Extreme Car', 'GTA V5', 'Ashphalt']
 for game in game_varities:
     
SyntaxError: unexpected indent
for game in game_varities:
     print(game)

     
BGMI
FF
Extreme Car
GTA V5
Ashphalt

if "BGMI" in game_varities :
    print("BGMI Available")
    else :
        
SyntaxError: invalid syntax
if "BGMI" in game_varities :
    print("BGMI Available")else :
        
SyntaxError: invalid syntax
game_varities.append("Minecraft")
if "BGMI" in game_varities :
    print("BGMI Available")
else :
...     print("BGMI Not Available")
... 
...     
BGMI Available
>>> game_varities.pop()
'Minecraft'
>>> game_varities
['BGMI', 'FF', 'Extreme Car', 'GTA V5', 'Ashphalt']
>>> game_varities.remove("Extreme Car")
>>> game_varities
['BGMI', 'FF', 'GTA V5', 'Ashphalt']
>>> game_varities.insert(2,"Minecraft")
>>> game_varities
['BGMI', 'FF', 'Minecraft', 'GTA V5', 'Ashphalt']
>>> game_varities_copy = game_varities.copy()
>>> game_varities_copy
['BGMI', 'FF', 'Minecraft', 'GTA V5', 'Ashphalt']
>>> game_varities.append("Icecream")
>>> print(game_varities)
['BGMI', 'FF', 'Minecraft', 'GTA V5', 'Ashphalt', 'Icecream']
>>> game_varities.remove("Icecream")
>>> game_varities
['BGMI', 'FF', 'Minecraft', 'GTA V5', 'Ashphalt']
>>> square_num = [x**3 for x in range(10)]
>>> square_num
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> square_num = [y**3 for y in range(11)]
>>> square_num
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> square_num = [x**2 for x in range(11)]
>>> square_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> cube_num = [y**3 for y in range(11)]
>>> cube_num
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> 
