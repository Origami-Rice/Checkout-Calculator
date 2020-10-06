<template>
  <view class="container">
    <Statusbar color="#FFCE00" />
    <Header title="Calculator" />

    <view class="inputContainer">
      <text-input class="input" placeholder="Item" v-model="newItemText" />
      <touchable-opacity class="add-btn" :on-press="newItem">
        <text class="btn-text">ADD</text>
      </touchable-opacity>
    </view>
    <view class="info-container">
      <text-input class="input" placeholder="Tax" v-model="newTax" />
      <text-input class="input" placeholder="Discount" v-model="newDiscount" />
    </view>
    <scroll-view>
      <view class="item" v-for="item in items" :key="item.id">
        <text class="item-text">{{item.title}}</text>
        <text class="price">${{item.price}}</text>
        <text class="quantity">{{item.quantity}}</text>
        <view class="item-buttons">
          <touchable-opacity class="plus-btn" :on-press="() => plusItem(item)">
            <text class="plus-btn-text">+</text>
          </touchable-opacity>
          <touchable-opacity class="minus-btn" :on-press="() => minusItem(item)">
            <text class="minus-btn-text">-</text>
          </touchable-opacity>
          <touchable-opacity class="remove-btn" :on-press="() => removeItem(item.id)">
            <text class="remove-btn-text">x</text>
          </touchable-opacity>
        </view>
      </view>
    </scroll-view>

    <view class="output">
      <text class="total-cost">Total ${{total}}</text>
    </view>
    <button class="compute" title="Compute" :on-press="() => computeTotal()"></button>
    <button class="reset" title="Reset" :on-press="() => reset()"></button>
    <button class="submit" title="Submit" :on-press="() => submit()"></button>
  </view>
</template>

<script>
import Statusbar from "./components/Statusbar";
import Header from "./components/Header";

export default {
  components: {
    Statusbar,
    Header,
  },
  data() {
    return {
      newItemText: "",
      /*
      items: [
        {
          id: 0,
          title: "Apple",
          price: 2,
          quantity: 1,
        },
        {
          id: 1,
          title: "Orange",
          price: 3,
          quantity: 1,
        },
      ],
*/
      newDiscount: 0,
      newTax: 0,
      total: 0,
      items: {},
      inventory: {},
    };
  },

  beforeMount() {
    fetch("https://uoftcsc301.herokuapp.com/getCatalogue")
      .then((resp) => resp.json())
      .then((datat) => (this.items = datat.catalogue));
  },
  mounted() {
    fetch("https://uoftcsc301.herokuapp.com/getCatalogue")
      .then((resp) => resp.json())
      .then((datat) => (this.inventory = datat.catalogue));
  },
  methods: {
    newItem() {
      /*if the new item is already in the list, just increase the quantity by 1 */
      for (var i = 0; i < this.items.length; i++) {
        if (this.items[i].title == this.newItemText) {
          this.items[i].quantity += 1;
          this.newItemText = "";
          return;
        }
      }

      var existingPrice = 0;
      for (var j = 0; j < this.inventory.length; j++) {
        if (this.inventory[j].title == this.newItemText) {
          existingPrice = this.inventory[j].price;
        }
      }
      /*if newItem is in inventory list, retrieve the price */
      if (existingPrice == 0) {
        this.items.push({
          id: this.items.length + 1,
          title: this.newItemText,
          price: 5,
          quantity: 1,
        });
      } else {
        this.items.push({
          id: this.items.length + 1,
          title: this.newItemText,
          price: existingPrice,
          quantity: 1,
        });
      }

      this.newItemText = "";
    },
    removeItem(id) {
      this.items = this.items.filter((item) => item.id !== id);
    },
    plusItem(item) {
      item.quantity = item.quantity + 1;
    },
    minusItem(item) {
      item.quantity = item.quantity - 1;
      if (item.quantity == 0) {
        this.removeItem(item.id);
      }
    },
    computeTotal() {
      this.total = 0;
      for (var i = 0; i < this.items.length; i++) {
        this.total += this.items[i].price * this.items[i].quantity;
      }
      this.total =
        this.total *
        (parseInt(1) - parseFloat(this.newDiscount)) *
        (parseInt(1) + parseFloat(this.newTax));
      this.total = this.total.toFixed(2);
    },

    submit() {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.items),
      };

      fetch("https://uoftcsc301.herokuapp.com/submit", requestOptions);
      /*
        fetch("http://localhost:5000/submit")
          .then((response) => response.json())
          .then((data) => (this.items = data.catalogue));
          */
    },
    reset() {
      fetch("https://uoftcsc301.herokuapp.com/getCatalogue")
        .then((resp) => resp.json())
        .then((datat) => (this.items = datat.catalogue));
      this.total = 0;
    },
  },
};
</script>

<style>
.container {
  background-color: white;
  flex: 1;
}
.inputContainer {
  flex-direction: row;
  justify-content: center;
  align-items: stretch;
}
.input {
  flex: 1;
  height: 35px;
  background-color: #f3f3f3;
  font-size: 18px;
  color: #888888;
}
.add-btn {
  width: 100px;
  height: 35px;
  background-color: #ffce00;
  justify-content: center;
  align-items: center;
}
.btn-text {
  font-size: 18px;
  font-weight: 700;
}
.item {
  flex-direction: row;
  justify-content: space-between;
  padding: 15px;
}
.item-text {
  font-size: 18px;
}
.remove-btn-text {
  margin-left: 27px;
  font-size: 18px;
  color: red;
}
.plus-btn-text {
  margin-left: 27px;
  font-size: 18px;
  color: blue;
}
.minus-btn-text {
  margin-left: 27px;
  font-size: 18px;
  color: green;
}
.item-buttons {
  flex-direction: row;
  justify-content: flex-end;
}
.price {
  justify-content: center;
  align-items: stretch;
}
.quantity {
  justify-content: center;
  align-items: stretch;
}
.info-container {
  flex-direction: row;
  justify-content: center;
  align-items: stretch;
  background-color: #d3d3d3;
}
.output {
  height: 40px;
  background-color: #171717;
  justify-content: center;
  align-items: center;
}
.total-cost {
  color: #f3f3f3;
  font-size: 28px;
  font-weight: 900;
  text-transform: uppercase;
  text-align: left;
}
</style>
