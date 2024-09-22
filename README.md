# Simulación de Crecimiento de Presas y Depredadores
Este repositorio contiene una aplicación que simula el crecimiento de presas y depredadores utilizando el modelo Lotka-Volterra. La aplicación está construida con Vue.js 2 para el frontend y FastAPI para el backend.

# Descripción del Proyecto
La simulación utiliza el modelo Lotka-Volterra para representar las interacciones entre dos especies: presas y depredadores. La interfaz de usuario permite visualizar los resultados de la simulación utilizando Highcharts.

# Instalación

## Instala las dependencias del frontend:
```
npm install
```

### Instala las dependencias del backend:
```
cd api
pip install -r requirements.txt
```
## Ejecución del Proyecto

### Inicia el servidor del frontend:
```
npm run dev
```

### Inicia el servidor de FastAPI:
```
cd api
npm run server
```
## Visualización de Resultados

Una vez que ambos servidores estén en funcionamiento, podrás acceder a la interfaz del frontend en tu navegador. Los resultados de la simulación se visualizarán utilizando Highcharts, permitiéndote observar la dinámica de las poblaciones de presas y depredadores en tiempo real.
