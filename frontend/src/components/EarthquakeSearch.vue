<template>
  <div class="hello">
    <Dropdown
        :options="items"
        :disabled="false"
        v-on:selected="validateSelection"
        name="cities"
        :maxItem="10"
        placeholder="Please select an city"
        >
    </Dropdown>
    <button @click="open">
      Create City
    </button>

    <Datepicker
        v-model="date"
        range multiCalendars
    ></Datepicker>

    <p>
      {{ msg_result }}
    </p>
    <button @click="search">
      Search
    </button>

    <widget-container-modal />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Dropdown from '@/components/Dropdown.vue';
import CreateCity from '@/components/CreateCity.vue';
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
//@ts-ignore
import api from '@/services/api.js'
import {openModal, container} from "jenesius-vue-modal";

export default defineComponent({
  name: 'HelloWorld',
  components: {
    Dropdown,
    Datepicker,
    WidgetContainerModal: container
  },
  props: {
    cities: [],
  },
  data() {
    return {
      items: undefined,
      selected: <any> Object,
      date: '',
      data_set: [],
      distances: new Array<any>(),
      msg_result: '',
    };
  },
  watch: {
    cities() {
      this.items = this.cities;
    },
  },
  methods: {
      async open() {
        const modal = await openModal(CreateCity);
        modal.onclose = () => {
        console.log("closing");
          api
              .get('/cities')
              .then((response: { data: any; }) => response.data)
              .then((items: { results: undefined; }) => {
                  this.items = items.results
              })
        }
      },
      validateSelection(selection: {}) {
        this.selected = selection;
      },
    createResult(start: any, end: any, distance: any, city: any, date: any, earthquake: any) {

     },
      distance(lat1: number, lon1: number, lat2: number, lon2: number) {
         const p = 0.017453292519943295;    // Math.PI / 180
         const c = Math.cos;
         const a = 0.5 - c((lat2 - lat1) * p) / 2 +
             c(lat1 * p) * c(lat2 * p) *
             (1 - c((lon2 - lon1) * p)) / 2;

         return 12742 * Math.asin(Math.sqrt(a)); // 2 * R; R = 6371 km
      },
      search(){
        console.log("consultar",this.selected)
        const d_start = Date.parse(this.date[0])
        let ye_start = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d_start);
        let mo_start = new Intl.DateTimeFormat('en', { month: 'numeric' }).format(d_start);
        let da_start = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(d_start);
        const start = `${ye_start}-${mo_start}-${da_start}`
        const d_end = Date.parse(this.date[1])
        let ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d_end);
        let mo = new Intl.DateTimeFormat('en', { month: 'numeric' }).format(d_end);
        let da = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(d_end);
        const end = `${ye}-${mo}-${da}`
        api
          .get('https://earthquake.usgs.gov/fdsnws/event/1/query.geojson', {
            params: {
              starttime: start,
              endtime: end,
              minmagnitude: '4.5',
              orderby: 'time'
            },
          }, { cache: true })
          .then((response: { data: any; }) => response.data)
          .then((items: { features: never[]; }) => {
              this.distances = []
              this.data_set = items.features
              this.data_set.forEach((value : any) => {
                const p = 0.017453292519943295;    // Math.PI / 180
                const c = Math.cos;
                const a = 0.5 - c((this.selected.latitude - value.geometry.coordinates[0]) * p) / 2 +
                   c(value.geometry.coordinates[0] * p) * c(this.selected.latitude * p) *
                   (1 - c((this.selected.longitude - value.geometry.coordinates[1]) * p)) / 2;
                value.distance =  12742 * Math.asin(Math.sqrt(a)); // 2 * R; R = 6371 km
                this.distances.push(value)
              })
              this.distances.sort(function(a, b) {
                  return parseFloat(a.distance) - parseFloat(b.distance);
              });
              let earthquake_time = new Date(this.distances[0].properties.time)
              let earthquake_time_str = ""+earthquake_time.getFullYear()+
                "-"+(earthquake_time.getMonth()+1)+
                "-"+earthquake_time.getDate()

              this.msg_result = `Result for ${this.selected.name} between ${start} and ${end}:
              The closest Earthquake to ${this.selected.name} was ${this.distances[0].properties.title} on
              ${earthquake_time_str} distance: ${this.distances[0].distance}`
              console.log({
                        "start_date": start,
                        "end_date": end,
                        "distance": this.distances[0].distance,
                        "city": this.selected.id,
                        "date": earthquake_time_str,
                        "earthquake": this.distances[0].properties.title
                    })
              api
                  .post('/result/', {
                        "start_date": start,
                        "end_date": end,
                        "distance": this.distances[0].distance,
                        "city": this.selected.id,
                        "date": earthquake_time_str,
                        "earthquake": this.distances[0].properties.title
                    })
                  .then((response: { data: any; }) => response.data)
          })
      },
  },
  setup() {

  },
  created() {
     this.items = this.cities
  }
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
