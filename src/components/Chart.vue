<template>
  <b-container class="h-100">
    <div class="h-100 w-100" :id="`container-chart-${idx}`"></div>
  </b-container>
</template>

<script>
import Highcharts from "highcharts";
import axios from "axios";

export default {
  name: "LinearChart",
  data() {
    return {
      chart: null,
    };
  },
  props: {
    conditions: {
      type: Object,
      required: true,
    },
    algorithm: {
      type: String,
      required: true,
      default: "lotka",
    },
    idx: {
      type: Number,
      required: true,
      default: 1,
    },
  },
  methods: {
    init() {
      if (this.algorithm && this.idx) {
        switch (this.algorithm) {
          case "lotka":
            this.handleLotka(this.idx);
            break;
          case "mds":
            this.handleMDS(this.idx);
            break;
          case "colas":
            this.handleColas(this.idx);
            break;
          case "reloj":
            this.handleReloj(this.idx);
            break;
          case "montecarlo":
            this.handleMonteCarlo(this.idx);
            break;
          default:
            alert("Algoritmo no valido");
        }
      } else {
        this.message = "Por favor selecciona un algoritmo.";
      }
    },
    handleLotka(option) {
      if (option == 1) {
        axios
          .get(
            `/lotka_volterra/?alpha=${+this.conditions.lotka.alpha}&beta=${+this
              .conditions.lotka.beta}&gamma=${+this.conditions.lotka
              .gamma}&delta=${+this.conditions.lotka.delta}&time=${+this
              .conditions.lotka.time}&x=${+this.conditions.lotka
              .InitialPrays}&y=${+this.conditions.lotka.InitialPredator}`
          )
          .then((response) => {
            this.chart = Highcharts.chart(`container-chart-${this.idx}`, {
              title: {
                text: "Modelo de Lotka-Volterra",
              },
              xAxis: {
                title: {
                  text: "Tiempo",
                },
                min: 0,
                max: +this.conditions.lotka.time,
              },
              yAxis: [
                {
                  title: {
                    text: "Conejos",
                  },
                  min: 0,
                },
                {
                  title: {
                    text: "Zorros",
                  },
                  opposite: true,
                  min: 0,
                },
              ],
              series: [
                {
                  name: "Conejos",
                  data: response.data.time.map((month, index) => [
                    month,
                    response.data.rabbits[index],
                  ]), // Empareja mes con conejos
                  yAxis: 0,
                  color: "#37C88F",
                },
                {
                  name: "Zorros",
                  data: response.data.time.map((month, index) => [
                    month,
                    response.data.foxes[index],
                  ]), // Empareja mes con zorros
                  yAxis: 1,
                  color: "#005CC8",
                },
              ],
            });
          });
      }
    },
    handleMDS(option) {
      if (option == 1) {
        axios
          .get(
            `/analogia/?masa=${+this.conditions.mds.masa}&resorte=${+this
              .conditions.mds.resorte}&amortiguador=${+this.conditions.mds
              .amortiguador}&time=${+this.conditions.mds.time}`
          )
          .then((response) => {
            this.chart = Highcharts.chart(`container-chart-${this.idx}`, {
              title: { text: "Posición de la masa (Población de presas)" },
              xAxis: {
                title: { text: "Tiempo (s)" },
                min: 0,
                max: +this.conditions.mds.time,
              },
              yAxis: { title: { text: "Posición (x)" } },
              series: [
                {
                  name: "Posición",
                  data: response.data.tiempo.map((month, index) => [
                    month,
                    response.data.posicion[index],
                  ]),
                  color: "#005CC8",
                },
              ],
            });
          });
      } else {
        axios
          .get(
            `/analogia/?masa=${+this.conditions.mds.masa}&resorte=${+this
              .conditions.mds.resorte}&amortiguador=${+this.conditions.mds
              .amortiguador}&time=${+this.conditions.mds.time}`
          )
          .then((response) => {
            this.chart = Highcharts.chart(`container-chart-${this.idx}`, {
              title: { text: "Velocidad de la masa (Interacción)" },
              xAxis: {
                title: { text: "Tiempo (s)" },
                min: 0,
                max: +this.conditions.mds.time,
              },
              yAxis: { title: { text: "Velocidad (v)" } },
              series: [
                {
                  name: "Velocidad",
                  data: response.data.tiempo.map((month, index) => [
                    month,
                    response.data.velocidad[index],
                  ]),
                  color: "#37C88F",
                },
              ],
            });
          });
      }
    },
    handleColas(option) {
      if (option == 1) {
        axios
          .get(
            `/colas/?alpha=${+this.conditions.colas.alpha}&beta=${+this
              .conditions.colas.beta}&gamma=${+this.conditions.colas
              .gamma}&delta=${+this.conditions.colas.delta}&time=${+this
              .conditions.colas.time}&x=${+this.conditions.colas
              .InitialPrays}&y=${+this.conditions.colas
              .InitialPredator}&z=${+this.conditions.colas
              .InitialAlphaPredator}`
          )
          .then((response) => {
            this.chart = Highcharts.chart(`container-chart-${this.idx}`, {
              title: { text: "Dinámica de Poblaciones" },
              xAxis: {
                title: { text: "Tiempo" },
                min: 0,
                max: +this.conditions.colas.time,
              },
              yAxis: {
                title: { text: "Población" },
              },
              series: [
                {
                  name: "Presas (C)",
                  data: response.data.tiempo.map((month, index) => [
                    month,
                    response.data.presas[index],
                  ]),
                  color: "#37C88F",
                },
                {
                  name: "Depredadores alfa (L_a)",
                  data: response.data.tiempo.map((month, index) => [
                    month,
                    response.data.depredadores_alfa[index],
                  ]),
                  color: "#005CC8",
                },
                {
                  name: "Otros depredadores (L_n)",
                  data: response.data.tiempo.map((month, index) => [
                    month,
                    response.data.otros_depredadores[index],
                  ]),
                  color: "#6B2C87",
                },
              ],
            });
          });
      }
    },
    handleReloj(option) {
      if (option == 1) {
        axios
          .get(
            `/reloj/?alpha=${+this.conditions.reloj.alpha}&beta=${+this
              .conditions.reloj.beta}&gamma=${+this.conditions.reloj
              .gamma}&delta=${+this.conditions.reloj.delta}&time=${+this
              .conditions.reloj.time}&x=${+this.conditions.reloj
              .InitialPrays}&y=${+this.conditions.reloj.InitialPredator}`
          )
          .then((response) => {
            let tiempos = response.data.map((e) => e.tiempo);
            let conejos = response.data.map((e) => e.conejos);
            let zorros = response.data.map((e) => e.zorros);

            this.chart = Highcharts.chart(`container-chart-${this.idx}`, {
              title: {
                text: "Modelo de Lotka-Volterra",
              },
              xAxis: {
                title: {
                  text: "Tiempo",
                },
                min: 0,
                max: +this.conditions.reloj.time,
              },
              yAxis: [
                {
                  title: {
                    text: "Conejos",
                  },
                  min: 0,
                },
                {
                  title: {
                    text: "Zorros",
                  },
                  opposite: true,
                  min: 0,
                },
              ],
              series: [
                {
                  name: "Conejos",
                  data: tiempos.map((month, index) => [month, conejos[index]]), // Empareja mes con conejos
                  yAxis: 0,
                  color: "#37C88F",
                },
                {
                  name: "Zorros",
                  data: tiempos.map((month, index) => [month, zorros[index]]), // Empareja mes con zorros
                  yAxis: 1,
                  color: "#005CC8",
                },
              ],
            });
          });
      }
    },
    handleMonteCarlo(option) {
      if (option == 1) {
        axios
          .get(
            `/montecarlos/?alpha=${+this.conditions.mcarlos.alpha}&beta=${+this
              .conditions.mcarlos.beta}&gamma=${+this.conditions.mcarlos
              .gamma}&delta=${+this.conditions.mcarlos.delta}&time=${+this
              .conditions.mcarlos.time}&timesteps=${+this.conditions.mcarlos
              .time_steps}&x=${+this.conditions.mcarlos.InitialPrays}&y=${+this
              .conditions.mcarlos.InitialPredator}`
          )
          .then((response) => {
            this.chart = Highcharts.chart(`container-chart-${this.idx}`, {
              chart: {
                type: "column",
              },
              title: {
                text: "Población Media de Presas y Depredadores",
              },
              xAxis: {
                categories: [
                  "Población media",
                  "Población media",
                ],
              },
              yAxis: {
                title: {
                  text: "Número de Individuos",
                },
              },
              series: [
                {
                  name: "Presas",
                  data: [response.data.mean_presas],
                  color: "#37C88F",
                },
                {
                  name: "Depredadores",
                  data: [response.data.mean_depredadores],
                  color: "#005CC8",
                },
              ],
            });
          });
      }
    },
  },
};
</script>

<style scoped></style>
