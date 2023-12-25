import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import axios from 'axios';

import { BASE_DEVELOPMENT_URL, WATER_DEPTH_ENDPOINT } from "./UrlConstants";

Vue.use(Vuex);

// Define the Coordinate interface
interface Coordinate {
  latitude: number;
  longitude: number;
}

// Update the TileInfo interface
interface TileInfo {
  average_depth: number;
}

interface State {
  tileInfo: TileInfo | null;
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
    async fetchTileInfo({ commit }, coordinates: Coordinate[]) {
      try {
        const params = new URLSearchParams();
        coordinates.forEach((coord: Coordinate) => {
          params.append('coords', `${coord.latitude},${coord.longitude}`);
        });

        const apiUrl = `${BASE_DEVELOPMENT_URL}/${WATER_DEPTH_ENDPOINT}`;

        const response = await axios.get(apiUrl, { params });
        console.log(response)
        commit('setTileInfo', { average_depth: response.data.average_depth });
      } catch (error) {
        console.error('Error fetching tile info:', error);
      }
    },
  },
};

export default new Vuex.Store<State>(store);
