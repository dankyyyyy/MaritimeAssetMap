<template>
    <div class="toolbar">
      <button @click="fetchData">Fetch Data</button>
    </div>
  </template>
  
  <script>
  import Cookies from 'js-cookie';
  import { mapActions } from 'vuex';
  
  export default {
    name: 'Toolbar',
    methods: {
      ...mapActions(['fetchTileInfo']),
  
      fetchData() {
        const coordinates = JSON.parse(Cookies.get('coordinates') || '[]');
        coordinates.forEach(({ latitude, longitude }) => {
          this.fetchTileInfo({ latitude, longitude });
        });
      }
    }
  };
  </script>
  
  <style scoped>
  .toolbar {
    display: flex;
    justify-content: flex-end;
    padding: 10px;
    background-color: #f4f4f4;
    border-bottom: 1px solid #ccc;
  }
  
  .toolbar button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .toolbar button:hover {
    background-color: #0056b3;
  }
  </style>