<template>
  <div class="container-fluid p-0 simulation-container">
    <SimulationContent/>
  </div>
</template>

<script>
import SimulationContent from "./view/Content.vue";

export default {
  name: "App",
  components: {
    SimulationContent
  },
};
</script>

<style>
*{
  margin: 0;
  padding: 0;
}
.simulation-container{
  height: 100vh;
  overflow-y: hidden;
}

</style>
