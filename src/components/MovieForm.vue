<template>
    <form @submit.prevent="saveMovie" id="movieForm">
        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="form-control" v-model="title" />
        </div>
        <div class="form-group mb-3">
            <label for="description" class="form-label">Description</label>
            <input type="text" name="description" class="form-control" v-model="description" />
        </div>
        <div class="form-group mb-3">
            <label for="poster" class="form-label">Poster</label>
            <input type="file" name="poster" class="formcontrol" accept=".jpg,.png" />
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
    </form>
</template>

<script setup>
    import {
        ref,
        onMounted
    } from 'vue';
    onMounted(() => {
        getCsrfToken();
    });
    let csrf_token = ref("");
    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                csrf_token.value = data.csrf_token;
            })
    }
    // const title = ref('');
    // const description = ref('');
    // const poster = ref('');
    function saveMovie(){
        let uploadForm = document.querySelector("#movieForm")
        let formData = new FormData(uploadForm)
        fetch("/api/v1/movies", {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
        })
        .catch(function (error) {
            console.log(error);
        });
    }
</script>

  
