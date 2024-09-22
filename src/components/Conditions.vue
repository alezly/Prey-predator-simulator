<template>
  <b-container class="timer-container h-100">
    <h5 class="text-center">Condiciones iniciales</h5>
    <div v-if="type == 'lotka'" style="width: 60%; margin: 0 auto">
      <div>
        <label for="sb-inline" style="width: 100%">Conejos Iniciales</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.lotka.InitialPrays"
        ></b-form-input>
      </div>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Zorros Iniciales</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.lotka.InitialPredator"
        ></b-form-input>
      </div>
      <b-row style="width: 100%">
        <b-col>
          <div class="condition mt-4">
            <label for="range-2">α (alfa)</label>
            <b-form-input
              id="alpha"
              v-model="data.lotka.alpha"
              type="range"
              min="0.01"
              max="0.2"
              step="0.01"
            ></b-form-input>
          </div>
          <div class="mt-4 condition">
            <label for="range-2">β (beta)</label>
            <b-form-input
              id="beta"
              v-model="data.lotka.beta"
              type="range"
              min="0.001"
              max="0.01"
              step="0.001"
            ></b-form-input>
          </div>
        </b-col>
        <b-col>
          <div class="condition mt-4">
            <label for="range-2">γ (gamma)</label>
            <b-form-input
              id="gamma"
              v-model="data.lotka.gamma"
              type="range"
              min="0.01"
              max="0.1"
              step="0.01"
            ></b-form-input>
          </div>
          <div class="mt-4 condition">
            <label for="range-2">δ (delta)</label>
            <b-form-input
              id="delta"
              v-model="data.lotka.delta"
              type="range"
              min="0.00001"
              max="0.0001"
              step="0.00001"
            ></b-form-input>
          </div>
        </b-col>
      </b-row>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Tiempo</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.lotka.time"
        ></b-form-input>
      </div>
    </div>
    <!-- End Lotka -->
    <div v-if="type == 'mds'" style="width: 60%; margin: 0 auto;">
        <div class="mt-4">
          <label for="sb-inline" style="width: 100%">Masa (población de presas)</label>
          <b-form-input
            id="type-number"
            type="number"
            v-model="data.mds.masa"
          ></b-form-input>
        </div>
        <div class="mt-4">
          <label for="sb-inline" style="width: 100%">Constante del resorte (población de depredadores)</label>
          <b-form-input
            id="type-number"
            type="number"
            v-model="data.mds.resorte"
          ></b-form-input>
        </div>
        <b-row style="width: 100%">
          <b-col>
            <div class="condition mt-4">
              <label for="range-2">Coeficiente de amortiguamiento (interacción)</label>
              <b-form-input
                id="alpha"
                v-model="data.mds.amortiguador"
                type="range"
                min="0.1"
                max="0.9"
                step="0.1"
              ></b-form-input>
            </div>
          </b-col>
        </b-row>
        <div class="mt-4">
          <label for="sb-inline" style="width: 100%">Tiempo</label>
          <b-form-input
            id="type-number"
            type="number"
            v-model="data.mds.time"
          ></b-form-input>
        </div>
    </div>
    <!-- End mds -->
    <div v-if="type == 'colas'" style="width: 60%; margin: 0 auto">
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Presas Iniciales</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.colas.InitialPrays"
        ></b-form-input>
      </div>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Depredadores Alfas</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.colas.InitialAlphaPredator"
        ></b-form-input>
      </div>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Otros Depredadores</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.colas.InitialPredator"
        ></b-form-input>
      </div>
      <b-row style="width: 100%">
        <b-col>
          <div class="condition mt-4">
            <label for="range-2">α (alfa)</label>
            <b-form-input
              id="alpha"
              v-model="data.colas.alpha"
              type="range"
              min="0.1"
              max="2.0"
              step="0.1"
            ></b-form-input>
          </div>
          <div class="mt-4 condition">
            <label for="range-2">β (beta)</label>
            <b-form-input
              id="beta"
              v-model="data.colas.beta"
              type="range"
              min="0.01"
              max="0.2"
              step="0.01"
            ></b-form-input>
          </div>
        </b-col>
        <b-col>
          <div class="condition mt-4">
            <label for="range-2">γ (gamma)</label>
            <b-form-input
              id="gamma"
              v-model="data.colas.gamma"
              type="range"
              min="0.0"
              max="2.5"
              step="0.1"
            ></b-form-input>
          </div>
          <div class="mt-4 condition">
            <label for="range-2">δ (delta)</label>
            <b-form-input
              id="delta"
              v-model="data.colas.delta"
              type="range"
              min="0.01"
              max="0.95"
              step="0.01"
            ></b-form-input>
          </div>
        </b-col>
      </b-row>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Tiempo</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.colas.time"
        ></b-form-input>
      </div>
    </div>
    <!-- Colas end -->
    <div v-if="type == 'reloj'" style="width: 60%; margin: 0 auto">
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Conejos Iniciales</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.reloj.InitialPrays"
        ></b-form-input>
      </div>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Zorros Iniciales</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.reloj.InitialPredator"
        ></b-form-input>
      </div>
      <b-row style="width: 100%">
        <b-col>
          <div class="condition mt-4">
            <label for="range-2">α (alfa)</label>
            <b-form-input
              id="alpha"
              v-model="data.reloj.alpha"
              type="range"
              min="0.01"
              max="0.2"
              step="0.01"
            ></b-form-input>
          </div>
          <div class="mt-4 condition">
            <label for="range-2">β (beta)</label>
            <b-form-input
              id="beta"
              v-model="data.reloj.beta"
              type="range"
              min="0.001"
              max="0.01"
              step="0.001"
            ></b-form-input>
          </div>
        </b-col>
        <b-col>
          <div class="condition mt-4">
            <label for="range-2">γ (gamma)</label>
            <b-form-input
              id="gamma"
              v-model="data.reloj.gamma"
              type="range"
              min="0.01"
              max="0.1"
              step="0.01"
            ></b-form-input>
          </div>
          <div class="mt-4 condition">
            <label for="range-2">δ (delta)</label>
            <b-form-input
              id="delta"
              v-model="data.reloj.delta"
              type="range"
              min="0.00001"
              max="0.0001"
              step="0.00001"
            ></b-form-input>
          </div>
        </b-col>
      </b-row>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Tiempo</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.reloj.time"
        ></b-form-input>
      </div>
    </div>
    <!-- End Reloj -->
    <div v-if="type == 'montecarlo'" style="width: 60%; margin: 0 auto">
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Presas Iniciales</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.mcarlos.InitialPrays"
        ></b-form-input>
      </div>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Depredadores Iniciales</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.mcarlos.InitialPredator"
        ></b-form-input>
      </div>
      <b-row style="width: 100%">
        <b-col>
          <div class="condition mt-4">
            <label for="range-2">α (alfa)</label>
            <b-form-input
              id="alpha"
              v-model="data.mcarlos.alpha"
              type="range"
              min="0.05"
              max="0.2"
              step="0.05"
            ></b-form-input>
          </div>
          <div class="mt-4 condition">
            <label for="range-2">β (beta)</label>
            <b-form-input
              id="beta"
              v-model="data.mcarlos.beta"
              type="range"
              min="0.01"
              max="0.05"
              step="0.01"
            ></b-form-input>
          </div>
        </b-col>
        <b-col>
          <div class="condition mt-4">
            <label for="range-2">γ (gamma)</label>
            <b-form-input
              id="gamma"
              v-model="data.mcarlos.gamma"
              type="range"
              min="0.05"
              max="0.2"
              step="0.05"
            ></b-form-input>
          </div>
          <div class="mt-4 condition">
            <label for="range-2">δ (delta)</label>
            <b-form-input
              id="delta"
              v-model="data.mcarlos.delta"
              type="range"
              min="0.001"
              max="0.05"
              step="0.001"
            ></b-form-input>
          </div>
        </b-col>
      </b-row>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Tiempo</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.mcarlos.time"
        ></b-form-input>
      </div>
      <div class="mt-4">
        <label for="sb-inline" style="width: 100%">Pasos de tiempo</label>
        <b-form-input
          id="type-number"
          type="number"
          v-model="data.mcarlos.time_steps"
        ></b-form-input>
      </div>
    </div>
    <!-- End Monte carlos -->
    <div class="d-flex justify-content-center">
      <b-button variant="primary" @click="setConditions">Modelar</b-button>
    </div>
  </b-container>
</template>

<script>
export default {
  name: "InitialConditions",
  data() {
    return {
      data: {},
      virtualClock: false,
    };
  },
  props: {
    type: {
      type: String,
      required: true,
    },
    conditions: {
      type: Object,
      required: true,
    }
  },
  methods: {
    setConditions() {
      this.$emit("refresh");
    },
  },
  created() {
    this.data = this.conditions;
  },
};
</script>

<style scoped>
.timer-container {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
.condition {
  display: flex;
  justify-content: space-between;
  padding: 0 0.4rem;
}
</style>
