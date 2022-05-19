<template>
  <div class="results">
      <table class="table table-striped">
      <thead>
        <tr>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Distance</th>
          <th>City Name</th>
          <th>When</th>
          <th>Earthquake</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in results" :key="index">
           <th scope="row">{{ item.start_date  }}</th>
           <td>{{ item.end_date }}</td>
           <td>{{ item.distance }}</td>
           <td>{{ item.city.name }}</td>
           <td>{{ item.date }}</td>
           <td>{{ item.earthquake }}</td>
        </tr>
       </tbody>
    </table>

  </div>
</template>
<script lang="ts">
import {defineComponent} from 'vue';
//@ts-ignore
import api from '@/services/api.js'

export default defineComponent({
  name: 'ResultsView',
  data() {
    return {
      results: [],
    };
  },
  methods: {
     getAllResults() {
       console.log('ssss')
        api
          .get('/results', {
            params: {
              page_size: -1
            }
          })
          .then((response: { data: any; }) => response.data)
          .then((items: { results: never[]; }) => {
              this.results = items.results
          })
     }
  },
  created() {
    this.getAllResults()
  },
  setup() {

  }
});
</script>
<style lang="scss">
.results {
  margin-left: 20%;
}
</style>
