from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from scipy.integrate import odeint
from pydantic import BaseModel 
import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt 

app  = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.1.133:8080","http://localhost:8080"],  # Origen permitido para las peticiones (puedes usar '*' para permitir cualquier origen)
    # allow_origins=["http://localhost:8080"],  # Origen permitido para las peticiones (puedes usar '*' para permitir cualquier origen)
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos
    allow_headers=["*"],  # Encabezados permitidos
)

class Result(BaseModel):  
    tiempo: float  
    evento: str  
    conejos: int  
    zorros: int  

def convertir_a_entero(decimal):  
    if decimal < 1:  
        numero_str = str(decimal)  
        punto_decimal = numero_str.find('.')  
        if punto_decimal != -1 and punto_decimal + 1 < len(numero_str):  
            return int(numero_str[punto_decimal + 1])  
        return 0  
    else:  
        return int(decimal)  

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get("/lotka_volterra/")
async def basicLotkaVolterra(alpha:float, beta:float, gamma:float, delta: float, time: int, x:int, y:int):
    # alpha tasa de crecimiento de conejos por mes por conejo
    # beta éxito en la caza del depredador por producto presa depredador
    # gamma tasa de crecimiento de zorros por zorro
    # delta éxito en la caza y cuánto alimenta cazar una presa al depredador
    # time tiempo en meses
    def LotkaVolterra(t, v):
        x, y = v
        dxdt = alpha * x - beta * x * y
        dydt = delta * x * y - gamma * y
        return dxdt, dydt 
    
    x0 = x  # conejos inicialmente
    y0 = y    # zorros inicialmente
    v0 = x0, y0

    tspan = (0, time)
    t = np.linspace(*tspan, 2000)

    r = integ.solve_ivp(LotkaVolterra, tspan, v0, t_eval=t)
    x, y = r.y

    # Formatear los datos para Highcharts
    data = {
        "time": t.tolist(),
        "rabbits": x.tolist(),
        "foxes": y.tolist()
    }
    
    return JSONResponse(content=data)

@app.get("/analogia/")
async def basicMDS(masa:float, resorte:float, amortiguador:float, time: int):
    # Parámetros del sistema
    m = masa  # Masa (población de presas)
    k = resorte    # Constante del resorte (población de depredadores)
    b = amortiguador   # Coeficiente de amortiguamiento (interacción)

    # Condiciones iniciales
    x0 = 1    # Posición inicial
    v0 = 0    # Velocidad inicial 
    y0 = [x0, v0]

    # Tiempo de simulación
    t_start = 0
    t_end = time
    t = np.linspace(t_start, t_end, 1000)

    # Definición de las ecuaciones
    def mass_spring_damper(y, t, m, k, b):
        x, v = y
        dx_dt = v
        dv_dt = -(b/m) * v - (k/m) * x
        return np.array([dx_dt, dv_dt])

    # Resolver el sistema de ecuaciones diferenciales
    sol = odeint(mass_spring_damper, y0, t, args=(m, k, b))

    data = {
        "tiempo": t.tolist(),
        "posicion": sol[:, 0].tolist(),
        "velocidad": sol[:, 1].tolist()
    }
    
    return JSONResponse(content=data)

@app.get("/colas/")
async def colas(alpha:float, beta:float, gamma:float, delta: float, time: int, x:int, y:int, z:int):
    # Parámetros
    alpha = alpha
    beta = beta
    gamma = gamma
    delta = delta

    # Sistema de ecuaciones
    def sistema(y, t):
        C, L_a, L_n = y
        dC = alpha*C - beta*(L_a/(L_a + L_n))*L_a*C
        dL_a = delta*beta*(L_a/(L_a + L_n))*L_a*C - gamma*L_a
        dL_n = delta*beta*(L_a/(L_a + L_n))*L_n*C - gamma*L_n
        return [dC, dL_a, dL_n]

    # Condiciones iniciales
    C0 = x
    L_a0 = z
    L_n0 = y
    y0 = [C0, L_a0, L_n0]

    # Tiempo
    t = np.linspace(0, time, 1000)

    # Resolver el sistema de ecuaciones
    sol = odeint(sistema, y0, t)

    data = {
        "tiempo": t.tolist(),
        "presas": sol[:, 0].tolist(),
        "depredadores_alfa": sol[:, 1].tolist(),
        "otros_depredadores": sol[:, 2].tolist()
    }

    return JSONResponse(content=data)

