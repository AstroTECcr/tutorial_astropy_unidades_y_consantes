from astropy import units as u
from astropy.units import imperial
from astropy import constants as c

# crear una cantidad
cantidad = 42.0 * u.meter 
print(cantidad)

# se puede imprimir su valor y su unidad por separado
print(cantidad.value)
print(cantidad.unit)

# aritmética
velocidad = 15.1 * u.meter / (32.0 * u.second)
print(velocidad)

# unidades compuestas
x = 3.0 * u.kilometer / (130.51 * u.meter / u.second)
fuerza = 1 * u.Newton
print(x)
print(fuerza)

# se pueden descomponer unidades a su forma más básica
print(x.decompose())
print(fuerza.decompose())

# conversiones
distancia_en_parsecs = 1.0 * u.parsec
print(distancia_en_parsecs)

distancia_en_km = distancia_en_parsecs.to(u.km)
print(distancia_en_km)

# unidades imperiales y creación de unidades nuevas
cms = u.cm / u.s
mph = imperial.mile / u.hour
print(cms)
print(mph)

# conversiones con unidades creadas
centimetros_por_segundo = 42.0 * cms
millas_por_hora = centimetros_por_segundo.to(mph)
print(centimetros_por_segundo)
print(millas_por_hora)

# unidad adimensional
adimensional = u.m / u.m
print(adimensional)

# igual que se puede descomponer a unidades básicas, se puede componer a unidades compuestas
compuesta = (u.s ** -1).compose()
print(compuesta)

# pasar de sistema de unidades a otro
presion_en_cgs = (1.0 * u.Pa).cgs
print(presion_en_cgs)

# unidades logarítmicas
magnitud = -2.5 * u.mag(u.ct / u.s)

# constantes
print(c.c)
print(c.alpha)

# equivalencias
equivalencia = (1000 * u.nm).to(u.Hz, equivalencies=u.spectral()) 
print(equivalencia)

# impresión "bonita"
cantidad_con_muchos_decimales = 15.1 * u.meter / (32.0 * u.second)
print(cantidad_con_muchos_decimales)
print(f"{cantidad_con_muchos_decimales.value:0.03f}")
print(f"{cantidad_con_muchos_decimales.value:0.04f}")
print(f"{cantidad_con_muchos_decimales.value:0.03f}", f"{cantidad_con_muchos_decimales.unit:FITS}")