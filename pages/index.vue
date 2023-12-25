<template>
  <div>
    <Toolbar />
    <!-- Additional components go here -->
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Toolbar from '~/components/Toolbar.vue';
import store from '../store/TilesViabilityStore'; // Adjust the extension if necessary
import { setDefaultCoordinates } from './utils/cookieManager';

export default Vue.extend({
    name: 'App', // Rename to 'App' for clarity, though the file name remains index.vue
    store, // Add the Vuex store here
    components: { Toolbar },
    created() {
      setDefaultCoordinates();
    }
})
</script>

<style>
/* Global styles for your app */
</style>
