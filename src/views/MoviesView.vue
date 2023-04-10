<template>
    <h1>Movies</h1>
    <ul>
        <div class="container">
    <div class="row">
      <div class="col-md-6 mb-4" v-for="movie in movies" :key="movie.id">
        <div class="card">
          <img :src="movie.poster.split('/').pop()" class="card-img-top" alt="Movie Poster">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
    </ul>
</template>

<script setup>
    import { ref, onMounted } from "vue";

    let movies = ref([]);

    function fetchMovies() {
        fetch("/api/v1/movies")
            .then(response => response.json())
            .then(data => {
                movies.value = data.movies;
            })
            .catch(error => console.log(error));
    }

    onMounted(() => {
        fetchMovies();
    });
</script>

<style>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  display: flex;
  flex-direction: row;
  width: 100%;
  margin: 1rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.card img {
  width: 100%;
  height: 300px;
  border-radius: 5px;
}

.card-body {
  padding: 1rem;
  text-align: center;
}
</style>