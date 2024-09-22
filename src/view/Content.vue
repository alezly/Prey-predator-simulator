<template>
  <div class="row container-fluid h-100 p-0 m-0">
    <div class="col-12 col-sm-12 col-md-12 col-lg-5 h-100 border p-0">
      <div class="simulation-container">
        <!-- Selected form -->
        <b-form-select
          v-model="selected"
          :options="options"
          style="position: absolute; top: 1rem; left: 1rem"
          @change="changeAlgoritmo"
        ></b-form-select>
        <!-- End form -->
        <div class="conditions-container">
          <InitialConditions
            :type="selected"
            :conditions="conditions"
            @refresh="handleConditions"
          />
        </div>
      </div>
    </div>
    <div class="right col-12 col-sm-12 col-md-12 col-lg-7 h-100 p-0">
      <div
        :style="{
          height: selected == 'mds' || selected == 'reloj' ? '50%' : '100%',
        }"
      >
        <LinearChart
          v-show="viewChart"
          ref="firstChart"
          :conditions="conditions"
          :algorithm="selected"
          :idx="1"
        />
      </div>
      <div
        :style="{
          height: selected == 'mds' || selected == 'reloj' ? '50%' : '0',
        }"
      >
        <b-table
          v-if="selected == 'reloj'"
          v-show="viewChart"
          hover
          sticky-header
          :items="items"
        ></b-table>
        <LinearChart
          v-show="viewChart"
          ref="secondChart"
          :conditions="conditions"
          :algorithm="selected"
          :idx="2"
        />
      </div>
    </div>
  </div>
</template>

<script>
import InitialConditions from "../components/Conditions.vue";
import LinearChart from "../components/Chart.vue";
import axios from "axios";

export default {
  name: "SimulationContent",
  components: {
    InitialConditions,
    LinearChart,
  },
  data() {
    return {
      selected: "lotka",
      viewChart: false,
      options: [
        { value: "lotka", text: "Modelo Matemático" },
        { value: "mds", text: "Analogía" },
        { value: "colas", text: "Modelo de Colas" },
        { value: "montecarlo", text: "Monte Carlos" },
        { value: "reloj", text: "Reloj Virtual" },
      ],
      items: [],
      conditions: {
        lotka: {
          alpha: 0.1,
          beta: 0.005,
          gamma: 0.04,
          delta: 0.00004,
          InitialPrays: 200,
          InitialPredator: 10,
          time: 250,
        },
        mds: {
          masa: 200,
          resorte: 200,
          amortiguador: 0.5,
          time: 100,
        },
        colas: {
          alpha: 1.0,
          beta: 0.1,
          gamma: 1.5,
          delta: 0.75,
          InitialPrays: 40,
          InitialPredator: 5,
          InitialAlphaPredator: 9,
          time: 15,
        },
        mcarlos: {
          alpha: 0.1,
          beta: 0.02,
          gamma: 0.1,
          delta: 0.01,
          InitialPrays: 100,
          InitialPredator: 20,
          time: 1000,
          time_steps: 100,
        },
        reloj: {
          alpha: 0.1,
          beta: 0.005,
          gamma: 0.04,
          delta: 0.00004,
          InitialPrays: 200,
          InitialPredator: 10,
          time: 250,
        },
      },
      eventos: [],
    };
  },
  methods: {
    handleConditions() {
      this.$refs.firstChart.init();
      this.$refs.secondChart.init();
      this.viewChart = true;
      if (this.selected == "reloj") {
        axios
          .get(
            `/reloj/?alpha=${+this.conditions.reloj.alpha}&beta=${+this
              .conditions.reloj.beta}&gamma=${+this.conditions.reloj
              .gamma}&delta=${+this.conditions.reloj.delta}&time=${+this
              .conditions.reloj.time}&x=${+this.conditions.reloj
              .InitialPrays}&y=${+this.conditions.reloj.InitialPredator}`
          )
          .then((response) => {
            this.items = response.data
          });
      }
    },
    changeAlgoritmo() {
      this.viewChart = false;
    },
  },
};
</script>
<style scoped>
.simulation-container {
  height: 100%;
  position: relative;
}
.conditions-container {
  height: 100%;
}
.b-table-sticky-header {
    overflow-y: auto;
    max-height: 100%;
}
</style>
