<template>
    <view class="statusbar" :style="{backgroundColor: color }"></view>
</template>

<script>
export default {
    props: ['color']
}
</script>

<style>
.statusbar{
    background-color: #ffce00;
    height: 20px;
}
</style>