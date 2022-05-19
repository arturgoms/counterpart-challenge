<template>
  <div class="home">
    <EarthquakeSearch :cities="items"/>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import EarthquakeSearch from '@/components/EarthquakeSearch.vue';
//@ts-ignore
import api from '@/services/api.js'

export default defineComponent({
  name: 'HomeView',
  components: {
    EarthquakeSearch,
  },
  data() {
    return {
      items: [],
    };
  },
  methods: {
     getAllCities() {
      api
          .get('/cities', { cache: true })
          .then((response: { data: any; }) => response.data)
          .then((items: { results: never[]; }) => {
              this.items = items.results
          })
     }
  },
  created() {
    this.getAllCities()
  }
});
</script>
<style lang="scss">
.home {
  width: 50%;
  padding: 24px;
  margin-left: 20%;
}
</style>