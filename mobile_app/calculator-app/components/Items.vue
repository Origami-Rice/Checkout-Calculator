<template>
    <div>
        <div v-bind:key="item.id" v-for="item in items">
            <Item />
        </div> 
    </div>
</template>

<script>
import Item from './Item.vue';

export default {
    name: "Items",
    components: {
        Item 
    },
    props: ["items"]
}
</script>

<style scoped>

</style>
