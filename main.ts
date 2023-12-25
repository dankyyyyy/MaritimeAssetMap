import Vue from 'vue';
import App from './pages/index.vue';
import tilesViabilityStore from './store/TilesViabilityStore'; // Adjust the import path as needed

Vue.config.productionTip = false;

new Vue({
  store: tilesViabilityStore, // Correct way to register the store
  render: h => h(App),
}).$mount('#app');
