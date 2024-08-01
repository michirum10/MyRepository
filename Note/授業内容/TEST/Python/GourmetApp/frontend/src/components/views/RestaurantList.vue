// src/components/RestaurantList.vue
<template>
  <div>
    <h1>Restaurant List</h1>
    <ul>
      <li v-for="restaurant in allRestaurants" :key="restaurant.id">
        {{ restaurant.name }}
        <button @click="addToFavorites(restaurant)">Add to Favorites</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  computed: {
    allRestaurants() {
      return this.$store.getters.allRestaurants;
    }
  },
  methods: {
    addToFavorites(restaurant) {
      this.$store.dispatch('addFavorite', restaurant);
    }
  },
  created() {
    this.$store.dispatch('fetchRestaurants');
  }
};
</script>
