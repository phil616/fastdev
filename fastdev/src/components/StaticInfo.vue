<template>
    <div>
      <h2>Child Component</h2>
      <p>Name: {{ name }}</p>
    </div>
  </template>
  
  <script>
  export default {
    computed: {
      name() {
        return this.$route.params.name;
      }
    }
  }
  </script>