@app.get("/reloj", response_model=list[Result])  
def virtualClock(alpha:float, beta:float, gamma:float, delta: float, time: int, x:int, y:int):  

    def LotkaVolterra(t, v):
        x, y = v
        dxdt = alpha * x - beta * x * y
        dydt = delta * x * y - gamma * y
        return dxdt, dydt 
    
    x0 = x  
    y0 = y  
    v0 = x0, y0  
    tspan = (0, time)  
    t = np.linspace(*tspan, 2000)  

    r = integ.solve_ivp(LotkaVolterra, tspan, v0, t_eval=t)  

    x = np.array([convertir_a_entero(val) for val in r.y[0]])  
    y = np.array([convertir_a_entero(val) for val in r.y[1]])  

    # Reloj virtual y lista de eventos
    eventos = []

    for i in range(len(t)):
        if x[i] > 0 and y[i] < 20 and y[i] > 0:  # Regla 1: Aumento de Presas con Pocos Depredadores
            eventos.append((t[i], "Aumento de Presas", x[i], y[i]))
        elif x[i] < 500 and y[i] > 15 and x[i] > 0:  # Regla 2: Disminución de Presas con Muchos Depredadores
            eventos.append((t[i], "Disminución de Presas", x[i], y[i]))
        elif y[i] > 0 and x[i] < 100 and x[i] > 0:  # Regla 3: Disminución de Depredadores con Pocas Presas
            eventos.append((t[i], "Disminución de Depredadores", x[i], y[i]))
        elif y[i] < 20 and x[i] > 1000 and y[i] > 0:  # Regla 4: Aumento de predadores con muchas presas
            eventos.append((t[i], "Aumento de Depredadores", x[i], y[i]))
        elif y[i] > 0 and x[i] == 0:  # Regla 5: Extinción de Depredadores sin Presas
            eventos.append((t[i], "Extinción de Depredadores", x[i], y[i]))
        elif x[i] > 0 and y[i] == 0:  # Regla 6: Crecimiento Exponencial de Presas sin Depredadores
            eventos.append((t[i], "Crecimiento Exponencial de Presas", x[i], y[i]))

    # Filtrar el tiempo y las poblaciones donde hay cambios
    tiempos_cambios = []
    conejos_cambios = []
    zorros_cambios = []
    eventos_filtrados = []
    eventos_array = []

    for i in range(1, len(t)):
        if x[i] != x[i-1] or y[i] != y[i-1]:  # Si hay un cambio
            tiempos_cambios.append(t[i])
            conejos_cambios.append(x[i])
            zorros_cambios.append(y[i])
            # Filtrar eventos que coincidan con tiempos_cambios
            for evento in eventos:
                if abs(evento[0] - t[i]) < 1e-5:  # Comparar tiempos con una tolerancia
                    eventos_filtrados.append(evento)

    for evento in eventos_filtrados:
        eventos_array.append({
            "tiempo": round(evento[0], 2),  # Redondear el tiempo a 2 decimales
            "evento": evento[1],
            "conejos": evento[2],
            "zorros": evento[3]
        })

    return eventos_array 

@app.get("/montecarlos/")
async def monteCarlos(alpha:float, beta:float, gamma:float, delta: float, time: int, timesteps: int, x:int, y:int):
    # Cantidad de simulaciones y condiciones iniciales  
    simulations = time  
    time_steps = timesteps  
    dt = 0.1  

    # Arrays para almacenar resultados  
    final_presas = []  
    final_depredadores = []  

    # Simulación  
    for _ in range(simulations):  
        # Condiciones iniciales aleatorias  
        X0 = np.random.uniform(0, x)  # Población inicial de presas  
        Y0 = np.random.uniform(0, y)  # Población inicial de depredadores  
        
        # Inicializar la población  
        X = X0  
        Y = Y0  

        # Simular el comportamiento a lo largo del tiempo  
        for t in np.arange(0, time_steps, dt):  
            dX = (alpha * X - beta * X * Y) * dt  
            dY = (delta * X * Y - gamma * Y) * dt  
            X += dX  
            Y += dY  
        
        # Guardar resultados finales  
        final_presas.append(X)  
        final_depredadores.append(Y)  

    # Calcular medias de las poblaciones finales  
    mean_presas = np.mean(final_presas)  
    mean_depredadores = np.mean(final_depredadores)  

    return {  
        "mean_presas": mean_presas,  
        "mean_depredadores": mean_depredadores  
    }  

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)