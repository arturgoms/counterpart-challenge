import axios from "axios";
import {throttleAdapterEnhancer} from "axios-extensions";
const api = axios.create({
    baseURL: 'http://localhost:8000/api',
    headers: {'Cache-Control': 'no-cache'},
    adapter: throttleAdapterEnhancer(axios.defaults.adapter, { threshold: 5 * 1000 })
})
export default api
