<template>
  <div class="wrapper">
    <div class="row">
      <router-link
        class="button"
        :to="{name: 'HomeView'}"
      >
        &#8592; Назад
      </router-link>
    </div>
    <div
      class="placeholder psychotherapist row"
      v-if="psychotherapistData === undefined"
    >
      <div class="photo placeholder__photo">
        <div class="photo__img placeholder-item" />
      </div>
      <div class="info wrapper">
        <div class="placeholder__name info__name placeholder-item" />
        <div class="info__methods wrapper">
          <div class="methods__text">Методы:</div>
          <div class="methods__container">
            <div
              class="placeholder__method methods__method placeholder-item"
              v-for="index in Array(3)"
              :key="index"
            />
          </div>
        </div>
      </div>
    </div>
    <div
      class="psychotherapist row"
      v-else
    >
      <div class="photo">
        <img
          class="photo__img"
          :src="psychotherapistData.photo_url_full"
          alt="aa"
        />
      </div>
      <div class="info wrapper">
        <div class="info__name">
          {{ psychotherapistData.name }}
        </div>
        <div class="methods wrapper">
          <span class="methods__text">Методы:</span>
          <div class="methods__container">
            <div
              class="methods__method"
              v-for="(method, index) in psychotherapistData.methods"
              :key="index"
              :style="{ 'grid-column': index % 4 + 1, background: methodColors[index % methodColors.length] }"
            >
              {{ method }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PsychotherapistInfoView',
  props: {
    id: {
      type: String,
      required: true,
    },
    psychotherapist: {
      type: Object,
      required: false,
    },
  },
  data () {
    return {
      psychotherapistData: this.psychotherapist,
      methodColors: [
        '#FFC107',
        '#1976D2',
        '#4CAF50',
        '#82B1FF',
        '#FF5252',
        '#2196F3'
      ],
    }
  },
  methods: {
    getColor () {
      let colorIndex = Math.ceil(Math.random() * this.methodColors.length)
      return this.methodColors[colorIndex]
    },
    loadContactData () {
      this.$_fetch(
        '/read_single',
        {
          id: this.id,
        }
      ).then(
        response => response.json()
      ).then(
        response => this.psychotherapistData = response
      )
    },
  },
  created () {
    if (this.psychotherapistData === undefined)
      this.loadContactData()
  },
}
</script>

<style lang="sass" scoped>
.placeholder
  min-width: 85vw
  &__photo
    min-height: 75vh
  &__name
    height: 2rem
  &__method
    max-width: 20%
    height: 1rem

.placeholder-item
  display: block
  width: 100%
  background: linear-gradient(to right, grey 10%, darkgrey 18%, grey 33%)

  animation-duration: 2s
  animation-fill-mode: forwards
  animation-iteration-count: infinite
  animation-name: placeholder
  animation-timing-function: linear
  background-size: 600% 100%

@keyframes placeholder
  0%
    background-position: 100% 0
  100%
    background-position: -200% 0

.row
  display: flex
  flex-flow: row wrap
  align-items: flex-start

.psychotherapist
  padding-top: 1rem

.photo
  display: flex
  flex: 3 0 30%
  &__img
    width: 100%

.info
  display: flex
  flex: 7 7
  &__name
    font-size: 2rem
    font-weight: 600

.methods
  display: flex
  flex-flow: column nowrap
  flex: 0 1 auto
  &__text
    font-size: 1.25rem
  &__container
    display: flex
    flex-flow: row wrap
    flex: 1 1 auto
    padding-top: 0.25rem
  &__method
    margin: 1rem
    border-radius: 1rem
    padding: 0.5rem 1rem
    text-align: center
    color: whitesmoke
</style>
