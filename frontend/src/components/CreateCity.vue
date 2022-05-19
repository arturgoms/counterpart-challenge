<template>
  <form class="city-create" id="city-create" @submit.prevent="createCity">
    <div class="city-create-container">
      <input v-model="form.name" type="text" id="name" name="name" placeholder="Name">
      <input v-model="form.country_code" type="text" id="country_code" name="country_code" placeholder="Country Code">
      <input v-model="form.latitude" type="number" id="latitude" name="latitude" placeholder="Latitude" step="0.000001">
      <input v-model="form.longitude" type="number" id="longitude" name="longitude" placeholder="Longitude" step="0.000001">
    </div>
    <button type="submit">Create</button>
  </form>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import axios from 'axios';
import {closeModal} from "jenesius-vue-modal"

export default defineComponent({
  name: 'ResultsView',
  emits: ["createFinish"],
  data() {
    return {
      form: {
        name: "",
        country_code: "",
        latitude: Number,
        longitude: Number,
      }
    };
  },
  methods: {
     createCity() {
        console.log(this.form)
        axios
            .post('http://localhost:8000/api/city/', {
                "name": this.form.name,
                "country_code": this.form.country_code,
                "latitude": this.form.latitude,
                "longitude": this.form.longitude
            })
            .then(response => response.data)
        closeModal()
        this.$emit("createFinish", true)
     }

  },
  created() {
  }
});
</script>
<style lang="scss">
.city-create {
  width: 50%;
  padding: 24px;
  background-color: white;
  border: solid 1px;
  .city-create-container{
    display: flex;
    flex-direction: column;
    width: 85%;
    margin-right: auto;
    margin-left: auto;

    input {
      margin-bottom: 16px;
      padding: 10px;
    }
  }
  button {
      padding: 10px 40px;
  }
}
</style>