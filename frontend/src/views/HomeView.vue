<template>
    <div>
        HomeView
        <Title  :title="complexData" />
    </div>
</template>


<script>    
import Title from '../components/TitlePage.vue'
export default {
    components: {
        Title
    },
    name: 'HomeView',
    data() {
        return {
            complexData: {
                title: 'Welcome to our website',
                subtitle: 'This is a sample subtitle',
                description: 'This is a sample description'
            }

        }
    }
}

</script>