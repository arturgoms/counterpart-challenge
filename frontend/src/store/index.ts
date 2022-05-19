import { createStore } from 'vuex'
// @ts-ignore
import api from '@/services/api/cities'
import axios from "axios";


export default createStore({
  state: {
    allCities: []
  },
  getters: {
    allCities: (state) => state.allCities
  },
  mutations: {
    SET_CITIES(state, cities) {
    state.allCities = cities
  }
  },
  actions: {
    getAllCities({ commit }) {
      axios
          .get('http://localhost:8000/api/city')
          .then(response => response.data)
          .then(items => {
          commit('SET_Items', items)
        })
      }
  },
  modules: {
  }
})
