<template>
    <div class="item">
      <text class="item-text">{{item.title}}</text>
      <touchable-opacity class="remove-btn" :on-press="() => removeItem(item.id)">
        <text class="remove-btn-text">X</text>
      </touchable-opacity>
    </div>
</template>

<script>
export default {
    name: "Item",
    props: ["item"]
}
</script>

<style scoped>
    .item{
    flex-direction: row;
    justify-content: space-between;
    padding: 15px;
    }
    .item-text{
    font-size: 18px;
    }
    .remove-btn-text{
    font-size: 18px; 
    color: red; 
    }
</style>