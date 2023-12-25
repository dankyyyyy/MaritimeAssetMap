import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

interface State {
  tileInfo: TileInfo | null;
}

interface TileInfo {
  latitude: number;
  longitude: number;
  depth: number;
}

const store: StoreOptions<State> = {
  state: {
    tileInfo: null,
  },
  mutations: {
    setTileInfo(state, info: TileInfo) {
      state.tileInfo = info;
    },
  },
  actions: {
    async fetchTileInfo({ commit }, { latitude, longitude }: { latitude: number, longitude: number }) {
      try {
        const response = await axios.get(`http://localhost:8000/api/v1/water-depth?lat=${latitude}&lon=${longitude}`);
        commit('setTileInfo', { latitude, longitude, depth: response.data.depth });
      } catch (error) {
        console.error('Error fetching tile info:', error);
        // Additional error handling as needed
      }
    },
  },
};

export default new Vuex.Store<State>(store);
